---
name: preparar-pitch
description: >
  Preparar o pitch final do projeto IPIT com narrativa objetiva, demonstração
  tecnicamente honesta e evidências de aprendizagem. Use when o desenvolvimento
  do MVP estiver concluído ou suficientemente estável para apresentação.
metadata:
  author: Sandra Maria Pereira
  methodology: IPIT
  version: 1.2.0
  mcp-server: none
  personas:
    - professor
    - estudante
    - equipe-pedagogica
    - gestao
  ipit-stage: finalizacao
  requires-human-review: true
  depends-on:
    - acompanhar-desenvolvimento
  required-evidence:
    - mvp-executavel
    - evidencias-de-testes
    - limitacoes-conhecidas
    - registro-de-uso-de-ia
    - documentacao-atualizada
  produces:
    - roteiro-de-pitch
    - apresentacao
    - plano-de-demonstracao
    - respostas-para-banca
    - retrospectiva
    - proximos-passos
license: repository-license
compatibility: GitHub Copilot, Codex e agentes compativeis com Markdown
---

# Preparar Pitch

## Purpose — Finalidade

Transformar as evidências do projeto em uma apresentação curta, clara e verificável, sem exagerar resultados, ocultar limitações ou substituir a autoria da equipe.

## Use When — Quando usar

Use esta skill quando:

- o MVP estiver concluído ou estável para demonstração;
- a equipe precisar apresentar problema, solução, processo e resultados;
- houver banca, mostra, reunião pedagógica ou apresentação institucional.

Trigger phrases:

- "precisamos montar o pitch";
- "vamos apresentar o projeto";
- "como demonstrar o MVP";
- "prepare a apresentação final".

## Instructions — Instruções

1. Declarar a skill utilizada: `preparar-pitch`.
2. Confirmar a conclusão de `acompanhar-desenvolvimento`.
3. Identificar público, tempo disponível e critérios da apresentação.
4. Estruturar a narrativa em problema, evidências, público afetado, solução, demonstração, resultados, limitações e próximos passos.
5. Selecionar apenas evidências verificáveis.
6. Preparar demonstração do fluxo principal do MVP ou alternativa tecnicamente honesta quando a execução ao vivo não for viável.
7. Explicar arquitetura e tecnologias em linguagem adequada ao público.
8. Declarar uso de IA, validação humana e limites de confiança.
9. Prever acessibilidade visual, textual e oral.
10. Preparar respostas para perguntas prováveis da banca.
11. Ensaiar e ajustar a duração para 3 a 5 minutos, salvo regra institucional diferente.
12. Encerrar com próximo passo realista e responsável definido.

## Inputs — Entradas

### Obrigatórias

- MVP executável e seu estado real;
- evidências de testes e validação;
- limitações conhecidas;
- público da apresentação;
- tempo disponível.

### Opcionais

- critérios da banca;
- identidade visual institucional;
- contexto BNCC, currículo local e PPP;
- autorização para uso de imagens e depoimentos.

Quando a demonstração ao vivo não for viável, preparar uma alternativa tecnicamente honesta baseada no MVP e declarar explicitamente a limitação. A ausência de evidências verificáveis é bloqueante.

## Outputs — Saídas

A skill deve produzir:

- roteiro de pitch;
- estrutura de apresentação;
- plano de demonstração;
- lista de evidências utilizadas;
- respostas para perguntas prováveis;
- retrospectiva do processo;
- limitações declaradas;
- próximos passos priorizados.

## Dependencies — Dependências

Esta skill depende de:

- `skills/acompanhar-desenvolvimento/SKILL.md`.

Não avançar sem evidências do desenvolvimento e estado real do MVP.

## BNCC Alignment — Alinhamento à BNCC

- Não inventar códigos BNCC.
- Quando não houver habilidade confirmada, registrar: `a validar pela equipe pedagogica`.
- Relacionar evidências da apresentação ao currículo local, ao PPP e à avaliação processual quando aplicável.
- Não apresentar alinhamento curricular como definitivo sem validação humana registrada.

## Safety and Pedagogy — Segurança e pedagogia

- Não expor dados pessoais, imagens não autorizadas, credenciais ou segredos.
- Usar dados fictícios, anonimizados ou agregados na demonstração.
- Não prometer funcionalidades, impactos ou resultados sem evidência.
- Preservar autoria estudantil e autoria metodológica de Sandra Maria Pereira.
- Não permitir que IA produza ou apresente evidências inexistentes.
- Aplicar `guardrails/policy.yaml` em toda entrada e saída.
- Garantir linguagem inclusiva e recursos de acessibilidade.

## Human Review — Revisão humana

Revisão obrigatória por professor e, quando houver impacto institucional, pela equipe pedagógica ou gestão.

A revisão deve confirmar:

- fidelidade das evidências;
- ausência de dados sensíveis;
- autoria e créditos;
- adequação curricular;
- acessibilidade;
- coerência entre demonstração e estado real do MVP.

## Completion Criteria — Critérios de conclusão

A skill está concluída quando:

- o roteiro estiver estruturado;
- a apresentação estiver adequada ao público e ao tempo;
- a demonstração estiver preparada;
- resultados e limitações estiverem documentados;
- o uso de IA estiver declarado;
- perguntas prováveis tiverem respostas preparadas;
- acessibilidade e revisão humana estiverem registradas;
- próximos passos estiverem definidos.

## Examples — Exemplos

### Caso adequado

"O MVP executa o fluxo principal, possui 12 testes registrados, duas limitações conhecidas e plano de continuidade em três frentes."

### Caso ambíguo

Quando o MVP estiver parcialmente funcional, apresentar somente o fluxo executável e usar protótipo, vídeo curto ou sequência de telas para contextualizar as partes pendentes, deixando claro o que ainda não foi implementado.

### Caso bloqueante

Não criar métricas, depoimentos, resultados ou funcionalidades inexistentes apenas para fortalecer a apresentação.

## Performance Notes — Notas de desempenho

- Priorizar problema, evidência, demonstração, resultados, limites e próximos passos.
- Evitar excesso de texto nos slides.
- Usar uma evidência principal por afirmação relevante.
- Reduzir detalhes secundários quando o tempo exceder o limite.
- Não repetir toda a documentação técnica durante o pitch.

## Troubleshooting — Solução de problemas

### Ausência de demonstração ao vivo

Preparar alternativa tecnicamente honesta com protótipo, vídeo curto ou sequência de telas, vinculada ao estado real do MVP e declarando a limitação.

### Falta de evidências

Interromper a finalização e retornar para `acompanhar-desenvolvimento`.

### Roteiro muito longo

Remover detalhes secundários e preservar problema, evidências, demonstração, resultados e limitações.

### Dados ou imagens sem autorização

Bloquear o uso e substituir por conteúdo fictício, anonimizado ou autorizado.

## Política de atualização

- PATCH: ajustes textuais sem mudança de comportamento.
- MINOR: novo requisito de apresentação compatível com o fluxo atual.
- MAJOR: alteração de dependência, formato obrigatório ou critério de conclusão.

## Authorship — Autoria

**Sandra Maria Pereira**  
Criadora e autora do IPIT — Ideathon Pedagógico de Inovação Tecnológica.
