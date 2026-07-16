---
name: acompanhar-desenvolvimento
description: >
  Acompanhar a etapa de desenvolvimento do MVP com controle de execucao,
  qualidade tecnica e registro pedagogico. Use when o planejamento de
  arquitetura ja foi concluido e a equipe vai implementar, testar e integrar.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: desenvolvimento
  requires-human-review: true
  depends-on:
    - planejar-arquitetura
  required-evidence:
    - issues ativas e rastreaveis
    - historico de commits e branches
    - evidencias de testes e depuracao
    - README atualizado
  produces:
    - mvp-executavel
    - evidencias-de-testes
    - limitacoes-conhecidas
    - registro-de-uso-de-ia
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `acompanhar-desenvolvimento`.
- Confirmar dependencia: so executar se `planejar-arquitetura` estiver concluida.
- Conduzir desenvolvimento incremental, com entregas pequenas e verificaveis.
- Organizar trabalho em issues com escopo claro, responsavel e status.
- Exigir commits frequentes, descritivos e vinculados a issues.
- Usar branches para mudancas de risco, integrando por pull requests revisadas.
- Executar testes tecnicos e de fluxo a cada incremento relevante.
- Registrar depuracao: erro observado, hipotese, ajuste e resultado.
- Manter documentacao tecnica atualizada durante a implementacao.
- Registrar uso de IA: onde ajudou, limites e validacao humana.
- Proibir exposicao de credenciais, tokens e segredos no repositorio.
- Exigir dados ficticios ou anonimizados para demonstracoes e testes.
- Registrar limitacoes conhecidas sem mascarar pendencias tecnicas.
- Prever acompanhamento docente com checkpoints de progresso e risco.

## Inputs - Entradas

- Estado da arquitetura e backlog (bloqueante).
- Quadro de issues, branches e pull requests (bloqueante).
- Evidencias de testes e logs de depuracao (bloqueante).
- Evidencias de acompanhamento docente (nao bloqueante).
- Contexto BNCC/curriculo local/PPP (nao bloqueante, registrar "a validar pela equipe pedagogica" quando faltar confirmacao).

## Outputs - Saidas

- Status do desenvolvimento por incremento.
- Lista consolidada de issues, commits, branches e pull requests.
- Registro de testes executados e depuracoes realizadas.
- Registro do uso de IA com verificacao humana.
- Entregaveis minimos:
  - MVP executavel;
  - evidencias de testes;
  - limitacoes conhecidas;
  - README atualizado.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar evidencias a curriculo local, PPP e avaliacao processual.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao coletar ou publicar dados pessoais desnecessarios.
- Nao aceitar credenciais reais em codigo, issue, commit ou documentacao.
- Priorizar dados ficticios em desenvolvimento, testes e demonstracoes.
- Garantir supervisao docente em decisoes criticas e uso de IA.
- Manter acessibilidade e inclusao nos fluxos do MVP.

## Examples - Exemplos

- Exemplo de checkpoint: "Incremento 3 concluido, PR revisada, 6 testes passando, limitacao de autenticacao social registrada no README."

## Performance Notes - Notas de desempenho

- Prioridade: seguranca de dados -> fluxo funcional do MVP -> qualidade de testes -> documentacao.
- Se faltarem evidencias bloqueantes, interromper e solicitar complementacao objetiva.

## Troubleshooting - Solucao de problemas

- Erro bloqueante: ausencia de arquitetura aprovada, sem testes minimos, sem rastreabilidade de issues/commits/PRs.
- Aviso nao bloqueante: documentacao parcial, acompanhamento docente incompleto, mapeamento BNCC pendente.
- Em risco alto tecnico ou pedagogico, escalar para revisao docente e equipe pedagogica.

## Criterios de conclusao

A skill conclui quando houver MVP executavel com fluxo principal funcionando, evidencias de testes, limitacoes conhecidas documentadas, README atualizado e rastreabilidade entre issues, commits, branches e pull requests.

## Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: nova regra de acompanhamento ou evidencia adicional compativel.
- MAJOR: mudanca de dependencia, escopo ou criterio de conclusao.
