---
name: iniciar-ideathon
description: Diagnostica o contexto escolar e cria o plano inicial de aplicação do IPIT com alinhamento à BNCC, ao currículo local e à validação da equipe pedagógica.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT — Ideathon Pedagógico de Inovação Tecnológica
  version: 0.2.0
license: Consulte a licença do repositório.
compatibility: Agentes e assistentes de IA que utilizem arquivos Markdown como instruções de projeto.
---

# 🚀 Skill: iniciar-ideathon

## 🎯 Finalidade

Orientar professor, equipe pedagógica ou gestão escolar na definição do primeiro plano de aplicação do IPIT.

A skill transforma uma intenção inicial em uma proposta coerente com:

- BNCC;
- currículo da rede e da escola;
- Projeto Político-Pedagógico, quando aplicável;
- objetivos de aprendizagem;
- perfil dos estudantes;
- tempo e infraestrutura;
- avaliação por evidências;
- segurança, privacidade, inclusão e acessibilidade;
- validação da equipe pedagógica.

**Autora da metodologia:** Sandra Maria Pereira.

---

## 👥 Quando usar

Use quando o usuário quiser:

- começar uma aplicação do IPIT;
- escolher o formato adequado;
- montar cronograma e plano inicial;
- apresentar a proposta à equipe pedagógica;
- verificar alinhamento curricular e viabilidade;
- adaptar a metodologia às condições da escola.

Não use para conduzir uma etapa específica já iniciada.

---

## 🧭 Instruções

### 1. Identifique o perfil

Confirme se o interlocutor é professor, coordenador pedagógico, gestor, equipe técnica ou outro profissional.

Se for estudante, informe que o planejamento curricular e institucional precisa de validação docente.

### 2. Faça diagnóstico progressivo

Comece por no máximo três perguntas:

1. Qual etapa de ensino, ano/série, modalidade e turma participarão?
2. Quais áreas, componentes ou objetivos curriculares a escola pretende trabalhar?
3. Quanto tempo e quais recursos estão disponíveis?

Depois, aprofunde conforme necessário:

- número de estudantes;
- competências e habilidades já previstas no planejamento;
- códigos BNCC fornecidos pela escola;
- currículo da rede e PPP;
- experiência técnica;
- internet e equipamentos;
- acessibilidade;
- professores e parceiros;
- avaliação;
- culminância;
- dados, imagem e privacidade.

### 3. Faça o alinhamento curricular

Consulte `references/alinhamento-bncc.md`.

O agente deve:

1. identificar objetivos de aprendizagem;
2. selecionar apenas competências gerais realmente mobilizadas;
3. identificar área e componente curricular;
4. usar códigos BNCC somente quando fornecidos ou verificados;
5. escrever **“a validar pela equipe pedagógica”** quando o código não estiver confirmado;
6. definir uma evidência observável para cada objetivo;
7. relacionar a evidência a um critério de avaliação.

Nunca invente códigos BNCC.

### 4. Classifique a prontidão

| Nível | Situação | Recomendação |
|---|---|---|
| 🟢 Pronto para piloto | turma, objetivo, alinhamento inicial, tempo e recursos mínimos definidos | criar plano de aplicação |
| 🟡 Requer ajustes | há lacunas curriculares, operacionais ou institucionais administráveis | propor ajustes e responsáveis |
| 🔴 Não iniciar ainda | riscos críticos ou ausência de condições básicas | elaborar plano de preparação |

A classificação não é julgamento da escola.

### 5. Recomende o formato

| Formato | Uso recomendado |
|---|---|
| ⚡ Micro-Ideathon | piloto curto e protótipo conceitual |
| 🗓️ Oito encontros | uma etapa por encontro |
| 📚 Projeto bimestral ou trimestral | integração curricular e desenvolvimento aprofundado |
| 🏫 Programa institucional | várias turmas, áreas e parceiros |

Consulte `docs/formatos-de-aplicacao.md`.

### 6. Produza o plano inicial

Inclua obrigatoriamente:

- título e contexto;
- etapa de ensino, turma e modalidade;
- áreas e componentes envolvidos;
- objetivo geral;
- objetivos de aprendizagem;
- competências gerais selecionadas e justificadas;
- habilidades BNCC confirmadas ou marcadas para validação;
- articulação com currículo local e PPP;
- formato e duração;
- cronograma;
- responsabilidades;
- recursos;
- inclusão e acessibilidade;
- avaliação por evidências;
- segurança e privacidade;
- riscos;
- pontos de validação da equipe pedagógica;
- próximos passos.

### 7. Explique as decisões

Após o plano, explique de três a cinco critérios usados, como:

- aprendizagem pretendida;
- coerência com a BNCC e currículo local;
- tempo;
- maturidade da turma;
- equipamentos;
- capacidade de acompanhamento docente.

### 8. Evidência de conclusão

A skill termina quando houver:

- plano documentado;
- matriz curricular inicial;
- formato escolhido;
- responsáveis por pendências;
- validação pedagógica prevista;
- próxima ação definida.

---

## 📄 Modelo de saída

```markdown
# 🚀 Plano Inicial do IPIT

**Autora da metodologia:** Sandra Maria Pereira  
**Escola:** [nome]  
**Etapa/ano/série:** [informação]  
**Turma:** [turma]  
**Responsável:** [nome]

## 🎯 Objetivo geral

[objetivo]

## 🇧🇷 Alinhamento à BNCC e ao currículo

| Etapa/atividade | Objetivo de aprendizagem | Competência geral | Área/componente | Habilidade BNCC | Evidência | Avaliação |
|---|---|---|---|---|---|---|
| [atividade] | [objetivo] | [competência] | [área] | [código confirmado ou “a validar”] | [entregável] | [critério] |

## 🧭 Formato recomendado

[formato e justificativa]

## 🗓️ Cronograma

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

- [competências e habilidades]
- [cronograma]
- [avaliação]
- [autorizações e recursos]

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

> 🧭 Para estruturar uma proposta curricularmente coerente, preciso confirmar três pontos:
>
> 1. Qual é o ano/série e a modalidade da turma?
> 2. Quais componentes ou objetivos de aprendizagem devem ser integrados?
> 3. As quatro aulas são consecutivas ou distribuídas?
>
> Não atribuirei códigos BNCC sem confirmação. Quando necessário, prepararei uma matriz inicial para validação da equipe pedagógica.

---

## ✅ Critérios de qualidade

Uma boa saída:

- não pressupõe recursos inexistentes;
- não inventa códigos BNCC;
- conecta atividade, aprendizagem, evidência e avaliação;
- diferencia BNCC, currículo local e objetivos da Educação Profissional;
- inclui a equipe pedagógica;
- oferece alternativas para pouca infraestrutura;
- preserva autoria docente e estudantil;
- registra a autoria de Sandra Maria Pereira.

---

## ⚠️ Situações críticas

Interrompa e solicite validação quando houver:

- código BNCC não verificado apresentado como definitivo;
- ausência de objetivo de aprendizagem;
- publicação de dados ou imagens sem autorização;
- coleta de dados sensíveis;
- ferramenta com idade mínima incompatível;
- avaliação automatizada sem revisão docente;
- ausência de supervisão;
- conflito com currículo, PPP ou normas da escola.

---

## 🛠️ Solução de problemas

### A escola ainda não definiu habilidades

Crie objetivos em linguagem pedagógica, selecione competências gerais pertinentes e marque os códigos como **“a validar pela equipe pedagógica”**.

### Poucos equipamentos

Proponha rodízio, prototipação em papel, atividades desplugadas e estações.

### Tempo curto

Recomende Micro-Ideathon com escopo reduzido.

### Proposta ainda não aprovada

Gere documento preliminar identificado como **“para validação”**.

---

## ⚡ Notas de desempenho

- Faça no máximo três perguntas por rodada.
- Reutilize informações existentes.
- Apresente primeiro a decisão principal.
- Não liste todas as competências gerais automaticamente.
- Mantenha as recomendações executáveis no contexto escolar.