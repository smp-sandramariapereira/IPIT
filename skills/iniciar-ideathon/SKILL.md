---
name: iniciar-ideathon
description: >
	Conduzir o primeiro atendimento para iniciar um Ideathon pedagogico com
	diagnostico objetivo e sem gerar plano completo prematuro. Use when o
	docente ainda esta definindo contexto, limites e intencao pedagogica.
metadata:
	author: Sandra Maria Pereira
	methodology: IPIT
	version: 1.0.0
	mcp-server: none
	personas:
		- professor
		- professora
	ipit-stage: inicio
	requires-human-review: true
	depends-on: []
	required-evidence:
		- perfil docente e contexto da turma
		- intencao pedagogica inicial
		- restricoes de tempo e infraestrutura
	produces:
		- diagnostico-inicial
		- perguntas-diagnosticas
		- proximo-passo-definido
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

## Instructions - Instrucoes

- Declarar a skill utilizada: `iniciar-ideathon`.
- Identificar perfil docente, etapa/serie, area e intencao pedagogica.
- Fazer no maximo tres perguntas diagnosticas, curtas e acionaveis.
- Nao gerar plano completo, cronograma final ou rubrica completa nesta etapa.
- Ajustar perguntas a tempo, infraestrutura, turma e equipamentos disponiveis.
- Incluir desde o inicio curriculo local, PPP, avaliacao processual, inclusao e acessibilidade.
- Registrar necessidade de participacao da equipe pedagogica quando houver decisao curricular.
- Encerrar com sintese do contexto e proximo passo claro.

## Inputs - Entradas

- Pedido inicial do docente para iniciar Ideathon (bloqueante).
- Contexto de turma, ano/serie e componente curricular (bloqueante).
- Restricoes de tempo e infraestrutura (bloqueante).
- Objetivo pedagogico inicial (bloqueante).
- Contexto BNCC/curriculo local/PPP (nao bloqueante, registrar "a validar pela equipe pedagogica" quando faltar confirmacao).

## Outputs - Saidas

- Perfil e contexto inicial sintetizados.
- Intencao pedagogica declarada.
- Ate tres perguntas diagnosticas objetivas.
- Proximo passo acionavel para continuar a jornada.
- Limite explicito: nao entregar projeto pronto nem plano completo nesta etapa.

## BNCC Alignment - Alinhamento a BNCC

- Nao inventar codigos BNCC.
- Quando nao houver habilidade confirmada, registrar: "a validar pela equipe pedagogica".
- Relacionar diagnostico ao curriculo local, PPP e contexto escolar.

## Safety and Pedagogy - Seguranca e pedagogia

- Nao solicitar nem expor dados pessoais desnecessarios de estudantes.
- Nao aceitar pedido de trabalho avaliativo completo por estudante.
- Nao solicitar credenciais, tokens ou segredos.
- Garantir linguagem pedagogicamente responsavel e inclusiva.
- Exigir revisao humana em decisoes pedagogicas, curriculares ou institucionais.

## Examples - Exemplos

- Exemplo de saida: "Perfil identificado (3o ano tecnico, 8 encontros). Perguntas: 1) Qual problema real da escola sera investigado? 2) Quais recursos estao disponiveis por encontro? 3) Quais criterios de avaliacao processual a equipe pedagogica quer adotar?"

## Performance Notes - Notas de desempenho

- Prioridade: seguranca pedagogica e de dados -> clareza do diagnostico -> proximo passo.
- Responder de forma curta; evitar plano detalhado nesta etapa.
- Se faltar entrada bloqueante, interromper e solicitar dados minimos.

## Troubleshooting - Solucao de problemas

- Erro bloqueante: ausencia de contexto da turma, objetivo pedagogico ou restricoes basicas.
- Aviso nao bloqueante: BNCC pendente de confirmacao, PPP ainda nao informado.
- Em risco curricular ou institucional, escalar para equipe pedagogica/gestao.

## Criterios de conclusao

A skill conclui quando houver perfil e contexto inicial registrados, intencao pedagogica clara, ate tres perguntas diagnosticas definidas e proximo passo acionavel sem gerar plano completo.

## Politica de atualizacao

- PATCH: ajustes textuais sem mudanca de comportamento.
- MINOR: nova regra de diagnostico compativel com o fluxo atual.
- MAJOR: mudanca de escopo da etapa inicial ou de criterios de conclusao.