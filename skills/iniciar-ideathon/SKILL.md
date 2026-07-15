---
name: iniciar-ideathon
description: Diagnostica o contexto escolar e cria o plano inicial de aplicação do IPIT sem retirar a autoria docente ou estudantil.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT — Ideathon Pedagógico de Inovação Tecnológica
  version: 0.1.0
license: Consulte a licença do repositório.
compatibility: Agentes e assistentes de IA que utilizem arquivos Markdown como instruções de projeto.
---

# 🚀 Skill: iniciar-ideathon

## 🎯 Finalidade

Orientar professor, equipe pedagógica ou gestão escolar na definição do primeiro plano de aplicação do IPIT.

Esta skill deve transformar uma intenção genérica — por exemplo, “quero fazer um Ideathon com minha turma” — em uma proposta inicial coerente com:

- objetivos curriculares;
- perfil dos estudantes;
- tempo disponível;
- infraestrutura;
- equipe docente;
- critérios de avaliação;
- segurança, privacidade e acessibilidade;
- validação da gestão e da equipe pedagógica.

**Autora da metodologia:** Sandra Maria Pereira.

---

## 👥 Quando usar

Use esta skill quando o usuário desejar:

- começar uma aplicação do IPIT;
- escolher entre Micro-Ideathon, oito encontros ou projeto trimestral;
- montar um cronograma inicial;
- apresentar a proposta para a equipe pedagógica;
- avaliar viabilidade antes de mobilizar estudantes;
- adaptar a metodologia à infraestrutura da escola.

Não use esta skill para conduzir uma etapa específica já iniciada. Nesse caso, selecione a skill correspondente à etapa.

---

## 🧭 Instruções

### 1. Identifique o perfil do usuário

Confirme se o interlocutor é:

- professor;
- coordenador pedagógico;
- gestor;
- equipe técnica;
- outro profissional da escola.

Se for estudante, explique que o planejamento institucional deve ser validado por um professor ou responsável pedagógico.

### 2. Faça um diagnóstico progressivo

Pergunte apenas o que for necessário para a próxima decisão. Comece por:

1. Qual turma ou público participará?
2. Quantos estudantes?
3. Quanto tempo está disponível?
4. Qual objetivo curricular ou formativo?
5. Qual infraestrutura existe?
6. Quantos profissionais participarão?

Depois, aprofunde somente quando relevante:

- experiência com programação;
- disponibilidade de internet;
- número de computadores;
- acessibilidade;
- parceiros externos;
- necessidade de autorização de imagem;
- dados que serão coletados;
- formato de culminância;
- critérios de avaliação.

### 3. Classifique o nível de prontidão

Use uma das classificações:

| Nível | Situação | Recomendação |
|---|---|---|
| 🟢 Pronto para piloto | objetivo, turma, tempo e recursos mínimos definidos | criar plano de aplicação |
| 🟡 Requer ajustes | existem lacunas administráveis | propor ajustes e responsáveis |
| 🔴 Não iniciar ainda | há riscos críticos ou ausência de condições básicas | elaborar plano de preparação |

Nunca use a classificação como julgamento da escola. Ela serve apenas para orientar a preparação.

### 4. Recomende o formato

Escolha com justificativa:

| Formato | Uso recomendado |
|---|---|
| ⚡ Micro-Ideathon | primeiro piloto, poucas horas, protótipo conceitual |
| 🗓️ Oito encontros | uma etapa por encontro, progressão controlada |
| 📚 Projeto bimestral ou trimestral | formação técnica, desenvolvimento e avaliação aprofundada |
| 🏫 Programa institucional | várias turmas, áreas, parceiros e culminância ampliada |

Consulte `docs/formatos-de-aplicacao.md` antes de recomendar.

### 5. Produza o plano inicial

O plano deve conter:

- título da proposta;
- contexto;
- público participante;
- objetivo geral;
- objetivos de aprendizagem;
- formato recomendado;
- duração;
- etapas;
- responsabilidades;
- recursos;
- avaliação;
- acessibilidade e inclusão;
- segurança e privacidade;
- pontos de decisão da equipe pedagógica;
- riscos e respostas;
- próximos passos.

### 6. Explique as decisões

Depois do plano, inclua:

#### 🧠 Por que esta configuração foi recomendada?

Explique de três a cinco critérios utilizados, por exemplo:

- tempo disponível;
- maturidade técnica da turma;
- quantidade de equipamentos;
- objetivo curricular;
- capacidade de acompanhamento docente.

### 7. Indique evidência de conclusão

A skill só está concluída quando existir:

- plano inicial documentado;
- responsável por cada decisão pendente;
- formato de aplicação escolhido;
- ponto de validação com equipe pedagógica ou gestão;
- próxima ação com prazo ou encontro definido.

---

## 📄 Modelo de saída

```markdown
# 🚀 Plano Inicial do IPIT

**Autora da metodologia:** Sandra Maria Pereira  
**Escola:** [nome]  
**Turma:** [turma]  
**Responsável pela aplicação:** [nome]

## 🎯 Objetivo

[objetivo geral]

## 👥 Público

[público, quantidade e experiência]

## 🧭 Formato recomendado

[formato e justificativa]

## 🗓️ Cronograma inicial

| Momento | Atividade | Responsável | Evidência |
|---|---|---|---|
| 1 | [atividade] | [responsável] | [entregável] |

## 📊 Avaliação

[critérios e evidências]

## ♿ Inclusão e acessibilidade

[adaptações]

## 🔒 Segurança e privacidade

[medidas]

## 🏫 Pontos para validação da equipe pedagógica

- [decisão 1]
- [decisão 2]

## ⚠️ Riscos e respostas

| Risco | Impacto | Resposta |
|---|---|---|
| [risco] | [impacto] | [ação] |

## 🚀 Próximo passo

[ação concreta]
```

---

## 💬 Exemplo de interação

**Usuária:**

> Quero aplicar o IPIT com 30 estudantes, 10 computadores e quatro aulas.

**Agente:**

> 🧭 Para recomendar um formato coerente, preciso confirmar dois pontos:
>
> 1. As quatro aulas são consecutivas ou distribuídas?
> 2. O objetivo é construir software funcional ou um protótipo de baixa fidelidade?
>
> Com 10 computadores para 30 estudantes, a tendência é trabalhar com rodízios entre investigação, prototipação em papel, documentação e desenvolvimento.

---

## ✅ Critérios de qualidade

Uma boa saída desta skill:

- não pressupõe recursos inexistentes;
- não obriga o uso de programação;
- relaciona atividades aos objetivos curriculares;
- inclui a equipe pedagógica nas decisões institucionais;
- oferece alternativas para pouca infraestrutura;
- define evidências avaliáveis;
- preserva autoria docente e estudantil;
- registra a autoria de Sandra Maria Pereira.

---

## ⚠️ Tratamento de situações críticas

Interrompa o planejamento e sinalize necessidade de validação quando houver:

- intenção de publicar dados pessoais de estudantes;
- uso de imagem sem autorização;
- coleta de dados sensíveis;
- participação externa sem definição de responsabilidade;
- uso de ferramentas com idade mínima incompatível;
- avaliação automatizada sem revisão docente;
- ausência de supervisão adequada.

---

## 🛠️ Solução de problemas

### O usuário não sabe responder às perguntas

Ofereça opções e exemplos. Não invente informações.

### A escola tem poucos equipamentos

Proponha rodízio, prototipação em papel, atividades desplugadas e trabalho por estações.

### O tempo é muito curto

Recomende Micro-Ideathon e reduza o produto esperado para problema definido, proposta de valor e protótipo conceitual.

### A equipe pedagógica ainda não aprovou

Gere uma proposta preliminar identificada como “para validação”, com decisões pendentes claramente marcadas.

---

## ⚡ Notas de desempenho

- Faça no máximo três perguntas por rodada.
- Reutilize informações já fornecidas.
- Não repita o diagnóstico inteiro em cada resposta.
- Apresente primeiro a decisão principal e depois a justificativa.
- Mantenha as recomendações executáveis no contexto escolar.
