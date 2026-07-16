---
name: desenhar-solucao
description: >
  Detalha a solução selecionada em fluxos, funcionalidades, experiência de uso e
  protótipo inicial. Use when a ideação já tiver priorizado uma proposta e a
  equipe precisar demonstrar como ela funcionará antes da escolha tecnológica.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.1.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
  ipit-stage: solucao
  requires-human-review: true
  depends-on:
    - conduzir-ideacao
  required-evidence:
    - proposta-selecionada
    - justificativa-da-escolha
    - definicao-do-problema
  produces:
    - perfil-de-usuario
    - jornada-do-usuario
    - fluxo-da-solucao
    - especificacao-funcional
    - prototipo-inicial
    - criterios-de-validacao
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compatíveis com Markdown
---

# 🧩 Skill: desenhar-solucao

## Purpose — Finalidade

Transformar a proposta priorizada na ideação em uma descrição compreensível e testável da solução, preservando o vínculo com o problema investigado e evitando decisões tecnológicas prematuras.

## Use When — Quando usar

Use esta skill quando:

- a equipe já tiver concluído `conduzir-ideacao`;
- houver uma proposta selecionada e justificada;
- for necessário desenhar fluxo, funcionalidades e experiência de uso;
- a equipe precisar criar um protótipo inicial antes de selecionar tecnologias.

Trigger phrases:

- "como essa solução vai funcionar?";
- "precisamos desenhar o fluxo";
- "vamos criar o protótipo";
- "quais funcionalidades são essenciais?".

## Instructions — Instruções

1. Declare a skill utilizada: `desenhar-solucao`.
2. Confirme a dependência `conduzir-ideacao` e as evidências de entrada.
3. Relembre o problema, o público afetado e a proposta selecionada.
4. Defina o perfil de usuário com base em evidências, sem estereótipos.
5. Descreva a jornada principal e os pontos de contato da solução.
6. Modele o fluxo principal, incluindo entradas, decisões, saídas e exceções.
7. Classifique funcionalidades como essenciais, desejáveis ou fora do escopo atual.
8. Inclua requisitos de acessibilidade e participação equitativa.
9. Registre suposições, restrições, riscos e questões ainda abertas.
10. Produza um protótipo inicial em papel, wireframe ou ferramenta digital adequada ao contexto.
11. Defina critérios de validação com usuários ou responsáveis, sem inventar resultados.
12. Encerre com evidências observáveis e próximo passo acionável.

Faça no máximo três perguntas por rodada e reutilize informações já fornecidas.

## Inputs — Entradas

### Obrigatórias

- `proposta-selecionada`;
- `justificativa-da-escolha`;
- `definicao-do-problema`;
- público afetado ou perfil de usuário fundamentado;
- restrições iniciais da escola ou da equipe.

A ausência da proposta selecionada ou da definição do problema é bloqueante.

### Opcionais

- mapa de contexto;
- requisitos institucionais;
- critérios de acessibilidade;
- referências de soluções semelhantes;
- recursos disponíveis para prototipação.

## Outputs — Saídas

A skill deve produzir:

- perfil de usuário sem estereótipos;
- jornada principal;
- fluxo da solução;
- lista de funcionalidades essenciais, desejáveis e fora do escopo;
- especificação funcional inicial;
- protótipo inicial;
- critérios de validação;
- riscos, suposições e questões abertas;
- próximo passo: `selecionar-tecnologia`.

Entregável recomendado: `docs/03-solucao.md` no repositório da equipe.

## Dependencies — Dependências

Depende de:

1. `skills/conduzir-ideacao/SKILL.md`;
2. proposta selecionada e justificada;
3. evidências da descoberta ainda rastreáveis.

Não avance para tecnologia se o fluxo da solução ou as funcionalidades essenciais não estiverem claros.

## BNCC Alignment — Alinhamento à BNCC

- Não inventar códigos BNCC.
- Quando não houver habilidade confirmada, registrar **“a validar pela equipe pedagógica”**.
- Relacionar o desenho da solução a objetivos de aprendizagem, currículo local e PPP quando a atividade fizer parte do planejamento pedagógico.
- Associar protótipo, fluxo e justificativas a evidências observáveis de aprendizagem.
- Submeter o alinhamento curricular à revisão docente e da equipe pedagógica.

## Safety and Pedagogy — Segurança e pedagogia

- Não usar dados pessoais reais em personas, jornadas ou protótipos.
- Não solicitar credenciais, senhas ou tokens.
- Não tratar suposição como necessidade comprovada do usuário.
- Não inventar entrevistas, testes ou validações.
- Preservar a autoria estudantil; o agente orienta, questiona e revisa, mas não substitui o trabalho da equipe.
- Considerar acessibilidade desde o primeiro fluxo, e não como correção posterior.
- Evitar dark patterns, exclusão, exposição ou vigilância desnecessária.
- Aplicar `guardrails/policy.yaml` nas entradas e saídas.

## Human Review — Revisão humana

Revisão obrigatória por professor e, quando aplicável, equipe pedagógica para:

- coerência entre problema e solução;
- perfil de usuário e ausência de estereótipos;
- funcionalidades essenciais;
- acessibilidade;
- coleta ou uso de dados;
- critérios de validação;
- alinhamento curricular.

## Completion Criteria — Critérios de conclusão

A skill está concluída quando:

- a solução responde claramente ao problema definido;
- o perfil de usuário está fundamentado;
- a jornada e o fluxo principal estão documentados;
- entradas, saídas e exceções estão identificadas;
- funcionalidades essenciais e limites estão definidos;
- existe protótipo inicial;
- acessibilidade e riscos foram considerados;
- critérios de validação foram registrados;
- a revisão humana está prevista;
- o próximo passo é `selecionar-tecnologia`.

## Examples — Exemplos

### Caso adequado

A equipe desenha o fluxo de empréstimo de livros: busca, seleção, solicitação, confirmação e devolução, usando dados fictícios e prevendo navegação por teclado.

### Caso com contexto insuficiente

> "Crie todas as telas do nosso aplicativo."

Antes de desenhar, solicite a proposta selecionada, o problema e o fluxo principal esperado.

### Caso bloqueante

> "Use nomes, fotos e notas reais dos alunos no protótipo."

Bloqueie o uso de dados reais e proponha dados fictícios ou anonimizados, com validação institucional.

## Performance Notes — Notas de desempenho

- Priorize o fluxo principal antes de variações secundárias.
- Comece com protótipos de baixa fidelidade quando o contexto ainda estiver em validação.
- Não discuta stack antes de concluir o desenho funcional.
- Use tabelas ou Mermaid quando melhorarem a compreensão do fluxo.
- Evite especificações excessivas para funcionalidades fora do MVP.

## Troubleshooting — Solução de problemas

### Proposta ainda vaga

Retorne à ideação e refine a proposta selecionada.

### Fluxo excessivamente complexo

Reduza ao caminho principal e registre exceções para ciclos posteriores.

### Perfil de usuário baseado em estereótipos

Substitua inferências por necessidades observadas ou marque como hipótese a validar.

### Protótipo depende de dados reais

Use dados fictícios ou anonimizados e solicite revisão institucional.

### Ausência de acessibilidade

Inclua requisitos mínimos antes de concluir a skill.

## Update Policy — Política de atualização

- PATCH: ajustes textuais sem mudança de comportamento.
- MINOR: nova técnica de prototipação ou validação compatível.
- MAJOR: alteração de dependência, escopo ou contrato de saída.

## Authorship — Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT — Ideathon Pedagógico de Inovação Tecnológica.
