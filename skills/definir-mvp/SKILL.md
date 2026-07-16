---
name: definir-mvp
description: >
  Definir o escopo minimo viavel do produto para implementacao incremental,
  com criterios de aceite e evidencias de aprendizagem. Use when a tecnologia
  ja foi selecionada e a equipe precisa recortar o MVP.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: mvp
  requires-human-review: true
  depends-on:
    - selecionar-tecnologia
  required-evidence:
    - funcionalidades essenciais priorizadas
    - criterio de aceite por funcionalidade
    - plano de validacao do MVP
  produces:
    - escopo-mvp
    - criterios-de-aceite
    - plano-de-validacao
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `definir-mvp`.
- Confirmar dependencia: executar apenas apos `selecionar-tecnologia`.
- Recortar funcionalidades minimas para gerar valor no contexto escolar.
- Definir criterios de aceite verificaveis por funcionalidade.
- Planejar validacao com evidencias observaveis.
- Registrar o que fica fora do MVP e por que.
- Encerrar com escopo fechado e proximo passo acionavel para arquitetura.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".

## Criterios de conclusao

A skill conclui quando o escopo do MVP estiver fechado, com criterios de aceite e plano de validacao documentados.
