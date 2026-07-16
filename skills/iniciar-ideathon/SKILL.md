---
name: iniciar-ideathon
description: >
  Conduzir a abertura operacional do Ideathon Pedagogico depois que a persona e o
  percurso metodologico foram definidos, estabelecendo acordo de trabalho, desafio
  inicial, papeis, limites e primeiro passo. Use when a jornada ja foi orquestrada
  e a equipe precisa iniciar a execucao sem antecipar a solucao.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.1.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
    - gestao
    - apoio-tecnico
  ipit-stage: inicio
  requires-human-review: true
  depends-on:
    - orquestrar-ipit
  required-evidence:
    - classificacao-de-persona
    - percurso-orquestrado
    - checkpoints-de-validacao
    - entregaveis-por-etapa
  produces:
    - acordo-de-trabalho
    - desafio-inicial
    - papeis-e-responsabilidades
    - restricoes-confirmadas
    - primeiro-passo-acionavel
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

# Iniciar Ideathon

## Instructions - Instrucoes

1. Declarar a skill utilizada: `iniciar-ideathon`.
2. Confirmar que `orquestrar-ipit` foi concluida e que existe um percurso aprovado para iniciar.
3. Apresentar o objetivo do IPIT e o desafio inicial sem sugerir uma solucao pronta.
4. Confirmar papeis, responsabilidades, autonomia e instancias de validacao.
5. Estabelecer acordos de colaboracao, autoria, uso de IA, comunicacao e registro de evidencias.
6. Confirmar tempo, infraestrutura, acessibilidade e restricoes institucionais relevantes.
7. Fazer no maximo tres perguntas quando uma lacuna alterar o inicio da jornada.
8. Definir o primeiro passo da descoberta e encaminhar para `conduzir-descoberta`.
9. Registrar evidencias e revisao humana aplicavel antes de encerrar.

## Inputs - Entradas

### Obrigatorias

- Classificacao de persona e papel ativo.
- Percurso orquestrado e cadeia de skills.
- Checkpoints de validacao pedagogica, tecnica e institucional.
- Entregaveis esperados por etapa.
- Contexto da turma, tempo e infraestrutura disponivel.

### Opcionais

- Curriculo local, PPP e referencias BNCC confirmadas.
- Regras institucionais de comunicacao, imagem e publicacao.
- Composicao preliminar das equipes.

Quando houver referencia curricular sem codigo confirmado, registrar exatamente: "a validar pela equipe pedagogica".

## Outputs - Saidas

- Acordo de trabalho da jornada.
- Desafio inicial formulado de modo investigavel e sem solucao embutida.
- Papeis e responsabilidades registrados.
- Restricoes de tempo, infraestrutura, acessibilidade e dados confirmadas.
- Regras de autoria e uso de IA declaradas.
- Primeiro passo acionavel para `conduzir-descoberta`.
- Evidencias da abertura e revisao humana registrada quando aplicavel.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Usar somente referencias confirmadas por fonte oficial ou pela equipe pedagogica.
- Relacionar o desafio ao curriculo local e ao PPP sem transformar a BNCC em decoracao documental.
- Registrar "a validar pela equipe pedagogica" quando o alinhamento estiver pendente.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao entregar projeto, problema resolvido ou plano avaliativo integral para estudantes.
- Nao solicitar, registrar ou publicar dados pessoais desnecessarios.
- Nao solicitar credenciais, tokens ou segredos.
- Usar dados ficticios ou anonimizados em exemplos e demonstracoes.
- Preservar autoria estudantil e declarar apoio de IA.
- Prever acessibilidade, inclusao e alternativas de participacao desde a abertura.
- Escalar decisoes curriculares, institucionais, de imagem ou de dados para revisao humana competente.

## Examples - Exemplos

### Adequado

"O percurso foi aprovado para seis encontros. Vamos registrar os papeis da equipe, confirmar os recursos disponiveis e iniciar a descoberta investigando evidencias do problema, sem definir ainda a tecnologia."

### Ambiguo

"Vamos comecar o projeto."

Antes de iniciar, confirmar em no maximo tres perguntas qual e o percurso aprovado, quem participa e quais restricoes podem alterar o primeiro encontro.

### Bloqueante

"Entregue aos estudantes uma ideia pronta, o codigo e o pitch para ganhar tempo."

Bloquear a entrega pronta, preservar autoria e encaminhar a equipe para a investigacao orientada do problema.

## Performance Notes - Notas de desempenho

- Prioridade: clareza de papeis -> seguranca e autoria -> restricoes reais -> primeiro passo.
- Evitar repetir todo o percurso; apresentar apenas o necessario para iniciar.
- Fazer no maximo tres perguntas por rodada.
- Encerrar sempre com responsavel, evidencia esperada e proximo passo.

## Troubleshooting - Solucao de problemas

- Percurso ausente: interromper e executar `orquestrar-ipit`.
- Papeis indefinidos: registrar responsavel provisoria e solicitar validacao docente.
- Restricao institucional desconhecida: nao presumir permissao; escalar para gestao ou equipe pedagogica.
- Desafio ja contem solucao: reformular para uma pergunta investigavel.
- BNCC nao confirmada: registrar "a validar pela equipe pedagogica".

## Criterios de conclusao

A skill conclui quando houver acordo de trabalho, desafio inicial investigavel, papeis e responsabilidades, restricoes confirmadas, regras de autoria e uso de IA, revisao humana aplicavel e primeiro passo acionavel para `conduzir-descoberta`.

## Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: nova evidencia, regra de abertura ou exemplo compativel.
- MAJOR: alteracao de dependencia, escopo, produtos ou criterio de conclusao.

## Autoria

Metodologia e especificacao por **Sandra Maria Pereira**. Materiais derivados devem preservar esta atribuicao.