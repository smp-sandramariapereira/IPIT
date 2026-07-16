---
name: conduzir-ideacao
description: >
  Conduz a ideação colaborativa do IPIT com geração, agrupamento e priorização
  de alternativas baseadas nas evidências da descoberta. Use when o problema
  já estiver delimitado e a equipe precisar escolher uma proposta de solução.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.1.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
  ipit-stage: ideacao
  requires-human-review: true
  depends-on:
    - conduzir-descoberta
  required-evidence:
    - definicao-do-problema
    - mapa-de-contexto
    - registro-de-evidencias
  produces:
    - lista-de-alternativas
    - agrupamento-de-ideias
    - matriz-de-priorizacao
    - proposta-selecionada
    - justificativa-da-escolha
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compatíveis com Markdown
---

# 💡 Skill: conduzir-ideacao

## Purpose — Finalidade

Conduzir uma ideação estruturada e participativa, produzindo alternativas coerentes com o problema investigado e selecionando uma proposta com critérios explícitos, sem antecipar decisões técnicas ou retirar a autoria da equipe estudantil.

## Use When — Quando usar

Use esta skill quando:

- a etapa de descoberta estiver concluída;
- o problema e o público afetado estiverem suficientemente delimitados;
- a equipe precisar gerar possibilidades de solução;
- houver necessidade de comparar impacto, viabilidade, acessibilidade e aderência ao problema.

Trigger phrases:

- "precisamos gerar ideias";
- "qual solução devemos escolher";
- "como priorizar as alternativas";
- "vamos começar a ideação".

## Instructions — Instruções

1. Declarar a utilização da skill `conduzir-ideacao`.
2. Confirmar a conclusão de `conduzir-descoberta` e verificar suas evidências.
3. Reapresentar o problema em uma frase, sem alterá-lo silenciosamente.
4. Gerar alternativas antes de discutir implementação ou stack tecnológica.
5. Garantir participação equitativa e registrar a autoria das contribuições.
6. Agrupar ideias semelhantes sem apagar diferenças relevantes.
7. Definir critérios de priorização adequados ao contexto escolar.
8. Comparar as alternativas por aderência ao problema, impacto, viabilidade, acessibilidade, riscos e aprendizagem.
9. Selecionar uma proposta com justificativa baseada nas evidências da descoberta.
10. Registrar hipóteses e pontos ainda não validados.
11. Encerrar com evidência verificável e próximo passo acionável.

## Inputs — Entradas

### Obrigatórias

- definição do problema;
- público afetado;
- mapa de contexto;
- evidências registradas na descoberta;
- restrições de tempo, infraestrutura e acessibilidade.

A ausência da definição do problema ou das evidências da descoberta é bloqueante.

### Opcionais

- critérios institucionais;
- objetivos de aprendizagem;
- currículo local e PPP;
- repertório de soluções semelhantes;
- limitações técnicas já conhecidas.

A ausência dessas informações gera aviso e deve ser registrada para revisão posterior.

## Outputs — Saídas

A skill deve produzir:

- lista de alternativas distintas;
- agrupamento temático das ideias;
- critérios de priorização com justificativa;
- matriz comparativa;
- proposta selecionada;
- justificativa da escolha;
- riscos, hipóteses e pendências;
- evidência esperada para a etapa seguinte;
- próximo passo recomendado: `desenhar-solucao`.

Modelo mínimo de priorização:

| Alternativa | Aderência ao problema | Impacto | Viabilidade | Acessibilidade | Riscos | Decisão |
|---|---:|---:|---:|---:|---|---|
| [ideia] | [critério] | [critério] | [critério] | [critério] | [risco] | [manter, combinar ou descartar] |

## Dependencies — Dependências

Esta skill depende de:

- `skills/conduzir-descoberta/SKILL.md`.

Não avançar quando o problema estiver genérico, quando as evidências forem inventadas ou quando a equipe estiver tentando escolher tecnologia antes de definir a solução.

## BNCC Alignment — Alinhamento à BNCC

- Relacionar a dinâmica de ideação aos objetivos de aprendizagem quando aplicável.
- Considerar competências relacionadas a pensamento crítico e criativo, comunicação, argumentação, cooperação e cultura digital somente quando houver relação justificável.
- Não inventar códigos BNCC.
- Quando a habilidade não estiver confirmada, registrar **“a validar pela equipe pedagógica”**.
- Considerar currículo local e PPP quando a ideação fizer parte de planejamento curricular.

## Safety and Pedagogy — Segurança e pedagogia

- Não produzir a solução final no lugar dos estudantes.
- Não tratar quantidade de ideias como único indicador de qualidade.
- Não usar IA para substituir discussão, justificativa ou decisão da equipe.
- Registrar o uso de IA e revisar criticamente as sugestões geradas.
- Não inventar pesquisa, entrevista, validação ou resultado.
- Não expor dados pessoais nas personas, exemplos ou matrizes.
- Evitar estereótipos sobre usuários ou comunidades.
- Garantir participação equitativa e recursos de acessibilidade.
- Aplicar `guardrails/policy.yaml` nas entradas e saídas.

## Human Review — Revisão humana

A revisão do professor é obrigatória antes de avançar para o desenho da solução.

A equipe pedagógica deve revisar quando houver:

- associação curricular ou BNCC;
- implicação institucional;
- participação de parceiros externos;
- coleta ou uso de dados;
- risco de exclusão ou barreira de acessibilidade.

A revisão deve confirmar que a proposta escolhida é coerente com o problema e que a priorização não foi decidida apenas pela IA.

## Completion Criteria — Critérios de conclusão

A skill está concluída quando:

- foram geradas alternativas suficientemente distintas;
- as ideias foram agrupadas sem perda de autoria;
- os critérios de priorização foram explicitados;
- as alternativas foram comparadas;
- uma proposta foi selecionada e justificada;
- hipóteses, riscos e pendências foram registrados;
- a revisão docente foi indicada;
- o próximo passo `desenhar-solucao` foi definido.

## Examples — Exemplos

### Caso adequado

Problema: estudantes têm dificuldade para localizar livros disponíveis na biblioteca.

A equipe gera alternativas como catálogo digital, sinalização física, terminal de consulta e sistema de reservas. Depois compara impacto, custo, acesso sem celular e prazo antes de selecionar uma proposta.

### Caso que exige retorno à descoberta

A equipe quer criar um aplicativo, mas não possui evidência de que o problema existe ou de quem é afetado. Interromper a ideação e retornar a `conduzir-descoberta`.

### Pedido inadequado de estudante

> Escolha a melhor ideia e faça o projeto completo para mim.

Não entregar o projeto pronto. Orientar a equipe a aplicar critérios, justificar a decisão e preservar a autoria estudantil.

## Performance Notes — Notas de desempenho

- Fazer no máximo três perguntas por rodada.
- Priorizar diversidade de alternativas antes da convergência.
- Evitar listas extensas sem critérios.
- Reutilizar evidências produzidas na descoberta.
- Explicitar primeiro a decisão e depois a justificativa.
- Quando houver empate, propor teste rápido, consulta ao público ou combinação controlada de ideias.

## Troubleshooting — Solução de problemas

### Problema ainda genérico

Retornar à descoberta e solicitar recorte de público, contexto, consequência e evidências.

### Apenas uma ideia foi apresentada

Solicitar alternativas com abordagens diferentes antes de priorizar.

### Equipe escolheu pela preferência pessoal

Reaplicar a matriz de priorização e exigir justificativa vinculada às evidências.

### Ideias excessivamente complexas

Separar valor central de funcionalidades acessórias. A definição de escopo ocorrerá em `definir-mvp`.

### Uso excessivo de IA

Solicitar registro das sugestões, critérios de descarte e alterações realizadas pela equipe.

### Risco pedagógico, institucional ou de dados

Pausar e escalar para professor, equipe pedagógica ou gestão, conforme o impacto.

## Update Policy — Política de atualização

- PATCH: ajustes textuais sem mudança de comportamento.
- MINOR: novos critérios ou formatos compatíveis com o fluxo atual.
- MAJOR: mudança de dependência, saída obrigatória ou regra de revisão humana.

## Authorship — Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT — Ideathon Pedagógico de Inovação Tecnológica.
