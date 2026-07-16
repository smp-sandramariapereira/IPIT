import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES_DIR = ROOT / "tests" / "fixtures"
SKILLS_DIR = ROOT / "skills"
ORCHESTRATOR_FILE = SKILLS_DIR / "orquestrar-ipit" / "SKILL.md"


def load_fixtures():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(FIXTURES_DIR.glob("*.json"))]


def fixture_by_id(fixture_id):
    fixtures = {fixture["id"]: fixture for fixture in load_fixtures()}
    return fixtures[fixture_id]


def available_skill_names():
    return {path.parent.name for path in SKILLS_DIR.glob("*/SKILL.md")}


def test_expected_routes_target_existing_skills():
    valid_skills = available_skill_names()
    for fixture in load_fixtures():
        route = fixture["expected_route"]
        if route is not None:
            assert route in valid_skills, f"Rota para skill inexistente em {fixture['id']}: {route}"


def test_professora_iniciando_ideathon_routes_to_iniciar():
    fixture = fixture_by_id("professora-iniciando-ideathon")
    assert fixture["expected_route"] == "iniciar-ideathon"
    assert fixture["persona"] in {"professora", "professor"}


def test_skill_inexistente_routes_to_safe_fallback():
    fixture = fixture_by_id("skill-inexistente")
    assert fixture["expected_route"] is None
    assert "skill indisponivel" in fixture["expected_next_step"]


def test_routing_respects_dependency_chain_in_orchestrator():
    content = ORCHESTRATOR_FILE.read_text(encoding="utf-8")
    assert "`iniciar-ideathon` -> `orquestrar-ipit` -> `planejar-arquitetura`" in content
    assert "`planejar-arquitetura` -> `acompanhar-desenvolvimento` -> `preparar-pitch`" in content


def test_persona_coverage_for_routing_scenarios():
    personas = {fixture["persona"] for fixture in load_fixtures()}
    expected_personas = {
        "professora",
        "estudante",
        "equipe-pedagogica",
        "gestao-escolar",
        "parceiro-externo",
        "apoio-tecnico",
        "mentor",
        "familia",
        "professor",
    }
    assert expected_personas.issubset(personas), "Cobertura de personas insuficiente nos fixtures"

