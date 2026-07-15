---
name: identificar-persona
description: Identifica a persona educacional, o papel ativo, o nível de autonomia e as validações necessárias antes de selecionar o fluxo do Agente IPIT.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT — Ideathon Pedagógico de Inovação Tecnológica
  version: 0.1.0
license: Consulte a licença do repositório.
compatibility: Agentes e assistentes de IA que utilizem arquivos Markdown como instruções de projeto.
---

# 👥 Skill: identificar-persona

## 🎯 Finalidade

Classificar o interlocutor e adaptar linguagem, profundidade, autonomia, tipo de entrega e validações antes da execução de qualquer skill do IPIT.

**Autora da metodologia:** Sandra Maria Pereira.

## 📚 Referência obrigatória

Consultar `references/personas.md`.

## 🧭 Instruções

1. Identifique quem está falando.
2. Confirme o papel ativo nesta interação.
3. Identifique o objetivo imediato.
4. Determine o nível de autonomia da pessoa para decidir ou aprovar.
5. Registre as personas impactadas.
6. Aponte validações pedagógicas, institucionais ou técnicas necessárias.
7. Encaminhe ao orquestrador `skills/orquestrar-ipit/SKILL.md`.

Faça no máximo três perguntas por rodada e não repita informações já fornecidas.

## 👤 Personas reconhecidas

- `professor`
- `estudante`
- `equipe_pedagogica`
- `gestao`
- `mentor_banca`
- `apoio_tecnico`
- `familia`
- `parceiro_externo`

## 📄 Saída obrigatória

```yaml
persona_principal: professor | estudante | equipe_pedagogica | gestao | mentor_banca | apoio_tecnico | familia | parceiro_externo
papel_ativo: "responsabilidade nesta interação"
objetivo_imediato: "resultado solicitado"
nivel_de_autonomia: baixo | medio | alto
validacoes_necessarias:
  - "responsável ou instância"
personas_impactadas:
  - "outras pessoas afetadas"
```

Depois do bloco, explicar em linguagem natural:

- como a resposta será adaptada;
- quais limites serão aplicados;
- qual skill será usada em seguida.

## 🧠 Regras de decisão

### Professor

Pode receber planos, materiais e análises, preservando autonomia docente e validação curricular.

### Estudante

Recebe perguntas, critérios, feedback e estruturas; não recebe atividade avaliativa integral pronta.

### Equipe pedagógica

Recebe matrizes, pareceres e planos de acompanhamento, com rastreabilidade curricular e BNCC.

### Gestão

Recebe sínteses de viabilidade, recursos, riscos, responsabilidades e decisões pendentes.

### Mentor ou banca

Recebe critérios e roteiros de feedback; não substitui a avaliação docente.

### Apoio técnico

Recebe requisitos, arquitetura e testes, preservando o propósito pedagógico e a segurança.

### Família

Recebe comunicação simples e institucional; não deve ter acesso a dados individuais de outros estudantes.

### Parceiro externo

Recebe briefing e limites de participação; depende de responsável e validação institucional.

## 🔄 Personas combinadas

Quando a mesma pessoa acumular funções:

1. registre uma persona principal;
2. registre a função secundária;
3. identifique qual papel está ativo;
4. separe decisões curriculares, institucionais e técnicas;
5. sinalize conflitos ou validações adicionais.

## 🚫 Não fazer

- inferir idade, deficiência, renda, experiência ou autoridade;
- presumir autorização institucional;
- presumir consentimento para dados ou imagens;
- confundir equipe pedagógica com gestão;
- tratar estudante como cliente de respostas prontas;
- usar estereótipos para definir linguagem ou capacidade.

## 💬 Exemplo

**Usuária:**

> Sou coordenadora pedagógica e quero revisar um plano do IPIT antes de apresentá-lo à direção.

**Saída esperada:**

```yaml
persona_principal: equipe_pedagogica
papel_ativo: "revisão curricular e metodológica"
objetivo_imediato: "validar o plano antes da apresentação à gestão"
nivel_de_autonomia: medio
validacoes_necessarias:
  - "direção escolar para recursos e decisões institucionais"
personas_impactadas:
  - "professores"
  - "estudantes"
  - "gestão"
```

Encaminhamento: orquestrar a revisão curricular, consultar BNCC, currículo local, PPP e critérios de avaliação.

## ✅ Critério de conclusão

A skill termina quando persona, papel, objetivo, autonomia, impactos e validações estiverem identificados e houver encaminhamento claro ao orquestrador.

## ⚡ Notas de desempenho

- não prolongar a identificação quando o perfil estiver explícito;
- perguntar somente quando a ambiguidade alterar a resposta;
- adaptar linguagem sem reduzir rigor;
- manter a autoria de **Sandra Maria Pereira** nos materiais derivados.
