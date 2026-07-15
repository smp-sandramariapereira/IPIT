# 🛠️ Metodologia IPIT — da ideia ao MVP em 8 etapas

O IPIT organiza uma jornada prática para transformar problemas reais em projetos digitais demonstráveis.

> 🎯 **Princípio central:** cada etapa termina com um entregável verificável no repositório.

## 🧠 Objetivos de aprendizagem

Ao concluir o percurso, a equipe deverá ser capaz de:

- investigar e delimitar um problema real;
- formular uma proposta de valor orientada ao usuário;
- desenhar fluxos, interfaces e escopo;
- selecionar tecnologias de forma justificada;
- definir um MVP com critérios de sucesso;
- documentar arquitetura, tarefas e decisões no GitHub;
- desenvolver, testar e demonstrar um protótipo;
- comunicar resultados por meio de um pitch.

## 🔄 Fluxo geral

```mermaid
flowchart LR
    A[🔍 1. Descoberta] --> B[💡 2. Ideação]
    B --> C[🧩 3. Solução]
    C --> D[⚙️ 4. Tecnologia]
    D --> E[🚀 5. MVP]
    E --> F[🏗️ 6. Arquitetura]
    F --> G[💻 7. Desenvolvimento]
    G --> H[🎤 8. Pitch]
```

## 🔍 Etapa 01 — Descoberta

**Finalidade:** compreender o contexto antes de propor tecnologia.

### Atividades

1. Apresentar o desafio e formar equipes.
2. Identificar usuários e atores afetados.
3. Levantar dores, necessidades e restrições.
4. Formular o problema em uma frase clara.
5. Registrar evidências, hipóteses e dúvidas.

### Entregável

`docs/01-descoberta.md`, contendo problema priorizado, público, evidências e critérios de melhoria.

## 💡 Etapa 02 — Ideação

**Finalidade:** gerar alternativas e selecionar uma direção de solução.

### Atividades

1. Realizar brainstorming.
2. Agrupar ideias semelhantes.
3. Avaliar impacto, viabilidade e aderência.
4. Selecionar a hipótese prioritária.
5. Elaborar proposta de valor e persona.

### Entregável

`docs/02-ideacao.md`, com alternativas, priorização, ideia selecionada e proposta de valor.

## 🧩 Etapa 03 — Solução

**Finalidade:** transformar a ideia em uma experiência de uso compreensível.

### Atividades

- desenhar o fluxo principal;
- definir jornada, entradas, ações e resultados;
- criar wireframes;
- identificar riscos e exceções;
- validar com colegas ou usuários potenciais.

### Entregáveis

`docs/03-solucao.md`, fluxo do usuário, wireframes e escopo funcional inicial.

## ⚙️ Etapa 04 — Tecnologia

**Finalidade:** selecionar recursos técnicos coerentes com o problema e o MVP.

### Atividades

- definir frontend, backend e banco de dados;
- avaliar APIs, autenticação e integrações;
- identificar automações e usos responsáveis de IA;
- avaliar a necessidade real de Web3;
- registrar riscos de segurança e privacidade.

### Entregável

`docs/04-tecnologia.md`, com stack, justificativas, integrações e requisitos de segurança.

> 💡 A tecnologia deve responder a um requisito concreto, evitando complexidade ornamental.

## 🚀 Etapa 05 — MVP

**Finalidade:** definir o menor produto capaz de demonstrar valor.

### Atividades

- separar funções essenciais das desejáveis;
- definir o caminho crítico da demonstração;
- elaborar critérios de sucesso;
- limitar tempo e escopo;
- transformar funções em tarefas.

### Entregável

`docs/05-mvp.md`, com escopo, prioridades, funções excluídas e critérios de sucesso.

## 🏗️ Etapa 06 — Arquitetura

**Finalidade:** planejar a construção antes da implementação intensiva.

### Atividades

- desenhar componentes e fluxos de dados;
- estruturar pastas e padrões;
- criar issues;
- distribuir responsabilidades;
- definir convenções de commits e revisão.

### Entregáveis

`docs/06-arquitetura.md`, diagrama, backlog e plano de ação.

## 💻 Etapa 07 — Desenvolvimento

**Finalidade:** implementar e validar o MVP.

### Regras de trabalho

- uma tarefa relevante por issue;
- commits descritivos e frequentes;
- documentação atualizada;
- testes do fluxo principal;
- nenhuma credencial ou dado pessoal no repositório.

### Entregável

MVP executável, código-fonte, instruções, evidências de teste e limitações conhecidas.

## 🎤 Etapa 08 — Pitch e finalização

**Finalidade:** demonstrar resultado, processo e aprendizagem.

### Estrutura do pitch

1. Problema e público.
2. Evidência da necessidade.
3. Solução proposta.
4. Demonstração do MVP.
5. Arquitetura e tecnologias.
6. Resultados, limitações e próximos passos.

### Entregáveis

Pitch, demonstração, README final, retrospectiva e backlog de continuidade.

## 📊 Avaliação por evidências

| Dimensão | Evidências esperadas |
|---|---|
| Problema e usuário | pesquisa e definição clara |
| Proposta de valor | hipótese e justificativa |
| Experiência | fluxo, wireframes e validação |
| Decisão técnica | stack, arquitetura e segurança |
| Execução | código, commits, issues e integração |
| Qualidade | testes, documentação e tratamento de erros |
| Colaboração | divisão de tarefas e revisão |
| Comunicação | demonstração, pitch e reflexão |

## 🤖 Uso responsável de IA

GPT, Gemini e GitHub Copilot podem apoiar pesquisa, prototipação, depuração e documentação. A equipe continua responsável por revisar, compreender, testar e registrar o uso das ferramentas.

## 🔐 Segurança e proteção de dados

- coletar somente dados necessários;
- não publicar dados pessoais de estudantes;
- nunca versionar senhas, chaves ou tokens;
- utilizar ambientes de teste;
- documentar riscos e limitações.
