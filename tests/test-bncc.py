import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AGENTS_FILE = ROOT / "AGENTS.md"
FIXTURES_DIR = ROOT / "tests" / "fixtures"

# Padroes comuns de codigos BNCC, ex.: EM13LGG101, EF69LP01
BNCC_CODE_PATTERN = re.compile(r"\b(?:EM|EF)\d{2}[A-Z]{2,3}\d{2,3}\b")


def load_fixtures():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(FIXTURES_DIR.glob("*.json"))]


def test_agents_has_bncc_policy_guards():
    content = AGENTS_FILE.read_text(encoding="utf-8")
    assert "Nunca inventar codigos da BNCC." in content
    assert '"a validar pela equipe pedagogica"' in content


def test_bncc_validation_phrase_present_in_all_skills():
    for skill_file in ROOT.glob("skills/*/SKILL.md"):
        content = skill_file.read_text(encoding="utf-8")
        assert (
            "a validar pela equipe pedagogica" in content
        ), f"Skill sem frase de validacao BNCC: {skill_file}"


def test_repository_does_not_introduce_fabricated_bncc_codes():
    # Permite referencias em documentos externos existentes, mas bloqueia em AGENTS/skills.
    restricted_files = [AGENTS_FILE, *ROOT.glob("skills/*/SKILL.md")]
    for file_path in restricted_files:
        content = file_path.read_text(encoding="utf-8")
        assert not BNCC_CODE_PATTERN.search(content), f"Possivel codigo BNCC inventado em {file_path}"


def test_fixture_for_unconfirmed_bncc_requires_validation_flow():
    fixture = next(f for f in load_fixtures() if f["id"] == "habilidade-bncc-nao-confirmada")
    assert fixture["policy"]["requires_bncc_validation_phrase"] is True
    assert "a validar pela equipe pedagogica" in fixture["expected_next_step"]

