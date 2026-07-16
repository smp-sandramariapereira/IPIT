#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


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


def load_policy(path: Path = POLICY_PATH) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"guardrails/policy.yaml deve ser JSON valido (YAML-compativel): {exc}") from exc


def _extract_rule_ids_from_thematic_file(path: Path) -> set[str]:
    content = path.read_text(encoding="utf-8")
    return set(re.findall(r"^\s*-\s*(gr-[a-z0-9\-]+)\s*$", content, flags=re.MULTILINE))


def load_thematic_rule_ids() -> dict[str, set[str]]:
    thematic_rule_ids: dict[str, set[str]] = {}
    for filename in THEMATIC_FILES:
        file_path = GUARDRAILS_DIR / filename
        if not file_path.exists():
            thematic_rule_ids[filename] = set()
            continue
        thematic_rule_ids[filename] = _extract_rule_ids_from_thematic_file(file_path)
    return thematic_rule_ids


def validate_thematic_alignment(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy_rule_ids = {rule.get("id") for rule in policy.get("rules", []) if isinstance(rule, dict)}
    policy_rule_ids.discard(None)

    thematic_rule_ids = load_thematic_rule_ids()
    union_thematic_ids = set().union(*thematic_rule_ids.values()) if thematic_rule_ids else set()

    for filename in THEMATIC_FILES:
        file_path = GUARDRAILS_DIR / filename
        if not file_path.exists():
            errors.append(f"arquivo tematico ausente: guardrails/{filename}")
            continue

        content = file_path.read_text(encoding="utf-8")
        if "source_of_truth: policy.yaml" not in content:
            errors.append(f"source_of_truth ausente em guardrails/{filename}")

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

    missing_module_files = set(THEMATIC_FILES) - set(modules.keys())
    if missing_module_files:
        errors.append(f"modules sem arquivos tematicos obrigatorios: {sorted(missing_module_files)}")

    extra_module_files = set(modules.keys()) - set(THEMATIC_FILES)
    if extra_module_files:
        errors.append(f"modules com arquivos nao reconhecidos: {sorted(extra_module_files)}")

    for filename in THEMATIC_FILES:
        module_ids = modules.get(filename, [])
        if not isinstance(module_ids, list):
            errors.append(f"modules[{filename}] deve ser lista")
            continue
        module_id_set = set(module_ids)
        thematic_id_set = thematic_rule_ids.get(filename, set())
        if module_id_set != thematic_id_set:
            errors.append(
                f"divergencia entre policy.modules e guardrails/{filename}: "
                f"modules={sorted(module_id_set)} thematic={sorted(thematic_id_set)}"
            )

    return errors


def _contains_bncc_code(text: str) -> bool:
    # Padroes comuns de codigos BNCC (usado apenas para validacao defensiva de saida).
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
        flag = cond.get("flag")
        return not bool(payload.get(flag))

    if cond_type == "missing_evidence_or_next_step":
        evidence_field = cond.get("evidence_field", "evidencias")
        next_step_field = cond.get("next_step_field", "proximo_passo")
        evidencias = payload.get(evidence_field)
        proximo_passo = payload.get(next_step_field)
        return not evidencias or not str(proximo_passo).strip()

    if cond_type == "institutional_decision_without_review":
        return bool(payload.get("decisao_institucional")) and not bool(payload.get("revisao_humana_registrada"))

    if cond_type == "bncc_unverified_definitive":
        raw_text = payload.get("text", "")
        lowered = raw_text.lower()
        has_code = _contains_bncc_code(raw_text)
        has_bncc_definitive_claim = "bncc" in lowered and "definitiv" in lowered
        has_validation_phrase = "a validar pela equipe pedagogica" in lowered
        return (has_code or has_bncc_definitive_claim) and not has_validation_phrase

    if cond_type == "missing_context_keyword":
        required = [kw.lower() for kw in cond.get("required_keywords", [])]
        return any(kw not in text for kw in required)

    return False


def evaluate_payload(policy: dict[str, Any], payload: dict[str, Any], phase: str) -> list[dict[str, Any]]:
    hits = []
    for rule in policy.get("rules", []):
        if _evaluate_rule(rule, payload, phase):
            hits.append(rule)
    return hits


def validate_policy_schema(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if "metadata" not in policy:
        errors.append("metadata ausente")
    if "rules" not in policy or not isinstance(policy["rules"], list) or not policy["rules"]:
        errors.append("rules ausente ou vazio")

    levels = set(policy.get("levels", []))
    if not REQUIRED_LEVELS.issubset(levels):
        errors.append(f"levels incompleto: esperado {sorted(REQUIRED_LEVELS)}")

    phases = set()
    ids = set()
    block_ids = set()

    for idx, rule in enumerate(policy.get("rules", []), start=1):
        missing = REQUIRED_RULE_FIELDS - set(rule.keys())
        if missing:
            errors.append(f"regra #{idx} com campos ausentes: {sorted(missing)}")
            continue

        if rule["id"] in ids:
            errors.append(f"id duplicado: {rule['id']}")
        ids.add(rule["id"])

        if rule["nivel"] not in REQUIRED_LEVELS:
            errors.append(f"nivel invalido em {rule['id']}: {rule['nivel']}")

        if rule["fase"] not in {"entrada", "saida"}:
            errors.append(f"fase invalida em {rule['id']}: {rule['fase']}")
        phases.add(rule["fase"])

        if not isinstance(rule["evidencia_exigida"], list) or not rule["evidencia_exigida"]:
            errors.append(f"evidencia_exigida invalida em {rule['id']}")

        if rule["nivel"] == "block":
            block_ids.add(rule["id"])

    if "entrada" not in phases or "saida" not in phases:
        errors.append("devem existir regras de entrada e de saida")

    missing_blocking = BLOCKING_MIN_RULE_IDS - block_ids
    if missing_blocking:
        errors.append(f"regras bloqueantes minimas ausentes: {sorted(missing_blocking)}")

    return errors


def main() -> int:
    policy = load_policy()
    errors = validate_policy_schema(policy)
    errors.extend(validate_thematic_alignment(policy))

    if errors:
        print("ERRO: politica de guardrails invalida")
        for err in errors:
            print(f"- {err}")
        return 1

    rules = policy["rules"]
    by_level = {level: 0 for level in REQUIRED_LEVELS}
    for rule in rules:
        by_level[rule["nivel"]] += 1

    print("OK: politica de guardrails valida")
    print(f"Total de regras: {len(rules)}")
    print(
        "Niveis: "
        + ", ".join(f"{level}={by_level[level]}" for level in ("info", "warning", "block", "escalate"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
