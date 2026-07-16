import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = ROOT / "tests" / "fixtures"


def load_fixtures():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(FIXTURES_DIR.glob("*.json"))]


def fixture_by_id(fixture_id):
    fixtures = {fixture["id"]: fixture for fixture in load_fixtures()}
    return fixtures[fixture_id]


def test_privacy_rules_exist_in_core_documents():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    acompanhar = (ROOT / "skills" / "acompanhar-desenvolvimento" / "SKILL.md").read_text(encoding="utf-8")
    preparar = (ROOT / "skills" / "preparar-pitch" / "SKILL.md").read_text(encoding="utf-8")

    assert "protecao de dados dos estudantes" in agents
    assert "Nao coletar ou publicar dados pessoais desnecessarios." in acompanhar
    assert "Nao expor dados pessoais, credenciais ou segredos na apresentacao." in preparar


def test_external_partner_request_is_blocked_for_student_privacy():
    fixture = fixture_by_id("parceiro-externo-pedindo-dados-estudantes")
    assert fixture["expected_route"] is None
    assert fixture["policy"]["forbid_personal_data_sharing"] is True
    assert fixture["policy"]["protect_student_privacy"] is True


def test_family_request_keeps_institutional_and_teacher_channel():
    fixture = fixture_by_id("familia-solicitando-informacoes")
    assert fixture["expected_route"] is None
    assert fixture["policy"]["preserve_teacher_role"] is True
    assert "equipe docente" in fixture["expected_next_step"]


def test_agent_does_not_replace_teacher_in_fixtures():
    for fixture in load_fixtures():
        assert fixture["policy"]["preserve_teacher_role"] is True, f"Risco de substituicao docente em {fixture['id']}"

