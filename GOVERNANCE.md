# Governance - Agente IPIT

## Objetivo

Estabelecer regras de decisao, revisao e manutencao metodologica do projeto IPIT.

## Papeis

- Mantenedora metodologica: aprova mudancas que alteram comportamento pedagogico.
- Colaboradores: propem ajustes tecnicos e documentais.
- Revisores humanos: validam riscos de privacidade, seguranca e aderencia didatica.

## Aprovacao de mudancas metodologicas

Mudancas metodologicas exigem:

1. justificativa pedagogica;
2. impacto em BNCC/curriculo local/PPP;
3. revisao humana registrada;
4. aprovacao explicita da mantenedora metodologica.

Sem essa aprovacao, a mudanca nao deve ser integrada.

## Atualizacao de skills

- Toda skill deve seguir `references/skill-standard.md`.
- Dependencias, evidencias e criterios de conclusao devem permanecer verificaveis.
- Mudanca em risco pedagogico, dados ou seguranca exige revisao humana obrigatoria.

## Versionamento

- Usar SemVer para skills no campo `metadata.version`.
- PATCH: ajuste textual sem alterar comportamento.
- MINOR: nova capacidade compativel.
- MAJOR: quebra de contrato, escopo ou dependencia.

## Contribuicao externa

- Contribuicoes externas sao bem-vindas via Pull Request.
- Todo PR deve cumprir checklist de seguranca, privacidade e autoria.
- Nao aceitar contribuicao que exponha dados de estudantes, credenciais ou instrucoes maliciosas.

