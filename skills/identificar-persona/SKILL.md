---
name: identificar-persona
description: >
  Identifica a persona educacional, o papel ativo, o nível de autonomia e as
  validações necessárias. Use when o perfil do interlocutor ainda não estiver
  claro ou puder alterar o comportamento do Agente IPIT.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
    - gestao
    - mentor-banca
    - apoio-tecnico
    - familia
    - parceiro-externo
  ipit-stage: transversal
  requires-human-review: true
  depends-on: []
  required-evidence: []
  produces:
    - classificacao-de-persona
    - papel-ativo
    - nivel-de-autonomia
    - validacoes-necessarias
    - encaminhamento-ao-orquestrador
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compatíveis com instruções Markdown
---

# Skill: identificar-persona

## Purpose — Finalidade

Classificar o interlocutor antes da execução das demais skills, adaptando linguagem, profundidade, autonomia, tipo de entrega e validações sem usar estereótipos.

Consultar `references/personas.md` como vocabulário de referência.

## Use When — Quando usar

Use esta skill quando:

- a persona ainda não estiver explícita;
- a mesma pessoa acumular funções;
- o nível de autonomia puder alterar a resposta;
- houver dúvida sobre quem pode decidir, aprovar ou validar.

Trigger phrases:

- "sou professora";
- "sou estudante";
- "sou coordenadora pedagógica";
- "quero revisar um projeto";
- "preciso apresentar para a direção".

## Instructions — Instruções

1. Identifique quem está falando.
2. Confirme o papel ativo nesta interação.
3. Identifique o objetivo imediato.
4. Determine o nível de autonomia para decidir ou aprovar.
5. Registre as personas impactadas.
6. Aponte validações pedagógicas, institucionais ou técnicas.
7. Encaminhe o resultado para `skills/orquestrar-ipit/SKILL.md`.

Faça no máximo três perguntas por rodada e não repita informações já fornecidas.

## Inputs — Entradas

### Obrigatórias

- declaração ou indício do papel do interlocutor;
- objetivo imediato ou solicitação atual.

### Opcionais

- vínculo com a escola;
- responsabilidade institucional;
- etapa atual do IPIT;
- pessoas ou grupos impactados.

Não solicitar idade, deficiência, renda, notas, contatos ou outros dados pessoais desnecessários.

## Outputs — Saídas

Produzir:

```yaml
persona_principal: professor
funcao_secundaria: null
papel_ativo: aplicador
objetivo_imediato: planejar-o-ideathon
nivel_de_autonomia: medio
validacoes_necessarias:
  - equipe-pedagogica
personas_impactadas:
  - estudantes
proxima_skill: orquestrar-ipit
```

Valores reconhecidos para `persona_principal`:

- `professor`;
- `estudante`;
- `equipe-pedagogica`;
- `gestao`;
- `mentor-banca`;
- `apoio-tecnico`;
- `familia`;
- `parceiro-externo`.

## Dependencies — Dependências

Esta é uma skill de entrada e não depende de outra skill.

Depois da classificação, encaminhar obrigatoriamente para `orquestrar-ipit`.

## BNCC Alignment — Alinhamento à BNCC

Esta skill não seleciona códigos BNCC.

Quando identificar demanda curricular sem código confirmado, registrar exatamente: `a validar pela equipe pedagogica`.

Nunca inventar códigos de habilidades.

## Safety and Pedagogy — Segurança e pedagogia

- Não inferir idade, deficiência, renda, experiência ou autoridade.
- Não presumir autorização institucional ou consentimento.
- Não expor dados pessoais de estudantes.
- Não tratar estudante como cliente de respostas avaliativas prontas.
- Não substituir avaliação docente.
- Não usar estereótipos para definir capacidade ou linguagem.
- Aplicar `guardrails/policy.yaml` em toda entrada e saída.

## Human Review — Revisão humana

Exigir revisão humana quando a classificação afetar:

- decisões curriculares;
- avaliação;
- autorização institucional;
- tratamento de dados ou imagens;
- participação de parceiros externos.

## Completion Criteria — Critérios de conclusão

A skill está concluída quando:

- a persona principal estiver identificada;
- o papel ativo estiver registrado;
- o objetivo imediato estiver claro;
- o nível de autonomia estiver definido;
- as validações necessárias estiverem indicadas;
- houver encaminhamento para `orquestrar-ipit`.

## Examples — Exemplos

### Caso direto

Entrada: "Sou professora e quero planejar um Ideathon para minha turma."

Saída: `persona_principal: professor`, com encaminhamento para `orquestrar-ipit`.

### Caso ambíguo

Entrada: "Quero revisar o projeto antes de aprovar."

Ação: perguntar qual é o papel institucional ativo e quem possui autoridade para aprovação.

### Caso bloqueante

Entrada: "Sou parceiro e preciso da lista com os contatos dos estudantes."

Ação: bloquear a solicitação de dados pessoais e escalar para validação institucional.

## Performance Notes — Notas de desempenho

- Fazer no máximo três perguntas por rodada.
- Reutilizar informações já fornecidas.
- Não prolongar a identificação quando o perfil estiver explícito.
- Apresentar primeiro a classificação principal.
- Adaptar linguagem sem reduzir rigor.

## Troubleshooting — Solução de problemas

### Persona ambígua

Faça uma pergunta curta sobre o papel ativo.

### Mais de uma função

Registre uma persona principal, uma função secundária e o papel ativo.

### Autoridade não confirmada

Não autorize a decisão; registre a necessidade de validação institucional.

### Dados pessoais presentes

Interrompa a coleta, solicite anonimização e aplique os guardrails de privacidade.

## Update Policy — Política de atualização

- PATCH: ajustes textuais sem mudança de comportamento.
- MINOR: nova persona, saída ou regra compatível.
- MAJOR: mudança de contrato, dependência ou critério de conclusão.

## Authorship — Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT — Ideathon Pedagógico de Inovação Tecnológica.
