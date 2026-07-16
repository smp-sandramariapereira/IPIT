#!/usr/bin/env bash
# Valida todos os arquivos skills/*/SKILL.md segundo o padrão oficial do IPIT.
# Uso: bash scripts/validate-skills.sh

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT_DIR/skills"
ERRORS=0
WARNINGS=0
CHECKED=0

red()    { printf '\033[0;31m%s\033[0m\n' "$1"; }
green()  { printf '\033[0;32m%s\033[0m\n' "$1"; }
yellow() { printf '\033[0;33m%s\033[0m\n' "$1"; }

fail() {
  red "  FAIL: $1"
  ERRORS=$((ERRORS + 1))
}

warn() {
  yellow "  WARN: $1"
  WARNINGS=$((WARNINGS + 1))
}

extract_frontmatter_value() {
  local frontmatter="$1"
  local key="$2"
  printf '%s\n' "$frontmatter" | sed -n "s/^${key}:[[:space:]]*//p" | head -n 1
}

extract_description() {
  printf '%s\n' "$1" | awk '
    /^description:/ {
      found=1
      value=$0
      sub(/^description:[[:space:]]*/, "", value)
      if (value == "" || value ~ /^>[+-]?$/ || value ~ /^\|[+-]?$/) next
      print value
      exit
    }
    found && /^[^[:space:]]/ { exit }
    found {
      sub(/^[[:space:]]+/, "", $0)
      print
    }
  ' | paste -sd' ' -
}

body_without_code_fences() {
  local file="$1"
  local start_line="$2"
  awk -v start="$start_line" '
    NR < start { next }
    /^```/ { in_code = !in_code; next }
    !in_code { print }
  ' "$file"
}

extract_list_values() {
  local frontmatter="$1"
  local key="$2"
  printf '%s\n' "$frontmatter" | awk -v key="$key" '
    $0 ~ "^[[:space:]]+" key ":[[:space:]]*\\[\\][[:space:]]*$" { exit }
    $0 ~ "^[[:space:]]+" key ":[[:space:]]*$" { found=1; next }
    found && /^[[:space:]]+-[[:space:]]+/ {
      value=$0
      sub(/^[[:space:]]+-[[:space:]]+/, "", value)
      print value
      next
    }
    found { exit }
  '
}

has_section() {
  local body="$1"
  local heading="$2"
  printf '%s\n' "$body" | grep -qE "^##[[:space:]]+${heading}([[:space:]]|$)"
}

if [[ ! -d "$SKILLS_DIR" ]]; then
  red "ERRO: diretório skills/ não encontrado"
  exit 1
fi

shopt -s nullglob
skill_dirs=("$SKILLS_DIR"/*/)

if [[ ${#skill_dirs[@]} -eq 0 ]]; then
  red "ERRO: nenhuma pasta de skill encontrada"
  exit 1
fi

for skill_dir in "${skill_dirs[@]}"; do
  skill_name="$(basename "$skill_dir")"
  skill_file="$skill_dir/SKILL.md"

  # catalog.yaml é arquivo, não diretório; diretórios auxiliares sem SKILL.md falham.
  if [[ ! -f "$skill_file" ]]; then
    fail "$skill_name: SKILL.md não encontrado"
    continue
  fi

  CHECKED=$((CHECKED + 1))
  echo "Checking $skill_name..."

  if [[ ! "$skill_name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    fail "$skill_name: nome da pasta deve usar kebab-case"
  fi

  if [[ -f "$skill_dir/README.md" ]]; then
    fail "$skill_name: README.md não é permitido dentro da pasta da skill"
  fi

  if [[ "$(sed -n '1p' "$skill_file")" != "---" ]]; then
    fail "$skill_name: frontmatter deve começar na linha 1 com ---"
    continue
  fi

  frontmatter_end="$(awk 'NR > 1 && /^---$/ { print NR; exit }' "$skill_file")"
  if [[ -z "$frontmatter_end" ]]; then
    fail "$skill_name: delimitador final do frontmatter não encontrado"
    continue
  fi

  frontmatter="$(sed -n "2,$((frontmatter_end - 1))p" "$skill_file")"
  body_start=$((frontmatter_end + 1))
  body="$(body_without_code_fences "$skill_file" "$body_start")"

  fm_name="$(extract_frontmatter_value "$frontmatter" "name")"
  if [[ -z "$fm_name" ]]; then
    fail "$skill_name: campo name ausente"
  elif [[ "$fm_name" != "$skill_name" ]]; then
    fail "$skill_name: name '$fm_name' difere do nome do diretório"
  fi

  desc="$(extract_description "$frontmatter")"
  if [[ -z "$desc" ]]; then
    fail "$skill_name: description ausente ou vazia"
  else
    if [[ ${#desc} -gt 1024 ]]; then
      fail "$skill_name: description excede 1024 caracteres"
    fi
    if printf '%s\n' "$desc" | grep -qE '<[A-Za-z/][^>]*>'; then
      fail "$skill_name: description contém marcação XML/HTML"
    fi
    if ! printf '%s\n' "$desc" | grep -iqE 'use when|trigger phrases'; then
      warn "$skill_name: description sem 'Use when' ou 'Trigger phrases'"
    fi
  fi

  if ! printf '%s\n' "$frontmatter" | grep -q '^metadata:$'; then
    fail "$skill_name: bloco metadata ausente"
  fi

  author="$(printf '%s\n' "$frontmatter" | sed -n 's/^  author:[[:space:]]*//p' | head -n 1)"
  if [[ -z "$author" ]]; then
    fail "$skill_name: metadata.author ausente"
  elif [[ "$author" != "Sandra Maria Pereira" ]]; then
    fail "$skill_name: metadata.author deve ser Sandra Maria Pereira"
  fi

  methodology="$(printf '%s\n' "$frontmatter" | sed -n 's/^  methodology:[[:space:]]*//p' | head -n 1)"
  if [[ -z "$methodology" ]]; then
    fail "$skill_name: metadata.methodology ausente"
  fi

  version="$(printf '%s\n' "$frontmatter" | sed -n 's/^  version:[[:space:]]*//p' | head -n 1)"
  if [[ -z "$version" ]]; then
    fail "$skill_name: metadata.version ausente"
  elif [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    fail "$skill_name: metadata.version '$version' não usa SemVer"
  fi

  for field in mcp-server personas ipit-stage requires-human-review depends-on required-evidence produces; do
    if ! printf '%s\n' "$frontmatter" | grep -qE "^  ${field}:"; then
      fail "$skill_name: metadata.${field} ausente"
    fi
  done

  review_value="$(printf '%s\n' "$frontmatter" | sed -n 's/^  requires-human-review:[[:space:]]*//p' | head -n 1)"
  if [[ -n "$review_value" && "$review_value" != "true" && "$review_value" != "false" ]]; then
    fail "$skill_name: metadata.requires-human-review deve ser true ou false"
  fi

  if ! printf '%s\n' "$frontmatter" | grep -q '^license:'; then
    fail "$skill_name: license ausente"
  fi
  if ! printf '%s\n' "$frontmatter" | grep -q '^compatibility:'; then
    fail "$skill_name: compatibility ausente"
  fi

  # Dependências declaradas devem apontar para skills existentes.
  while IFS= read -r dependency; do
    [[ -z "$dependency" ]] && continue
    if [[ ! -f "$SKILLS_DIR/$dependency/SKILL.md" ]]; then
      fail "$skill_name: dependência inexistente '$dependency'"
    fi
    if [[ "$dependency" == "$skill_name" ]]; then
      fail "$skill_name: dependência circular direta para si mesma"
    fi
  done < <(extract_list_values "$frontmatter" "depends-on")

  if ! printf '%s\n' "$body" | grep -q '^# '; then
    warn "$skill_name: H1 ausente"
  fi

  required_sections=(
    "Instructions"
    "Inputs"
    "Outputs"
    "BNCC Alignment"
    "Safety and Pedagogy"
    "Examples"
    "Performance Notes"
    "Troubleshooting"
  )

  for section in "${required_sections[@]}"; do
    if ! has_section "$body" "$section"; then
      warn "$skill_name: seção '$section' ausente"
    fi
  done

  if ! printf '%s\n' "$body" | grep -qiE '^##[[:space:]]+(Completion Criteria|Critérios de conclusão|Criterios de conclusao)'; then
    warn "$skill_name: critérios de conclusão ausentes"
  fi

  if ! printf '%s\n' "$body" | grep -qi 'Sandra Maria Pereira'; then
    warn "$skill_name: autoria metodológica ausente no corpo"
  fi

  if ! printf '%s\n' "$body" | grep -qiE 'revis[aã]o humana|equipe pedag[oó]gica|valida[cç][aã]o humana'; then
    warn "$skill_name: revisão humana não está explícita no corpo"
  fi

  if ! printf '%s\n' "$body" | grep -qiE 'n[aã]o inventar c[oó]digos? (da )?BNCC|a validar pela equipe pedag[oó]gica'; then
    warn "$skill_name: regra defensiva de BNCC não encontrada"
  fi

  # Falha apenas quando o texto autoriza explicitamente inventar códigos BNCC.
  # Formulações defensivas como "Não inventar códigos BNCC" não podem gerar falso positivo.
  if printf '%s\n' "$body" | grep -qiE '(pode(m)?|deve(m)?|permitid[oa]s?|autorizad[oa]s?)[^.!?]{0,80}invent(ar|e)[^.!?]{0,30}c[oó]digos? (da )?BNCC'; then
    fail "$skill_name: conteúdo aparenta permitir invenção de código BNCC"
  fi

  if ! printf '%s\n' "$body" | grep -qiE 'privacidade|dados pessoais|credenciais|seguran[cç]a'; then
    warn "$skill_name: segurança ou privacidade não estão explícitas"
  fi

  body_words="$(sed -n "${body_start},\$p" "$skill_file" | wc -w | tr -d ' ')"
  if [[ "$body_words" -gt 5000 ]]; then
    warn "$skill_name: corpo com $body_words palavras; recomendado até 5000"
  fi

done

echo ""
echo "================================"
echo "Checked $CHECKED skills"
echo "  Errors:   $ERRORS"
echo "  Warnings: $WARNINGS"
echo "================================"

if [[ $ERRORS -gt 0 ]]; then
  red "Validation failed with $ERRORS error(s)"
  exit 1
fi

green "All skills passed validation ($WARNINGS warning(s))"
exit 0
