#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "guardrails" / "policy.yaml"
GUARDRAILS_DIR = ROOT / "guardrails"

THEMATIC_FILES = (
    "pedagogical.yaml",
    "bncc.yaml",
    "privacy.yaml",
    "safety.yaml",
    "authorship.yaml",
    "tool-use.yaml",
    "response-contract.yaml",
)

REQUIRED_LEVELS = {"info", "warning", "block", "escalate"}
REQUIRED_RULE_FIELDS = {
    "id",
    "fase",
    "categoria",
    "descricao",
    "condicao",
    "nivel",
    "acao",
    "mensagem",
    "revisao_humana",
    "evidencia_exigida",
}
BLOCKING_MIN_RULE_IDS = {
    "gr-bncc-codigo-nao-verificado",
    "gr-privacidade-dados-estudantes",
    "gr-seguranca-credenciais",
    "gr-ferramentas-codigo-nao-revisado",
    "gr-autoria-estudantil-preservar",
    "gr-protecao-menores-imagens",
    "gr-seguranca-armazenamento-sensivel",
    "gr-prompt-injection",
    "gr-pedagogia-projeto-pronto",
    "gr-decisao-institucional-automatica",
}


def load_yaml_mapping(path: Path) -> dict[str, Any]:
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML invalido em {path.relative_to(ROOT)}: {exc}") from exc

    if not isinstance(loaded, dict):
        raise ValueError(f"Documento YAML deve ser um objeto em {path.relative_to(ROOT)}")
    return loaded


def load_policy(path: Path = POLICY_PATH) -> dict[str, Any]:
    return load_yaml_mapping(path)


def load_thematic_modules() -> dict[str, dict[str, Any]]:
    modules: dict[str, dict[str, Any]] = {}
    for filename in THEMATIC_FILES:
        file_path = GUARDRAILS_DIR / filename
        if file_path.exists():
            modules[filename] = load_yaml_mapping(file_path)
    return modules


def load_thematic_rule_ids() -> dict[str, set[str]]:
    rule_ids: dict[str, set[str]] = {}
    modules = load_thematic_modules()
    for filename in THEMATIC_FILES:
        module = modules.get(filename)
        if module is None:
            rule_ids[filename] = set()
            continue
        values = module.get("rule_ids", [])
        if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
            raise ValueError(f"rule_ids deve ser lista de strings em guardrails/{filename}")
        rule_ids[filename] = set(values)
    return rule_ids


def validate_thematic_alignment(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy_rules = policy.get("rules", [])
    policy_rule_ids = {
        rule.get("id") for rule in policy_rules if isinstance(rule, dict) and rule.get("id")
    }

    try:
        thematic_modules = load_thematic_modules()
        thematic_rule_ids = load_thematic_rule_ids()
    except ValueError as exc:
        return [str(exc)]

    union_thematic_ids = set().union(*thematic_rule_ids.values()) if thematic_rule_ids else set()

    for filename in THEMATIC_FILES:
        file_path = GUARDRAILS_DIR / filename
        if not file_path.exists():
            errors.append(f"arquivo tematico ausente: guardrails/{filename}")
            continue

        module = thematic_modules.get(filename, {})
        if module.get("source_of_truth") != "policy.yaml":
            errors.append(f"source_of_truth ausente ou invalido em guardrails/{filename}")

        declared_ids = module.get("rule_ids")
        if not isinstance(declared_ids, list):
            errors.append(f"rule_ids ausente ou invalido em guardrails/{filename}")
        elif len(declared_ids) != len(set(declared_ids)):
            errors.append(f"rule_ids duplicados em guardrails/{filename}")

    missing_in_thematic = policy_rule_ids - union_thematic_ids
    if missing_in_thematic:
        errors.append(f"regras da policy sem mapeamento tematico: {sorted(missing_in_thematic)}")

    unknown_in_thematic = union_thematic_ids - policy_rule_ids
    if unknown_in_thematic:
        errors.append(f"regras tematicas inexistentes em policy: {sorted(unknown_in_thematic)}")

    modules = policy.get("modules")
    if not isinstance(modules, dict):
        errors.append("campo modules ausente ou invalido em guardrails/policy.yaml")
        return errors

    missing_module_files = set(THEMATIC_FILES) - set(modules)
    if missing_module_files:
        errors.append(f"modules sem arquivos tematicos obrigatorios: {sorted(missing_module_files)}")

    extra_module_files = set(modules) - set(THEMATIC_FILES)
    if extra_module_files:
        errors.append(f"modules com arquivos nao reconhecidos: {sorted(extra_module_files)}")

    for filename in THEMATIC_FILES:
        module_ids = modules.get(filename, [])
        if not isinstance(module_ids, list) or not all(
            isinstance(value, str) for value in module_ids
        ):
            errors.append(f"modules[{filename}] deve ser lista de strings")
            continue
        if len(module_ids) != len(set(module_ids)):
            errors.append(f"modules[{filename}] contem ids duplicados")

        module_id_set = set(module_ids)
        thematic_id_set = thematic_rule_ids.get(filename, set())
        if module_id_set != thematic_id_set:
            errors.append(
                f"divergencia entre policy.modules e guardrails/{filename}: "
                f"modules={sorted(module_id_set)} thematic={sorted(thematic_id_set)}"
            )

    return errors


def _contains_bncc_code(text: str) -> bool:
    return bool(re.search(r"\b(?:EM|EF)\d{2}[A-Z]{2,3}\d{2,3}\b", text))


def _evaluate_rule(rule: dict[str, Any], payload: dict[str, Any], phase: str) -> bool:
    if rule["fase"] != phase:
        return False

    cond = rule["condicao"]
    cond_type = cond.get("type")
    text = payload.get("text", "").lower()

    if cond_type == "keyword_any":
        return any(pattern.lower() in text for pattern in cond.get("patterns", []))
    if cond_type == "missing_flag":
        return not bool(payload.get(cond.get("flag")))
    if cond_type == "missing_evidence_or_next_step":
        evidence_field = cond.get("evidence_field", "evidencias")
        next_step_field = cond.get("next_step_field", "proximo_passo")
        return not payload.get(evidence_field) or not str(payload.get(next_step_field)).strip()
    if cond_type == "institutional_decision_without_review":
        return bool(payload.get("decisao_institucional")) and not bool(
            payload.get("revisao_humana_registrada")
        )
    if cond_type == "bncc_unverified_definitive":
        raw_text = payload.get("text", "")
        lowered = raw_text.lower()
        has_code = _contains_bncc_code(raw_text)
        has_claim = "bncc" in lowered and "definitiv" in lowered
        has_validation = "a validar pela equipe pedagogica" in lowered
        return (has_code or has_claim) and not has_validation
    if cond_type == "missing_context_keyword":
        required = [kw.lower() for kw in cond.get("required_keywords", [])]
        return any(kw not in text for kw in required)
    return False


def evaluate_payload(
    policy: dict[str, Any], payload: dict[str, Any], phase: str
) -> list[dict[str, Any]]:
    return [
        rule
        for rule in policy.get("rules", [])
        if isinstance(rule, dict) and _evaluate_rule(rule, payload, phase)
    ]


def validate_policy_schema(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if not isinstance(policy.get("metadata"), dict):
        errors.append("metadata ausente ou invalido")
    rules = policy.get("rules")
    if not isinstance(rules, list) or not rules:
        errors.append("rules ausente ou vazio")
        return errors

    levels_value = policy.get("levels", [])
    if not isinstance(levels_value, list):
        errors.append("levels deve ser lista")
        levels_value = []
    levels = set(levels_value)
    if not REQUIRED_LEVELS.issubset(levels):
        errors.append(f"levels incompleto: esperado {sorted(REQUIRED_LEVELS)}")

    phases: set[str] = set()
    ids: set[str] = set()
    block_ids: set[str] = set()

    for idx, rule in enumerate(rules, start=1):
        if not isinstance(rule, dict):
            errors.append(f"regra #{idx} deve ser objeto")
            continue
        missing = REQUIRED_RULE_FIELDS - set(rule)
        if missing:
            errors.append(f"regra #{idx} com campos ausentes: {sorted(missing)}")
            continue

        rule_id = rule["id"]
        if not isinstance(rule_id, str) or not rule_id:
            errors.append(f"id invalido na regra #{idx}")
            continue
        if rule_id in ids:
            errors.append(f"id duplicado: {rule_id}")
        ids.add(rule_id)

        if rule["nivel"] not in REQUIRED_LEVELS:
            errors.append(f"nivel invalido em {rule_id}: {rule['nivel']}")
        if rule["fase"] not in {"entrada", "saida"}:
            errors.append(f"fase invalida em {rule_id}: {rule['fase']}")
        phases.add(rule["fase"])

        if not isinstance(rule["condicao"], dict):
            errors.append(f"condicao invalida em {rule_id}")
        if not isinstance(rule["evidencia_exigida"], list) or not rule["evidencia_exigida"]:
            errors.append(f"evidencia_exigida invalida em {rule_id}")
        if rule["nivel"] == "block":
            block_ids.add(rule_id)

    if "entrada" not in phases or "saida" not in phases:
        errors.append("devem existir regras de entrada e de saida")

    missing_blocking = BLOCKING_MIN_RULE_IDS - block_ids
    if missing_blocking:
        errors.append(f"regras bloqueantes minimas ausentes: {sorted(missing_blocking)}")

    return errors


def main() -> int:
    try:
        policy = load_policy()
    except ValueError as exc:
        print(f"ERRO: {exc}")
        return 1

    errors = validate_policy_schema(policy)
    errors.extend(validate_thematic_alignment(policy))

    if errors:
        print("ERRO: politica de guardrails invalida")
        for error in errors:
            print(f"- {error}")
        return 1

    rules = policy["rules"]
    by_level = {level: 0 for level in REQUIRED_LEVELS}
    for rule in rules:
        by_level[rule["nivel"]] += 1

    print("OK: politica de guardrails valida")
    print(f"Total de regras: {len(rules)}")
    print(
        "Niveis: "
        + ", ".join(
            f"{level}={by_level[level]}"
            for level in ("info", "warning", "block", "escalate")
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
