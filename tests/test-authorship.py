import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = ROOT / "tests" / "fixtures"
AGENTS_FILE = ROOT / "AGENTS.md"
POLICY_FILE = ROOT / "guardrails" / "policy.yaml"


def load_fixtures():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(FIXTURES_DIR.glob("*.json"))]


def skill_files_with_frontmatter():
    return [path for path in ROOT.glob("skills/*/SKILL.md") if path.read_text(encoding="utf-8").startswith("---")]


def extract_frontmatter(content):
    match = re.match(r"^---\n(.*?)\n---\n", content, flags=re.DOTALL)
    assert match, "Frontmatter YAML ausente"
    return match.group(1)


def test_frontmatter_skills_declare_author():
    for skill_file in skill_files_with_frontmatter():
        frontmatter = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
        assert re.search(r"^\s*author:\s*.+$", frontmatter, flags=re.MULTILINE), f"author ausente em {skill_file}"


def test_frontmatter_skills_require_human_review():
    for skill_file in skill_files_with_frontmatter():
        frontmatter = extract_frontmatter(skill_file.read_text(encoding="utf-8"))
        assert re.search(
            r"^\s*requires-human-review:\s*true\s*$", frontmatter, flags=re.MULTILINE
        ), f"requires-human-review true ausente em {skill_file}"


def test_student_ready_made_project_request_protects_authorship():
    fixture = next(f for f in load_fixtures() if f["id"] == "estudante-pedindo-projeto-pronto")
    assert fixture["policy"]["forbid_ready_made_project"] is True
    assert fixture["policy"]["protect_student_authorship"] is True


def test_all_fixtures_protect_student_authorship():
    for fixture in load_fixtures():
        assert fixture["policy"]["protect_student_authorship"] is True, f"Autoria estudantil nao protegida em {fixture['id']}"


def test_ai_usage_and_authorship_traceability_are_documented():
    acompanhar = (ROOT / "skills" / "acompanhar-desenvolvimento" / "SKILL.md").read_text(encoding="utf-8")
    preparar = (ROOT / "skills" / "preparar-pitch" / "SKILL.md").read_text(encoding="utf-8")
    assert "Registrar uso de IA" in acompanhar
    assert "Declarar uso de IA" in preparar


def test_methodology_authorship_is_explicitly_preserved():
    agents = AGENTS_FILE.read_text(encoding="utf-8")
    assert "Sandra Maria Pereira" in agents
    assert "Bloquear remocao de autoria estudantil e da autoria metodologica de Sandra Maria Pereira." in agents


def test_authorship_guardrails_are_present_in_policy():
    content = POLICY_FILE.read_text(encoding="utf-8")
    assert "gr-autoria-estudantil-preservar" in content
    assert "gr-autoria-sandra-preservar" in content

