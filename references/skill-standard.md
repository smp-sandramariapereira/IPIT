# Padrão Oficial de Skills do Agente IPIT

Este documento define o formato oficial das skills do Agente IPIT. Ele foi escrito a partir da leitura das skills existentes e do modelo de validação esperado por harness-skills: frontmatter previsível, seções com títulos exatos e instruções curtas, verificáveis e orientadas a evidências.

## Estrutura de diretórios

Toda skill deve viver em um diretório próprio dentro de `skills/`, no formato:

```text
skills/
  nome-da-skill/
    SKILL.md
```

Regras obrigatórias:

- o nome da pasta deve estar em kebab-case;
- o arquivo principal deve se chamar obrigatoriamente `SKILL.md`;
- não deve existir `README.md` dentro da pasta da skill;
- arquivos auxiliares só podem existir se forem citados explicitamente no `SKILL.md`;
- a skill deve ser independente do restante do conteúdo, sem depender de arquivos ocultos.

## Frontmatter base

Toda skill deve começar com frontmatter YAML válido. O bloco abaixo é o modelo oficial mínimo:

```yaml
---
name: nome-da-skill
description: >
  Descrição objetiva. Use when...
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.0.0
  mcp-server: none
  personas:
    - professor
  ipit-stage: preparacao
  requires-human-review: true
  depends-on: []
  required-evidence: []
  produces: []
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compatíveis com Markdown
---
```

Campos obrigatórios:

- `name`: usa kebab-case e deve refletir o nome da pasta;
- `description`: descreve a intenção principal e inclui frases de ativação;
- `metadata.author`: autor ou autoria responsável;
- `metadata.methodology`: sempre `IPIT`;
- `metadata.version`: usa SemVer;
- `metadata.mcp-server`: informe `none` quando a skill não depender de MCP;
- `metadata.personas`: lista das personas atendidas;
- `metadata.ipit-stage`: etapa principal do IPIT;
- `metadata.requires-human-review`: `true` ou `false`;
- `metadata.depends-on`: lista de dependências;
- `metadata.required-evidence`: lista de evidências necessárias para concluir a tarefa;
- `metadata.produces`: lista de evidências produzidas pela skill;
- `license`: deve apontar para a licença do repositório;
- `compatibility`: ambientes ou agentes compatíveis.

## Versionamento

Toda skill deve seguir SemVer no campo `metadata.version`:

- `MAJOR` quando a interface, o escopo ou a validação mudarem de forma incompatível;
- `MINOR` quando houver nova capacidade, nova etapa ou novo comportamento retrocompatível;
- `PATCH` quando houver ajuste de texto, clareza, exemplo ou correção sem mudar a intenção.

## Instructions — Instruções

Esta é a seção principal de comportamento da skill. Deve conter:

- finalidade explícita;
- intenções atendidas;
- frases de ativação reconhecíveis;
- regras de escopo;
- dependências operacionais;
- requisitos de revisão humana, quando houver;
- critério mínimo para responder ou recusar.

Regras de escrita:

- use frases curtas e objetivas;
- prefira verbos de ação;
- cada regra deve ser testável;
- não misture instruções com justificativas longas;
- quando houver conflito, a regra da skill deve ser inequívoca.

## Inputs — Entradas

Declare tudo o que a skill precisa receber para funcionar bem:

- contexto mínimo do usuário;
- tipo de solicitação;
- dados obrigatórios;
- dados opcionais;
- pressupostos aceitáveis;
- limites de escopo.

Cada entrada deve indicar se a ausência gera erro bloqueante ou aviso não bloqueante.

## Outputs — Saídas

Declare tudo o que a skill deve produzir:

- formato da resposta;
- artefatos, listas, tabelas ou planos;
- evidências produzidas;
- próximos passos sugeridos, quando apropriado;
- limites do que não deve ser prometido.

As saídas devem ser verificáveis e compatíveis com o objetivo da skill.

## BNCC Alignment — Alinhamento à BNCC

Toda skill voltada para conteúdo, prática pedagógica ou planejamento deve registrar:

- relação com a BNCC quando houver confirmação;
- ausência de código BNCC quando não houver validação;
- a fórmula padrão `a validar pela equipe pedagogica` sempre que a habilidade ainda não estiver confirmada;
- adequação ao currículo local, ao PPP e ao contexto escolar, quando relevante.

Não é permitido inventar códigos da BNCC.

## Safety and Pedagogy — Segurança e pedagogia

Esta seção cobre segurança, privacidade e responsabilidade pedagógica.

Deve declarar:

- dados que não podem ser coletados ou publicados;
- limites para uso de IA e automação;
- necessidade de supervisão humana;
- cuidados com estudantes, famílias e equipe escolar;
- riscos previsíveis e como reduzi-los;
- acessibilidade e inclusão.

Regras mínimas:

- não solicitar ou expor dados pessoais desnecessários;
- não recomendar publicação de credenciais, tokens ou segredos;
- não tratar conteúdo sintetizado como evidência real;
- manter a linguagem pedagogicamente responsável.

## Examples — Exemplos

As skills devem incluir exemplos quando isso ajudar a reduzir ambiguidade.

Padrão para exemplos:

- um exemplo simples e direto por comportamento principal;
- se houver variação, mostrar apenas o suficiente para validar a leitura;
- usar exemplos reais ou plausíveis, sem excesso de volume;
- nunca substituir a instrução principal por um exemplo;
- manter o exemplo alinhado com a finalidade da skill.

Limite recomendado:

- o corpo total da skill deve ficar, em geral, abaixo de 500 palavras;
- skills mais complexas podem ir além disso, mas apenas quando a precisão exigir;
- exemplos devem ser curtos e pontuais.

## Performance Notes — Notas de desempenho

Esta seção define como a skill deve se comportar sob validação automatizada e uso real.

Deve incluir:

- eficiência de resposta;
- ordem de prioridades;
- dependências que precisam ser carregadas primeiro;
- sinais de que a skill recebeu contexto insuficiente;
- comportamento esperado quando a entrada estiver incompleta.

Se a skill precisar ser curta para funcionar melhor, isso deve ser declarado aqui.

## Troubleshooting — Solução de problemas

Esta seção deve orientar o que fazer quando a execução não seguir o esperado.

Inclua:

- erros bloqueantes mais prováveis;
- avisos não bloqueantes mais prováveis;
- como corrigir entradas faltantes;
- quando pedir revisão humana;
- quando recusar a continuidade.

Definições:

- erro bloqueante: impede a skill de concluir com segurança, precisão ou conformidade. Ex.: falta de informação essencial, conflito de escopo, risco pedagógico alto, ou dependência obrigatória ausente;
- aviso não bloqueante: não impede a entrega, mas reduz a confiança ou a completude. Ex.: contexto parcial, dependência opcional ausente, ou necessidade de confirmação posterior.

## Critérios de conclusão

Toda skill deve declarar, de forma objetiva, o que significa concluir com sucesso. Os critérios precisam ser observáveis e ligados ao resultado esperado.

Se a skill não puder concluir sem validação externa, isso deve estar explicitado no frontmatter e nesta seção.

## Política de atualização

Atualizações em skills devem seguir estas regras:

- ajuste de texto sem alterar comportamento: `PATCH`;
- nova capacidade compatível: `MINOR`;
- quebra de contrato, mudança de estrutura ou remoção de comportamento: `MAJOR`;
- toda atualização relevante deve revisar entradas, saídas, evidências e riscos;
- se a mudança afetar educação, segurança ou privacidade, marcar revisão humana.

## Checklist de conformidade

A skill está conforme quando atende a todos os itens abaixo:

- diretório em kebab-case;
- arquivo principal nomeado `SKILL.md`;
- sem `README.md` na pasta da skill;
- frontmatter YAML presente e válido;
- `metadata.version` em SemVer;
- `metadata.author` declarado;
- `metadata.personas` declarado;
- `metadata.ipit-stage` declarado;
- `description` com intenção e ativação;
- `metadata.depends-on` declarado;
- `metadata.required-evidence` declarado;
- `metadata.produces` declarado;
- seções obrigatórias presentes;
- alinhamento BNCC tratado corretamente;
- segurança, privacidade e pedagogia explicitadas;
- critérios de conclusão definidos;
- exemplos curtos e coerentes;
- política de atualização registrada;
- distinção clara entre erro bloqueante e aviso não bloqueante.

## Modelo de leitura para validação

O validador deve conseguir encontrar, no mínimo, estes sinais:

- um frontmatter com as chaves principais;
- os títulos exatos das seções obrigatórias;
- instruções curtas e acionáveis;
- referência a evidências, segurança e BNCC quando aplicável;
- critério de conclusão observável.

Se um desses sinais faltar, a skill deve ser tratada como incompleta.