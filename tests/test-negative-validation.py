import importlib.util
from pathlib import Path

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
DEPENDENCY_MODULE_PATH = ROOT / "tests" / "test-dependencies.py"
GUARDRAIL_MODULE_PATH = ROOT / "scripts" / "validate-guardrails.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def dependency_validator():
    return load_module("dependency_validator_negative", DEPENDENCY_MODULE_PATH)


@pytest.fixture
def guardrail_validator():
    return load_module("guardrail_validator_negative", GUARDRAIL_MODULE_PATH)


def test_guardrail_loader_rejects_invalid_yaml(tmp_path, monkeypatch, guardrail_validator):
    invalid_file = tmp_path / "invalid-policy.yaml"
    invalid_file.write_text("rules: [\n  - id: broken\n", encoding="utf-8")
    monkeypatch.setattr(guardrail_validator, "ROOT", tmp_path)

    with pytest.raises(ValueError, match="YAML invalido"):
        guardrail_validator.load_policy(invalid_file)


def test_guardrail_schema_rejects_duplicate_rule_ids(guardrail_validator):
    rule = {
        "id": "gr-duplicada",
        "fase": "entrada",
        "categoria": "teste",
        "descricao": "Regra de teste.",
        "condicao": {"type": "keyword_any", "patterns": ["teste"]},
        "nivel": "block",
        "acao": "bloquear",
        "mensagem": "Bloqueado.",
        "revisao_humana": True,
        "evidencia_exigida": ["registro"],
    }
    policy = {
        "metadata": {},
        "levels": ["info", "warning", "block", "escalate"],
        "rules": [rule, dict(rule)],
    }

    errors = guardrail_validator.validate_policy_schema(policy)

    assert "id duplicado: gr-duplicada" in errors


def test_thematic_alignment_rejects_unknown_rule_id(
    tmp_path, monkeypatch, guardrail_validator
):
    module_name = "invalid-module.yaml"
    (tmp_path / module_name).write_text(
        yaml.safe_dump(
            {
                "source_of_truth": "policy.yaml",
                "rule_ids": ["gr-inexistente"],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(guardrail_validator, "ROOT", tmp_path)
    monkeypatch.setattr(guardrail_validator, "GUARDRAILS_DIR", tmp_path)
    monkeypatch.setattr(guardrail_validator, "THEMATIC_FILES", (module_name,))
    policy = {"rules": [], "modules": {module_name: ["gr-inexistente"]}}

    errors = guardrail_validator.validate_thematic_alignment(policy)

    assert any("regras tematicas inexistentes em policy" in error for error in errors)


def test_catalog_loader_rejects_invalid_yaml(tmp_path, monkeypatch, dependency_validator):
    catalog = tmp_path / "catalog.yaml"
    catalog.write_text("skills: [\n  - name: broken\n", encoding="utf-8")
    monkeypatch.setattr(dependency_validator, "ROOT", tmp_path)
    monkeypatch.setattr(dependency_validator, "CATALOG_PATH", catalog)

    with pytest.raises(AssertionError, match="YAML invalido"):
        dependency_validator.parse_catalog_entries()


def test_frontmatter_loader_rejects_non_list_contract(
    tmp_path, monkeypatch, dependency_validator
):
    skill_dir = tmp_path / "skills" / "skill-teste"
    skill_dir.mkdir(parents=True)
    skill_file = skill_dir / "SKILL.md"
    skill_file.write_text(
        """---
name: skill-teste
metadata:
  depends-on: outra-skill
---
# Skill teste
""",
        encoding="utf-8",
    )
    monkeypatch.setattr(dependency_validator, "ROOT", tmp_path)

    frontmatter = dependency_validator.load_skill_frontmatter(skill_file)
    with pytest.raises(AssertionError, match="metadata.depends-on deve ser lista"):
        dependency_validator.metadata_list(frontmatter, "skill-teste", "depends-on")


def test_cycle_fixture_is_detected(dependency_validator):
    graph = {
        "skill-a": ["skill-c"],
        "skill-b": ["skill-a"],
        "skill-c": ["skill-b"],
    }

    cycle = dependency_validator.find_cycle(graph)

    assert cycle is not None
    assert cycle[0] == cycle[-1]
    assert set(cycle[:-1]) == {"skill-a", "skill-b", "skill-c"}


def test_orphan_fixture_is_not_reachable_from_root(dependency_validator):
    graph = {
        "raiz": [],
        "conectada": ["raiz"],
        "orfa": [],
    }

    reachable = dependency_validator.reachable_from_root(graph, "raiz")

    assert reachable == {"raiz", "conectada"}
    assert "orfa" not in reachable


def test_evidence_without_origin_is_rejected(monkeypatch, dependency_validator):
    graph = {"raiz": [], "seguinte": ["raiz"]}
    contracts = {
        "raiz": {
            "depends_on": [],
            "required_evidence": [],
            "produces": ["artefato-disponivel"],
        },
        "seguinte": {
            "depends_on": ["raiz"],
            "required_evidence": ["artefato-inexistente"],
            "produces": ["resultado"],
        },
    }
    monkeypatch.setattr(dependency_validator, "catalog_graph", lambda: graph)
    monkeypatch.setattr(dependency_validator, "skill_contracts", lambda: contracts)
    monkeypatch.setattr(dependency_validator, "EXTERNAL_EVIDENCE", set())

    with pytest.raises(AssertionError, match="Evidencias sem origem rastreavel"):
        dependency_validator.test_required_evidence_is_available_from_ancestors_or_external_inputs()


def test_dependency_without_direct_handoff_is_rejected(
    monkeypatch, dependency_validator
):
    graph = {"raiz": [], "seguinte": ["raiz"]}
    contracts = {
        "raiz": {
            "depends_on": [],
            "required_evidence": [],
            "produces": ["produto-da-raiz"],
        },
        "seguinte": {
            "depends_on": ["raiz"],
            "required_evidence": ["entrada-externa"],
            "produces": ["resultado"],
        },
    }
    monkeypatch.setattr(dependency_validator, "catalog_graph", lambda: graph)
    monkeypatch.setattr(dependency_validator, "skill_contracts", lambda: contracts)

    with pytest.raises(AssertionError, match="Sem handoff semantico direto"):
        dependency_validator.test_each_dependency_edge_has_direct_semantic_handoff()


def test_duplicate_evidence_contract_is_rejected(monkeypatch, dependency_validator):
    contracts = {
        "skill-teste": {
            "depends_on": [],
            "required_evidence": ["evidencia", "evidencia"],
            "produces": ["resultado"],
        }
    }
    monkeypatch.setattr(dependency_validator, "skill_contracts", lambda: contracts)

    with pytest.raises(AssertionError, match="Valores duplicados"):
        dependency_validator.test_evidence_contracts_have_no_duplicates()
