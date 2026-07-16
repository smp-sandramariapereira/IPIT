---
name: planejar-arquitetura
description: >
  Planejar a arquitetura tecnico-pedagogica do MVP com componentes, fluxos,
  backlog, testes, riscos e checkpoints de revisao humana. Use when o escopo do
  MVP ja foi definido e a equipe precisa organizar a implementacao de forma
  segura, simples e verificavel.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.1.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
    - apoio-tecnico
  ipit-stage: arquitetura
  requires-human-review: true
  depends-on:
    - definir-mvp
  required-evidence:
    - objetivo-do-mvp
    - escopo-mvp
    - criterios-de-aceite
    - plano-de-validacao
    - stack-selecionada
    - mapa-de-riscos-tecnicos
  produces:
    - arquitetura-mvp
    - diagrama-de-componentes
    - backlog-priorizado
    - plano-de-execucao
    - plano-de-testes
    - matriz-de-riscos
    - checkpoints-de-revisao
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

# Skill: planejar-arquitetura

## Purpose - Finalidade

Transformar o escopo validado do MVP em um plano tecnico-pedagogico executavel,
com componentes claros, dependencias controladas, entregas incrementais, testes,
riscos e momentos obrigatorios de revisao humana.

## Use When - Quando usar

Use esta skill quando:

- o MVP ja tiver objetivo, escopo e criterios de aceite definidos;
- a stack tecnologica ja tiver sido selecionada;
- a equipe precisar dividir a solucao em componentes e incrementos;
- for necessario planejar testes, seguranca, privacidade e acessibilidade;
- houver necessidade de organizar responsabilidades e checkpoints.

Trigger phrases:

- "vamos planejar a arquitetura";
- "como dividir o MVP em componentes?";
- "precisamos montar o backlog tecnico";
- "como organizar a implementacao?";
- "quais testes entram antes do desenvolvimento?".

## Instructions - Instrucoes

1. Declarar a skill utilizada: `planejar-arquitetura`.
2. Confirmar que `definir-mvp` foi concluida e que as evidencias obrigatorias existem.
3. Reafirmar objetivo, fluxo principal e limites do MVP sem ampliar o escopo.
4. Identificar componentes, integracoes, dados, atores e dependencias tecnicas.
5. Elaborar um diagrama textual ou visual simples da arquitetura.
6. Dividir o trabalho em incrementos pequenos, testaveis e pedagogicamente acompanhaveis.
7. Criar backlog priorizado com criterios de aceite e evidencias esperadas.
8. Planejar testes do fluxo principal, acessibilidade, seguranca e tratamento de dados.
9. Mapear riscos tecnicos, pedagogicos, institucionais e de privacidade.
10. Definir checkpoints de revisao docente, pedagogica e tecnica.
11. Registrar premissas, restricoes, decisoes adiadas e plano de mitigacao.
12. Encerrar com proximo passo acionavel para `acompanhar-desenvolvimento`.

## Inputs - Entradas

### Obrigatorias

- objetivo e escopo do MVP;
- criterios de aceite;
- plano de validacao;
- stack selecionada e justificativa;
- mapa de riscos tecnicos;
- contexto de infraestrutura, tempo e equipe.

### Opcionais

- prototipo atualizado;
- regras institucionais de hospedagem e acesso;
- disponibilidade de apoio tecnico;
- requisitos de integracao;
- contexto BNCC, curriculo local e PPP.

A ausencia de escopo, criterios de aceite ou stack selecionada e bloqueante.

## Outputs - Saidas

A skill deve produzir:

- arquitetura do MVP;
- diagrama de componentes e fluxo de dados;
- backlog priorizado por incremento;
- plano de execucao com responsabilidades;
- plano de testes;
- matriz de riscos e mitigacoes;
- checkpoints de revisao humana;
- proximo passo para desenvolvimento.

Formato minimo recomendado:

```yaml
arquitetura_mvp:
  componentes: []
  integracoes: []
  dados: []
backlog:
  - incremento: 1
    entrega: ""
    criterio_de_aceite: ""
    evidencia: ""
plano_de_testes: []
riscos: []
checkpoints_de_revisao: []
proximo_passo: acompanhar-desenvolvimento
```

## Dependencies - Dependencias

Esta skill depende de:

1. `skills/definir-mvp/SKILL.md`;
2. evidencias produzidas por `selecionar-tecnologia`;
3. guardrails definidos em `guardrails/policy.yaml`.

Nao deve retroceder silenciosamente para redefinir o MVP. Mudancas de escopo devem
ser encaminhadas novamente para `definir-mvp`.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar checkpoints e evidencias de aprendizagem ao curriculo local e ao PPP quando aplicavel.
- Decisoes curriculares exigem validacao da equipe pedagogica.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao incluir dados pessoais reais, credenciais, tokens ou segredos na arquitetura.
- Aplicar minimizacao de dados e preferir dados ficticios ou anonimizados.
- Prever controle de acesso apenas quando houver necessidade real.
- Nao automatizar decisoes pedagogicas, avaliativas ou institucionais.
- Manter acessibilidade e inclusao como requisitos de arquitetura.
- Registrar limites e riscos do uso de IA.
- Nao executar codigo ou provisionar infraestrutura nesta skill.
- Preservar autoria estudantil e autoria metodologica.

## Human Review - Revisao humana

Revisao obrigatoria por:

- professor, para coerencia pedagogica e avaliacao processual;
- equipe pedagogica, para curriculo, PPP e impacto institucional;
- apoio tecnico, quando houver integracoes, autenticacao, hospedagem ou dados;
- gestao, quando houver custo, publicacao externa ou tratamento de dados de estudantes.

A revisao deve registrar responsavel, data, criterio e pendencias.

## Completion Criteria - Criterios de conclusao

A skill esta concluida quando:

- os componentes e fluxos estiverem documentados;
- o backlog estiver priorizado em incrementos testaveis;
- cada incremento tiver criterio de aceite e evidencia esperada;
- o plano de testes cobrir fluxo principal e riscos criticos;
- riscos e mitigacoes estiverem registrados;
- checkpoints de revisao humana estiverem definidos;
- o proximo passo para desenvolvimento estiver claro.

## Examples - Exemplos

### Caso adequado

A equipe possui MVP de formulario anonimo, stack simples e criterios de aceite. A
skill produz arquitetura com frontend, armazenamento sem identificacao pessoal,
backlog em tres incrementos, testes de acessibilidade e checkpoint docente.

### Caso ambiguo

A equipe ainda discute quais funcionalidades pertencem ao MVP. Interromper a
arquitetura e retornar para `definir-mvp`.

### Caso bloqueante

A proposta exige armazenar nomes e telefones de estudantes sem justificativa ou
aprovacao. Bloquear o desenho, aplicar minimizacao de dados e escalar para revisao
institucional.

## Performance Notes - Notas de desempenho

- Priorizar simplicidade, testabilidade e manutencao.
- Evitar diagramas excessivamente detalhados para um MVP escolar.
- Reutilizar decisoes ja registradas e nao reabrir escolhas sem evidencia nova.
- Dividir entregas para permitir acompanhamento e feedback frequente.
- Fazer no maximo tres perguntas por rodada quando faltar contexto.

## Troubleshooting - Solucao de problemas

### Escopo ainda instavel

Retornar para `definir-mvp` antes de prosseguir.

### Stack incompatível com a infraestrutura

Retornar para `selecionar-tecnologia` e registrar a restricao descoberta.

### Arquitetura complexa demais

Remover componentes sem relacao direta com o fluxo principal e os criterios de aceite.

### Ausencia de plano de testes

Nao concluir a skill. Definir testes minimos antes do desenvolvimento.

### Risco alto de dados ou seguranca

Bloquear a continuidade e escalar para apoio tecnico, equipe pedagogica e gestao.

## Update Policy - Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: novo artefato ou criterio compativel com o fluxo atual.
- MAJOR: alteracao de dependencia, contrato de saida ou criterio de conclusao.

## Authorship - Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT - Ideathon Pedagogico de Inovacao Tecnologica.
