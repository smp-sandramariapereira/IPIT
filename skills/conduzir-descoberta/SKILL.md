---
name: conduzir-descoberta
description: >
  Conduzir a etapa de descoberta do IPIT para delimitar problema real,
  contexto, publico afetado e evidencias iniciais. Use when a jornada ja foi
  orquestrada e a equipe precisa investigar antes de idear solucoes.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: descoberta
  requires-human-review: true
  depends-on:
    - orquestrar-ipit
  required-evidence:
    - problema delimitado
    - contexto investigado
    - publico afetado identificado
    - evidencias iniciais registradas
  produces:
    - definicao-do-problema
    - mapa-de-contexto
    - hipoteses-iniciais
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `conduzir-descoberta`.
- Confirmar dependencia: executar apenas apos `orquestrar-ipit`.
- Definir problema real com recorte claro e verificavel.
- Levantar contexto com fontes observaveis e sem inventar evidencias.
- Identificar publico afetado e impactos esperados.
- Formular hipoteses iniciais para orientar ideacao.
- Registrar restricoes de tempo, infraestrutura e acessibilidade.
- Tratar dados de estudantes com minimizacao e anonimizaao.
- Encerrar com evidencias da descoberta e proximo passo acionavel.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar descobertas ao curriculo local e PPP.

## Criterios de conclusao

A skill conclui quando o problema estiver delimitado, o contexto investigado, o publico afetado identificado, hipoteses iniciais formuladas e evidencias registradas.
