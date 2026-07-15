# Metodologia Ideathon — da ideia ao MVP em 8 etapas

Esta metodologia organiza uma jornada prática de **oito etapas** para transformar problemas reais em projetos digitais demonstráveis. O percurso combina investigação, ideação, engenharia de software, colaboração no GitHub, uso crítico de Inteligência Artificial e fundamentos de Web3.

> **Princípio central:** cada etapa termina com um entregável verificável no repositório. O avanço depende da evidência produzida, não apenas da participação.

## Objetivos de aprendizagem

Ao concluir o percurso, a equipe deverá ser capaz de:

- investigar e delimitar um problema real;
- formular uma proposta de valor orientada ao usuário;
- desenhar fluxos, interfaces e escopo de solução;
- selecionar tecnologias de maneira justificada;
- definir um MVP com critérios de sucesso;
- documentar arquitetura, tarefas e decisões no GitHub;
- desenvolver, testar e demonstrar um protótipo funcional;
- comunicar resultados por meio de pitch técnico.

## Organização geral

- **Duração sugerida:** 8 dias ou 8 encontros.
- **Formato:** equipes pequenas, com papéis distribuídos e revisão diária.
- **Repositório:** todo o trabalho deve permanecer versionado no GitHub.
- **Tecnologias de apoio:** GitHub, banco de dados, ferramentas de IA generativa e assistentes de código.
- **Web3:** deve ser utilizada somente quando produzir valor técnico real, como verificabilidade, identidade, transparência, interoperabilidade ou registro auditável.

---

## Etapa 01 — Descoberta

**Finalidade:** compreender o contexto antes de propor tecnologia.

### Atividades

1. Apresentar o desafio e formar as equipes.
2. Identificar usuários, atores afetados e contexto de uso.
3. Levantar dores, necessidades e restrições.
4. Formular o problema principal em uma frase clara.
5. Registrar evidências, hipóteses e dúvidas.

### Perguntas orientadoras

- Quem vivencia o problema?
- Em qual situação ele ocorre?
- Qual consequência concreta ele gera?
- Como sabemos que o problema é relevante?

### Entregável

`docs/01-descoberta.md`, contendo:

- problema priorizado;
- público definido;
- evidências ou observações;
- objetivos iniciais;
- critérios que indicam melhoria.

### Critério de conclusão

Uma pessoa externa deve compreender **quem possui o problema, qual é a dor e por que ela importa**.

---

## Etapa 02 — Ideação

**Finalidade:** gerar alternativas e escolher uma direção de solução.

### Atividades

1. Realizar brainstorming sem julgamento inicial.
2. Agrupar ideias semelhantes.
3. Avaliar impacto, viabilidade e aderência ao problema.
4. Selecionar a melhor hipótese.
5. Elaborar proposta de valor e público-alvo.

### Entregável

`docs/02-ideacao.md`, contendo:

- lista de alternativas;
- matriz simples de priorização;
- ideia selecionada;
- proposta de valor;
- perfil de usuário ou persona.

### Critério de conclusão

A solução escolhida deve responder diretamente ao problema descrito na Etapa 01.

---

## Etapa 03 — Solução

**Finalidade:** transformar a ideia em experiência de uso compreensível.

### Atividades

1. Desenhar o fluxo principal do usuário.
2. Definir jornada, entradas, ações e resultados.
3. Criar esboços de telas ou wireframes.
4. Identificar exceções, riscos e pontos de abandono.
5. Validar o fluxo com colegas ou usuários potenciais.

### Entregáveis

- `docs/03-solucao.md`;
- fluxo do usuário;
- wireframes ou protótipos;
- escopo funcional inicial.

### Critério de conclusão

O fluxo deve mostrar como o usuário sai do problema inicial e alcança um resultado útil.

---

## Etapa 04 — Tecnologia

**Finalidade:** selecionar recursos técnicos coerentes com o MVP.

### Atividades

1. Definir frontend, backend e banco de dados.
2. Avaliar APIs, serviços externos e autenticação.
3. Decidir se há necessidade real de blockchain.
4. Identificar automações e usos responsáveis de IA.
5. Registrar limitações, riscos de segurança e dados tratados.

### Decisão de uso de Web3

A equipe deve responder:

- O que precisa ser verificável ou auditável?
- Existe mais de uma organização ou parte que não deve controlar o registro sozinha?
- Um banco de dados convencional resolveria o problema com menor custo e complexidade?
- Quais dados **não** devem ser colocados on-chain?

### Entregável

`docs/04-tecnologia.md`, contendo:

- stack escolhida;
- justificativas;
- integrações previstas;
- requisitos de segurança e privacidade;
- decisão fundamentada sobre Web3.

### Critério de conclusão

Cada tecnologia deve estar ligada a um requisito concreto, evitando complexidade ornamental.

---

## Etapa 05 — MVP

**Finalidade:** definir o menor produto capaz de demonstrar valor.

### Atividades

1. Separar funcionalidades essenciais das desejáveis.
2. Definir o caminho crítico da demonstração.
3. Elaborar critérios de sucesso.
4. Estabelecer restrições de tempo e escopo.
5. Transformar funcionalidades em histórias ou tarefas.

### Entregável

`docs/05-mvp.md`, contendo:

- definição do MVP;
- funcionalidades essenciais;
- funcionalidades fora do escopo;
- prioridades;
- critérios de sucesso e demonstração.

### Critério de conclusão

O MVP deve ser realizável no tempo disponível e demonstrar uma proposta de valor completa, ainda que limitada.

---

## Etapa 06 — Arquitetura

**Finalidade:** planejar a construção antes da implementação intensiva.

### Atividades

1. Desenhar os componentes do sistema.
2. Definir modelos e fluxos de dados.
3. Estruturar pastas e padrões do repositório.
4. Criar issues e distribuir tarefas.
5. Definir convenções de branches, commits e revisão.

### Entregáveis

- `docs/06-arquitetura.md`;
- diagrama de arquitetura;
- estrutura inicial do repositório;
- backlog no GitHub;
- responsáveis e dependências.

### Critério de conclusão

A equipe deve saber **o que construir, em qual ordem, onde registrar e quem é responsável**.

---

## Etapa 07 — Desenvolvimento

**Finalidade:** implementar e validar o MVP.

### Atividades

1. Desenvolver por incrementos pequenos.
2. Integrar frontend, backend, banco de dados e serviços.
3. Executar testes técnicos e de fluxo.
4. Registrar problemas e decisões nas issues.
5. Atualizar documentação e instruções de execução.

### Regras de trabalho no GitHub

- uma tarefa relevante por issue;
- commits descritivos e frequentes;
- branches para mudanças de maior risco;
- revisão antes de integrar;
- README atualizado com instalação e execução;
- nenhuma credencial ou dado pessoal no repositório.

### Entregável

MVP executável, acompanhado de:

- código-fonte;
- instruções de instalação;
- evidências de teste;
- lista de limitações conhecidas.

### Critério de conclusão

O fluxo principal deve funcionar de ponta a ponta ou possuir uma demonstração tecnicamente honesta das partes ainda simuladas.

---

## Etapa 08 — Pitch e finalização

**Finalidade:** demonstrar resultado, processo e aprendizagem.

### Estrutura sugerida do pitch

1. Problema e público.
2. Evidência da necessidade.
3. Solução proposta.
4. Demonstração do MVP.
5. Arquitetura e tecnologias.
6. Uso de Web3, quando aplicável.
7. Resultados, limitações e próximos passos.

### Entregáveis

- pitch de 3 a 5 minutos;
- demonstração do MVP;
- README final;
- registro de aprendizados;
- backlog de continuidade.

### Critério de conclusão

A apresentação deve demonstrar problema, solução, produto funcionando e evidências do processo de construção.

---

## Fluxo resumido

```mermaid
flowchart LR
    A[1. Descoberta] --> B[2. Ideação]
    B --> C[3. Solução]
    C --> D[4. Tecnologia]
    D --> E[5. MVP]
    E --> F[6. Arquitetura]
    F --> G[7. Desenvolvimento]
    G --> H[8. Pitch e finalização]
```

## Estrutura recomendada para os repositórios das equipes

```text
.
├── README.md
├── docs/
│   ├── 01-descoberta.md
│   ├── 02-ideacao.md
│   ├── 03-solucao.md
│   ├── 04-tecnologia.md
│   ├── 05-mvp.md
│   ├── 06-arquitetura.md
│   ├── 07-testes.md
│   └── 08-pitch.md
├── src/
├── tests/
├── assets/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## Avaliação por evidências

| Dimensão | Evidências esperadas |
|---|---|
| Problema e usuário | pesquisa, observações, definição do problema |
| Proposta de valor | hipótese escolhida e justificativa |
| Experiência | fluxo, wireframes e validação |
| Decisão técnica | stack, arquitetura, segurança e privacidade |
| Execução | código, commits, issues e integração |
| Qualidade | testes, documentação e tratamento de erros |
| Colaboração | divisão de tarefas, revisão e comunicação |
| Comunicação | demonstração, pitch e reflexão final |

### Rubrica sintética

- **4 — Evidência consistente:** entrega completa, justificada e validada.
- **3 — Evidência adequada:** entrega funcional, com pequenas lacunas.
- **2 — Evidência parcial:** entrega incompleta ou pouco fundamentada.
- **1 — Evidência insuficiente:** atividade sem comprovação verificável.

## Uso responsável de Inteligência Artificial

Ferramentas como GPT, Gemini e GitHub Copilot podem apoiar pesquisa, prototipagem, depuração e documentação. A equipe continua responsável por:

- revisar todo conteúdo gerado;
- compreender o código incorporado;
- testar resultados;
- citar o uso da ferramenta quando relevante;
- não inserir dados pessoais, segredos ou credenciais;
- distinguir evidência real de conteúdo sintetizado.

## Princípios de segurança e proteção de dados

- coletar somente dados estritamente necessários;
- evitar publicação de nomes, notas ou dados pessoais de estudantes;
- não armazenar dados sensíveis em blockchain;
- nunca versionar chaves privadas, tokens de API ou senhas;
- utilizar ambientes de teste e ativos sem valor econômico;
- documentar riscos e limitações do protótipo.

## Resultado esperado

Ao final, cada equipe deverá possuir um repositório que conte a história completa do projeto: **problema investigado, decisões tomadas, arquitetura planejada, MVP construído, testes realizados e resultado apresentado**.