---
name: selecionar-tecnologia
description: >
  Selecionar tecnologias adequadas ao contexto escolar e ao escopo da solucao,
  equilibrando simplicidade, manutencao e seguranca. Use when o desenho da
  solucao ja foi definido e a equipe precisa decidir stack e ferramentas.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - apoio-tecnico
    - equipe-estudantil
  ipit-stage: tecnologia
  requires-human-review: true
  depends-on:
    - desenhar-solucao
  required-evidence:
    - criterios de selecao tecnica
    - comparacao de opcoes
    - justificativa da stack
  produces:
    - stack-selecionada
    - justificativa-tecnica
    - riscos-tecnicos
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `selecionar-tecnologia`.
- Confirmar dependencia: executar apenas apos `desenhar-solucao`.
- Comparar opcoes tecnicas com base em contexto real da escola.
- Priorizar simplicidade, seguranca e manutencao.
- Evitar complexidade sem requisito pedagogico claro.
- Registrar riscos tecnicos e plano de mitigacao.
- Encerrar com stack selecionada e justificativa objetiva.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao solicitar, armazenar ou compartilhar credenciais.
- Priorizar ambientes seguros e dados anonimizados.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".

## Criterios de conclusao

A skill conclui quando a stack estiver selecionada com justificativa, riscos mapeados e aderencia ao contexto institucional.
