---
name: definir-mvp
description: >
  Define o escopo minimo viavel do produto, com criterios de aceite,
  limites explicitos e plano de validacao. Use when a stack ja foi selecionada
  e a equipe precisa transformar a solucao em um incremento implementavel.
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
  ipit-stage: mvp
  requires-human-review: true
  depends-on:
    - selecionar-tecnologia
  required-evidence:
    - especificacao-funcional
    - stack-selecionada
    - justificativa-tecnica
    - mapa-de-riscos-tecnicos
  produces:
    - objetivo-do-mvp
    - escopo-mvp
    - itens-fora-do-escopo
    - criterios-de-aceite
    - plano-de-validacao
    - evidencias-de-aprendizagem-previstas
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

# Skill: definir-mvp

## Purpose - Finalidade

Transformar a solucao desenhada e a stack selecionada em um escopo minimo,
implementavel e verificavel, preservando valor pedagogico, autoria estudantil e
viabilidade no contexto escolar.

## Use When - Quando usar

Use esta skill quando:

- a solucao e a stack ja estiverem definidas;
- a equipe precisar reduzir o escopo para caber no tempo disponivel;
- houver excesso de funcionalidades;
- for necessario criar criterios objetivos de aceite.

Trigger phrases:

- "precisamos definir o MVP";
- "o projeto esta grande demais";
- "o que entra na primeira versao?";
- "como saber se o MVP esta pronto?".

## Instructions - Instrucoes

1. Declare a skill utilizada: `definir-mvp`.
2. Confirme a dependencia `selecionar-tecnologia` e as evidencias requeridas.
3. Registre o problema prioritario e o valor minimo que o MVP deve demonstrar.
4. Identifique o fluxo principal que precisa funcionar de ponta a ponta.
5. Classifique funcionalidades em obrigatorias, adiaveis e fora do escopo.
6. Mantenha apenas funcionalidades essenciais para validar a proposta.
7. Defina criterios de aceite observaveis para cada funcionalidade obrigatoria.
8. Defina evidencias de aprendizagem e de funcionamento tecnico.
9. Planeje validacao com dados ficticios, anonimizados ou autorizados.
10. Registre riscos, dependencias e condicoes que podem impedir a entrega.
11. Encerre com escopo fechado e encaminhamento para `planejar-arquitetura`.

## Inputs - Entradas

### Obrigatorias

- especificacao funcional;
- stack selecionada e justificativa tecnica;
- mapa de riscos tecnicos;
- prazo e recursos disponiveis;
- problema prioritario e publico beneficiado.

### Opcionais

- prototipo inicial;
- criterios institucionais;
- infraestrutura disponivel;
- rubrica de avaliacao;
- restricoes de acessibilidade.

A ausencia de prazo, problema prioritario ou especificacao funcional e bloqueante.

## Outputs - Saidas

A skill deve produzir:

```yaml
objetivo_do_mvp: "Demonstrar o fluxo principal com valor pedagogico observavel"
fluxo_principal:
  inicio: "entrada do usuario"
  fim: "resultado verificavel"
funcionalidades_obrigatorias: []
funcionalidades_adiaveis: []
itens_fora_do_escopo: []
criterios_de_aceite: []
plano_de_validacao:
  participantes: []
  evidencias: []
  dados: "ficticios ou anonimizados"
evidencias_de_aprendizagem: []
riscos_e_dependencias: []
proximo_passo: "planejar-arquitetura"
```

## Dependencies - Dependencias

Esta skill depende de `selecionar-tecnologia`.

Nao deve concluir quando a stack estiver sem justificativa ou quando o desenho da
solucao ainda estiver indefinido.

A proxima skill recomendada e `planejar-arquitetura`.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Registrar `a validar pela equipe pedagogica` quando nao houver confirmacao documental.
- Relacionar evidencias de aprendizagem ao curriculo local e ao PPP quando aplicavel.
- Nao usar a BNCC para justificar funcionalidades sem valor pedagogico observavel.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao transformar o MVP em trabalho pronto para entrega pelo estudante.
- Preservar decisoes, justificativas e autoria da equipe estudantil.
- Nao incluir dados pessoais reais, credenciais ou segredos em testes.
- Nao exigir publicacao de imagens de estudantes sem autorizacao formal.
- Nao prometer automacao institucional sem aprovacao humana.
- Priorizar acessibilidade no fluxo principal, e nao como item opcional futuro.
- Declarar o uso de IA e exigir revisao humana dos artefatos produzidos.
- Aplicar `guardrails/policy.yaml` na entrada e na saida.

## Human Review - Revisao humana

A revisao e obrigatoria por:

- professor, para validar valor pedagogico, escopo e evidencias de aprendizagem;
- equipe pedagogica, quando houver impacto curricular ou avaliativo;
- apoio tecnico, para validar viabilidade, seguranca e dependencias;
- gestao, quando houver publicacao, contas institucionais ou uso de dados.

## Completion Criteria - Criterios de conclusao

A skill esta concluida quando:

- o objetivo minimo do MVP estiver claro;
- o fluxo principal estiver delimitado;
- funcionalidades obrigatorias e itens fora do escopo estiverem registrados;
- cada funcionalidade obrigatoria tiver criterio de aceite verificavel;
- houver plano de validacao com evidencias observaveis;
- riscos e dependencias estiverem documentados;
- houver revisao humana indicada;
- o proximo passo for `planejar-arquitetura`.

## Examples - Exemplos

### Caso adequado

Para uma solucao de comunicacao escolar, o MVP inclui criar um aviso, visualizar o
aviso e confirmar leitura usando dados ficticios. Relatorios avancados e integracoes
externas ficam fora do escopo.

### Escopo excessivo

Quando a equipe incluir aplicativo, painel administrativo, IA generativa, blockchain
e integracao com varios sistemas, reduzir ao fluxo que comprova a proposta de valor.

### Caso bloqueante

Se o teste exigir nomes, telefones ou imagens reais de estudantes sem autorizacao,
interromper, substituir por dados ficticios e escalar para revisao institucional.

## Performance Notes - Notas de desempenho

- Priorize um fluxo completo em vez de muitas funcionalidades incompletas.
- Use criterios de aceite binarios ou diretamente observaveis.
- Evite transformar desejos futuros em requisitos do MVP.
- Quando o prazo for curto, reduza escopo antes de reduzir seguranca ou acessibilidade.
- Apresente primeiro o objetivo, depois o escopo e por fim os criterios de aceite.

## Troubleshooting - Solucao de problemas

### Tudo parece essencial

Volte ao problema prioritario e mantenha apenas o que comprova valor para o publico.

### Criterios de aceite vagos

Substitua termos como "bom", "facil" ou "rapido" por comportamentos observaveis.

### Prazo insuficiente

Reduza funcionalidades e preserve fluxo principal, seguranca e evidencias.

### Stack inviavel

Retorne para `selecionar-tecnologia` antes de fechar o MVP.

### Falta de validacao pedagogica

Marque a saida como incompleta e escale para professor ou equipe pedagogica.

## Update Policy - Politica de atualizacao

- PATCH: clareza textual ou correcao sem mudanca de comportamento.
- MINOR: novo criterio, evidencia ou formato de validacao compativel.
- MAJOR: mudanca da dependencia, do contrato de saida ou da finalidade da skill.

## Authorship - Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT - Ideathon Pedagogico de Inovacao Tecnologica.
