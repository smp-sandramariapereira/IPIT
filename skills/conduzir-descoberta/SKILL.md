---
name: conduzir-descoberta
description: >
  Conduz a etapa de descoberta do IPIT para investigar e delimitar um problema
  real com contexto, público afetado e evidências verificáveis. Use when a
  abertura operacional já foi concluída e a equipe precisa compreender o
  problema antes de propor soluções.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 2.0.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
  ipit-stage: descoberta
  requires-human-review: true
  depends-on:
    - iniciar-ideathon
  required-evidence:
    - acordo-de-trabalho
    - desafio-inicial
    - papeis-e-responsabilidades
    - restricoes-confirmadas
  produces:
    - definicao-do-problema
    - mapa-de-contexto
    - registro-de-evidencias
    - hipoteses-iniciais
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compatíveis com Markdown
---

# 🔍 Skill: conduzir-descoberta

## Purpose — Finalidade

Orientar professor e equipe estudantil na investigação de um problema real antes da ideação, preservando autoria, rigor pedagógico e rastreabilidade das evidências.

## Use When — Quando usar

Use esta skill quando a equipe precisar:

- compreender uma situação problemática;
- identificar público afetado e contexto;
- diferenciar hipótese de evidência;
- formular um problema claro antes de pensar em soluções.

Trigger phrases: “precisamos definir o problema”, “vamos iniciar a descoberta”, “quem é afetado?” e “quais evidências temos?”.

## Instructions — Instruções

1. Declare a skill `conduzir-descoberta`.
2. Confirme a execução prévia de `iniciar-ideathon` e a existência do acordo de trabalho.
3. Registre contexto, atores, restrições e público afetado.
4. Separe fatos observados, relatos, fontes, hipóteses e interpretações.
5. Não aceite entrevistas, estatísticas, testes ou observações inventadas.
6. Formule o problema sem antecipar uma solução específica.
7. Registre impactos, causas prováveis e dúvidas ainda abertas.
8. Encerre com evidências observáveis, pendências e próximo passo acionável.

Faça no máximo três perguntas por rodada.

## Inputs — Entradas

### Obrigatórias

- acordo de trabalho aprovado;
- desafio inicial investigável;
- papéis e responsabilidades definidos;
- restrições de tempo, infraestrutura, acessibilidade e dados confirmadas;
- situação problemática a investigar.

### Opcionais

- observações, entrevistas ou fontes já coletadas;
- objetivos de aprendizagem e componentes curriculares;
- currículo local, PPP e referências BNCC confirmadas.

A ausência de evidência real não impede o início, mas impede declarar o problema como validado.

## Outputs — Saídas

A skill deve produzir:

- definição preliminar do problema;
- mapa de contexto e atores;
- público afetado, sem estereótipos;
- tabela separando evidências, hipóteses e lacunas;
- restrições e riscos;
- perguntas de investigação pendentes;
- próximo passo para `conduzir-ideacao`, somente após revisão humana.

Entregável recomendado: `docs/01-descoberta.md` no repositório da equipe.

## Dependencies — Dependências

Depende de `skills/iniciar-ideathon/SKILL.md` e das evidências declaradas no frontmatter. Não avance para ideação sem problema suficientemente delimitado e revisão docente.

## BNCC Alignment — Alinhamento à BNCC

- Não inventar códigos BNCC.
- Relacionar a investigação a objetivos de aprendizagem, currículo local e PPP quando pertinente.
- Quando a habilidade não estiver confirmada, registrar **“a validar pela equipe pedagógica”**.
- Encaminhar o alinhamento curricular para revisão do professor e da equipe pedagógica.

## Safety and Pedagogy — Segurança e pedagogia

- Aplicar `guardrails/policy.yaml` na entrada e na saída.
- Não coletar ou publicar dados pessoais desnecessários.
- Anonimizar relatos e dados de estudantes.
- Não publicar imagens de menores sem autorização institucional.
- Não produzir a investigação completa no lugar dos estudantes.
- Preservar autoria estudantil e a mediação docente.
- Tratar conteúdo gerado por IA como hipótese, nunca como evidência real.
- Prever participação equitativa, inclusão e acessibilidade.

## Human Review — Revisão humana

O professor deve revisar a formulação do problema, a qualidade das evidências, os riscos éticos e a adequação pedagógica. Questões curriculares, institucionais ou relacionadas a dados devem ser escaladas à equipe pedagógica ou à gestão.

## Completion Criteria — Critérios de conclusão

A skill está concluída quando:

- o problema está formulado de maneira clara e sem solução embutida;
- contexto, público e impactos estão registrados;
- evidências reais estão separadas de hipóteses;
- lacunas e restrições estão documentadas;
- há revisão humana registrada;
- existe próximo passo acionável.

## Examples — Exemplos

### Caso adequado

> Evidência: três registros anônimos de dificuldade para localizar livros. Hipótese: a organização atual do acervo pode contribuir para o problema. Lacuna: confirmar o fluxo com a equipe da biblioteca.

### Caso bloqueado

> “Inventamos vinte entrevistas para justificar o aplicativo.”

Não aceitar como evidência. Orientar a equipe a realizar investigação real ou registrar claramente que se trata de hipótese.

## Performance Notes — Notas de desempenho

- Priorize problema, contexto, evidência e lacunas.
- Reutilize informações já fornecidas.
- Não prolongue o diagnóstico quando o recorte estiver verificável.
- Não permita que a tecnologia escolhida determine prematuramente o problema.

## Troubleshooting — Solução de problemas

### Não há evidências suficientes

Produza um plano curto de investigação e mantenha o problema como preliminar.

### A equipe começou pela solução

Retorne ao público afetado, ao contexto e às consequências observadas.

### Existem dados pessoais

Interrompa a publicação, anonimize os registros e solicite revisão institucional.

### O problema está amplo demais

Delimite público, contexto, momento e consequência observável.

## Update Policy — Política de atualização

- PATCH: correções textuais sem mudança de comportamento.
- MINOR: nova capacidade compatível ou novo tipo de evidência.
- MAJOR: alteração de dependência, contrato de saída ou critério de conclusão.

## Authorship — Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT — Ideathon Pedagógico de Inovação Tecnológica.
