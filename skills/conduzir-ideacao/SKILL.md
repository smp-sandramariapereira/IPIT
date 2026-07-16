---
name: conduzir-ideacao
description: >
  Conduzir ideacao colaborativa com foco em alternativas viaveis, criterios de
  escolha e justificativas baseadas na descoberta. Use when a descoberta ja
  foi concluida e a equipe precisa gerar e priorizar solucoes.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: ideacao
  requires-human-review: true
  depends-on:
    - conduzir-descoberta
  required-evidence:
    - alternativas geradas
    - criterios de priorizacao
    - justificativas de escolha
  produces:
    - lista-de-alternativas
    - matriz-de-priorizacao
    - proposta-selecionada
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `conduzir-ideacao`.
- Confirmar dependencia: executar apenas apos `conduzir-descoberta`.
- Gerar alternativas sem pular para implementacao imediata.
- Definir criterios de priorizacao alinhados ao contexto escolar.
- Escolher proposta com justificativa e evidencias da descoberta.
- Registrar riscos pedagogicos, tecnicos e de dados.
- Encerrar com proposta selecionada e proximo passo acionavel.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".

## Criterios de conclusao

A skill conclui quando houver alternativas mapeadas, criterios aplicados, proposta priorizada e justificativa documentada.
