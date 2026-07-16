---
name: preparar-pitch
description: >
  Preparar o pitch final do projeto IPIT com narrativa objetiva, demonstracao
  tecnica honesta e evidencias de aprendizagem. Use when o desenvolvimento
  do MVP ja foi acompanhado e a equipe vai apresentar resultados.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: finalizacao
  requires-human-review: true
  depends-on:
    - acompanhar-desenvolvimento
  required-evidence:
    - roteiro de apresentacao
    - demonstracao funcional ou tecnicamente honesta
    - README final atualizado
    - retrospectiva do processo
  produces:
    - roteiro
    - apresentacao
    - demonstracao
    - readme-final
    - retrospectiva
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `preparar-pitch`.
- Confirmar dependencia: executar apenas apos `acompanhar-desenvolvimento`.
- Estruturar o pitch com problema, evidencias, publico e proposta de valor.
- Preparar demonstracao alinhada ao fluxo principal do MVP.
- Apresentar arquitetura e tecnologias com linguagem adequada ao publico.
- Mostrar resultados alcancados e limitacoes conhecidas.
- Declarar uso de IA, com validacao humana e limites de confianca.
- Fechar com proximos passos realistas e priorizados.
- Garantir tempo total entre 3 e 5 minutos.
- Incluir recursos de acessibilidade da apresentacao.
- Preparar respostas para perguntas provaveis da banca.

## Inputs - Entradas

- Evidencias do desenvolvimento e testes (bloqueante).
- Estado atual do MVP e limitacoes (bloqueante).
- Publico alvo do pitch (bloqueante).
- Requisitos de banca e criterios institucionais (nao bloqueante).
- Contexto BNCC/curriculo local/PPP (nao bloqueante, registrar "a validar pela equipe pedagogica" quando faltar confirmacao).

## Outputs - Saidas

- Roteiro objetivo para pitch de 3 a 5 minutos.
- Apresentacao com acessibilidade minima planejada.
- Plano de demonstracao do MVP.
- README final atualizado.
- Retrospectiva com aprendizados, limites e continuidade.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar evidencias da apresentacao ao curriculo local, PPP e avaliacao processual.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao expor dados pessoais, credenciais ou segredos na apresentacao.
- Usar dados ficticios ou anonimizados na demonstracao.
- Evitar promessas tecnicas sem evidencia.
- Manter linguagem inclusiva, acessivel e pedagogicamente responsavel.
- Garantir supervisao docente antes da apresentacao final.

## Examples - Exemplos

- Exemplo de fechamento: "Entregamos um MVP funcional para o fluxo principal, com 12 testes executados, duas limitacoes conhecidas e plano de continuidade em tres frentes."

## Performance Notes - Notas de desempenho

- Prioridade: clareza do problema -> prova de valor -> demonstracao -> resultados e limites -> proximos passos.
- Se o tempo ultrapassar 5 minutos, reduzir detalhes secundarios e preservar evidencias centrais.

## Troubleshooting - Solucao de problemas

- Erro bloqueante: ausencia de demonstracao, falta de evidencia de resultados, dependencia nao cumprida.
- Aviso nao bloqueante: roteiro longo, acessibilidade parcial, respostas de banca pouco objetivas.
- Em risco pedagogico ou etico, pausar e revisar com equipe docente.

## Criterios de conclusao

A skill conclui quando houver roteiro, apresentacao e demonstracao prontos, com problema/evidencias/publico/proposta de valor claros, arquitetura e tecnologias explicadas, resultados e limitacoes documentados, uso de IA registrado, tempo entre 3 e 5 minutos, acessibilidade prevista, perguntas de banca preparadas, README final atualizado e retrospectiva entregue.

## Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: novo requisito de apresentacao compativel com a estrutura atual.
- MAJOR: alteracao de dependencia, formato do pitch ou criterio de conclusao.
