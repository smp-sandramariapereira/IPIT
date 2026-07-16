---
name: planejar-arquitetura
description: >
  Planejar a arquitetura tecnico-pedagogica do MVP antes da implementacao,
  garantindo escopo viavel, seguranca, privacidade e evidencias de aprendizagem.
  Use when o diagnostico e a orquestracao inicial ja foram concluidos e a equipe
  precisa definir estrutura de solucao e plano de execucao.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - equipe-estudantil
  ipit-stage: planejamento
  requires-human-review: true
  depends-on:
    - orquestrar-ipit
  required-evidence:
    - problema priorizado e delimitado
    - requisitos funcionais minimos
    - criterios de seguranca e privacidade
    - plano de testes inicial
    - plano de registro de evidencias
  produces:
    - arquitetura-mvp
    - backlog-priorizado
    - plano-de-execucao
    - matriz-de-riscos
    - criterios-de-validacao
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `planejar-arquitetura`.
- Confirmar dependencia: executar apenas apos `orquestrar-ipit`.
- Definir escopo minimo viavel do MVP com problema, usuarios e fluxo principal.
- Especificar componentes tecnicos necessarios sem excesso de complexidade.
- Registrar premissas, restricoes e alternativas consideradas.
- Definir backlog inicial com prioridades e entregas incrementais.
- Incluir criterios de seguranca e privacidade desde o desenho da solucao.
- Planejar testes minimos para validar fluxo principal e riscos criticos.
- Prever checkpoints de revisao docente e da equipe pedagogica.
- Registrar evidencias esperadas por etapa para avaliacao processual.
- Evitar dependencia de dados pessoais reais; priorizar dados ficticios ou anonimizados.
- Declarar limites do MVP e riscos nao resolvidos.

## Inputs - Entradas

- Resultado do diagnostico inicial e da orquestracao (bloqueante).
- Contexto da turma, infraestrutura e tempo disponivel (bloqueante).
- Requisitos pedagogicos e institucionais (bloqueante).
- Restricoes tecnicas e de acessibilidade (bloqueante).
- Contexto BNCC/curriculo local/PPP (nao bloqueante, registrar "a validar pela equipe pedagogica" quando faltar confirmacao).

## Outputs - Saidas

- Desenho da arquitetura do MVP com fluxo principal definido.
- Backlog priorizado por incremento.
- Plano de execucao com checkpoints de revisao humana.
- Plano de testes iniciais e criterios de aceitacao.
- Matriz de riscos tecnicos, pedagogicos e de dados.
- Evidencias minimas:
  - arquitetura-mvp;
  - backlog-priorizado;
  - plano-de-execucao;
  - criterios-de-validacao.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar planejamento ao curriculo local, PPP e avaliacao processual.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao coletar nem planejar uso de dados pessoais desnecessarios.
- Nao incluir credenciais, tokens ou segredos em exemplos de arquitetura.
- Garantir supervisao docente para decisoes pedagogicas e de risco.
- Prever acessibilidade e inclusao como requisito de arquitetura.
- Registrar limites eticos do uso de IA no MVP.

## Examples - Exemplos

- Exemplo de saida: "Arquitetura aprovada com fluxo de cadastro anonimo, backlog em 4 incrementos, 8 testes planejados e checklist de privacidade validado pela equipe docente."

## Performance Notes - Notas de desempenho

- Prioridade: viabilidade pedagogica -> seguranca/privacidade -> simplicidade tecnica -> testabilidade.
- Se faltar entrada bloqueante, interromper e solicitar complementacao objetiva.

## Troubleshooting - Solucao de problemas

- Erro bloqueante: ausencia de orquestracao previa, escopo indefinido, sem plano de testes ou sem revisao humana prevista.
- Aviso nao bloqueante: backlog incompleto, riscos sem mitigacao detalhada, mapeamento BNCC pendente.
- Em risco alto institucional ou de dados, escalar para equipe pedagogica/gestao.

## Criterios de conclusao

A skill conclui quando houver arquitetura do MVP validada para o contexto, backlog priorizado, plano de execucao com checkpoints, plano de testes iniciais, riscos principais mapeados e registro de revisao humana.

## Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: nova evidencia ou regra compativel com o fluxo atual.
- MAJOR: mudanca de dependencia, escopo ou criterio de conclusao.
