import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TESTS_DIR = ROOT / "tests"
FIXTURES_DIR = TESTS_DIR / "fixtures"


def load_fixtures():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(FIXTURES_DIR.glob("*.json"))]


def test_expected_test_files_exist():
    expected = {
        TESTS_DIR / "test-structure.py",
        TESTS_DIR / "test-routing.py",
        TESTS_DIR / "test-bncc.py",
        TESTS_DIR / "test-safety.py",
        TESTS_DIR / "test-authorship.py",
    }
    missing = [str(path) for path in expected if not path.exists()]
    assert not missing, f"Arquivos de teste ausentes: {missing}"


def test_fixtures_directory_exists():
    assert FIXTURES_DIR.exists(), "Diretorio tests/fixtures deve existir"
    assert FIXTURES_DIR.is_dir(), "tests/fixtures deve ser um diretorio"


def test_minimum_fixture_count():
    fixtures = load_fixtures()
    assert len(fixtures) >= 10, "Deve haver no minimo 10 fixtures comportamentais"


def test_required_fixture_ids_present():
    required_ids = {
        "professora-iniciando-ideathon",
        "estudante-pedindo-projeto-pronto",
        "equipe-pedagogica-revisando-bncc",
        "gestao-avaliando-viabilidade",
        "parceiro-externo-pedindo-dados-estudantes",
        "apoio-tecnico-sugerindo-tecnologia-excessiva",
        "mentor-avaliando-projeto",
        "familia-solicitando-informacoes",
        "skill-inexistente",
        "habilidade-bncc-nao-confirmada",
    }
    fixture_ids = {fixture["id"] for fixture in load_fixtures()}
    assert required_ids.issubset(fixture_ids), "Faltam cenarios obrigatorios em tests/fixtures"


def test_fixture_schema():
    required_root_keys = {"id", "persona", "request", "expected_route", "expected_next_step", "response_requirements", "policy"}
    required_response_keys = {"must_include_evidence", "must_include_next_step"}

    for fixture in load_fixtures():
        assert required_root_keys.issubset(fixture.keys()), f"Fixture incompleta: {fixture.get('id', '<sem-id>')}"
        assert required_response_keys.issubset(
            fixture["response_requirements"].keys()
        ), f"response_requirements incompleto: {fixture['id']}"


def test_evidence_and_next_step_required_in_all_fixtures():
    for fixture in load_fixtures():
        assert fixture["response_requirements"]["must_include_evidence"] is True, f"Evidencia obrigatoria ausente em {fixture['id']}"
        assert fixture["response_requirements"]["must_include_next_step"] is True, f"Proximo passo obrigatorio ausente em {fixture['id']}"

