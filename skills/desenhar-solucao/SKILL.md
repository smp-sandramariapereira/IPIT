---
name: desenhar-solucao
description: >
  Desenhar a solucao escolhida com fluxo, funcionalidades e experiencia do
  usuario em nivel de prototipo. Use when a ideacao ja selecionou uma proposta
  e a equipe precisa detalhar como a solucao funcionara.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: desenho
  requires-human-review: true
  depends-on:
    - conduzir-ideacao
  required-evidence:
    - fluxo principal desenhado
    - funcionalidades essenciais definidas
    - criterios de usabilidade registrados
  produces:
    - fluxo-da-solucao
    - especificacao-funcional
    - prototipo-inicial
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `desenhar-solucao`.
- Confirmar dependencia: executar apenas apos `conduzir-ideacao`.
- Detalhar fluxo principal e funcionalidades essenciais.
- Priorizar clareza de uso, acessibilidade e viabilidade pedagógica.
- Registrar limites da solucao e suposicoes abertas.
- Encerrar com prototipo inicial e criterios de validacao.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao incluir dados pessoais reais em prototipos.
- Evitar propostas que exijam credenciais reais em atividades educacionais.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".

## Criterios de conclusao

A skill conclui quando fluxo, funcionalidades e prototipo inicial estiverem documentados com criterios de validacao.
