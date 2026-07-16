# Auditoria Completa do Agente Conversacional IPIT

Data da auditoria: 2026-07-16  
Escopo analisado: AGENTS, instrucoes do Copilot, todas as skills, catalogo, referencias, scripts, workflows, testes, politicas e README.

## Metodo e evidencias de execucao

Validadores e testes executados antes da conclusao:

```bash
python scripts/validate-guardrails.py
pytest -q
```

Resultado observado:

```text
OK: politica de guardrails valida
Total de regras: 16
Niveis: info=1, warning=1, block=11, escalate=3
37 passed in 0.07s
```

Evidencias base:

- Governanca do agente: [AGENTS.md](AGENTS.md#L7), [AGENTS.md](AGENTS.md#L18), [AGENTS.md](AGENTS.md#L35)
- Instrucoes obrigatorias do agente: [.github/copilot-instructions.md](.github/copilot-instructions.md#L7)
- Politica formal de guardrails: [guardrails/policy.yaml](guardrails/policy.yaml#L1)
- Script de validacao: [scripts/validate-guardrails.py](scripts/validate-guardrails.py#L101)
- Catalogo e cadeia de dependencias: [skills/catalog.yaml](skills/catalog.yaml#L4)
- Skills em formato estruturado: [skills/iniciar-ideathon/SKILL.md](skills/iniciar-ideathon/SKILL.md#L1), [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L1), [skills/planejar-arquitetura/SKILL.md](skills/planejar-arquitetura/SKILL.md#L1), [skills/acompanhar-desenvolvimento/SKILL.md](skills/acompanhar-desenvolvimento/SKILL.md#L1), [skills/preparar-pitch/SKILL.md](skills/preparar-pitch/SKILL.md#L1)
- Teste novo de consistencia de dependencias: [tests/test-dependencies.py](tests/test-dependencies.py#L87)
- CI com teste de dependencias: [.github/workflows/validate-agent.yml](.github/workflows/validate-agent.yml#L25)

## Matriz de avaliacao (1 a 4)

Classificacao usada:
- 1: insuficiente
- 2: parcial
- 3: adequada para piloto
- 4: consistente para uso controlado

| Dimensao | Nota | Justificativa objetiva | Evidencias |
|---|---:|---|---|
| Arquitetura | 3 | Arquitetura em camadas esta definida e coerente com regras de governanca e fluxo geral do agente. | [README.md](README.md#L23), [AGENTS.md](AGENTS.md#L35) |
| Qualidade das skills | 3 | Todas as skills estao no formato estruturado com secoes obrigatorias; existe risco tecnico por uso de tab no frontmatter de uma skill. | [skills/iniciar-ideathon/SKILL.md](skills/iniciar-ideathon/SKILL.md#L1), [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L1), [references/skill-standard.md](references/skill-standard.md#L23) |
| Personas | 3 | Cobertura de personas esta ampla em fixtures e testes de roteamento. | [README.md](README.md#L42), [tests/test-routing.py](tests/test-routing.py#L52) |
| Orquestracao | 3 | Cadeia de dependencias foi fechada e ganhou teste de consistencia entre catalogo e frontmatter. | [skills/catalog.yaml](skills/catalog.yaml#L12), [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L58), [tests/test-dependencies.py](tests/test-dependencies.py#L113) |
| BNCC | 3 | Regras de nao invencao e frase obrigatoria estao consistentes em politicas, skills e testes. | [AGENTS.md](AGENTS.md#L14), [references/alinhamento-bncc.md](references/alinhamento-bncc.md#L7), [tests/test-bncc.py](tests/test-bncc.py#L24) |
| Participacao da equipe pedagogica | 3 | Revisao humana e participacao da equipe pedagogica estao prescritas de forma recorrente. | [AGENTS.md](AGENTS.md#L28), [.github/copilot-instructions.md](.github/copilot-instructions.md#L23), [references/alinhamento-bncc.md](references/alinhamento-bncc.md#L32) |
| Seguranca | 3 | Politicas e guardrails bloqueantes cobrem credenciais, prompt injection e riscos de dados. | [SECURITY.md](SECURITY.md#L7), [guardrails/policy.yaml](guardrails/policy.yaml#L130), [tests/test-guardrails.py](tests/test-guardrails.py#L67) |
| Privacidade | 3 | Regras de minimizacao e nao compartilhamento com terceiros estao claras e testadas. | [PRIVACY.md](PRIVACY.md#L15), [guardrails/policy.yaml](guardrails/policy.yaml#L85), [tests/test-safety.py](tests/test-safety.py#L28) |
| Autoria | 3 | Preservacao de autoria estudantil e metodologica esta formalizada e testada. | [AGENTS.md](AGENTS.md#L25), [guardrails/policy.yaml](guardrails/policy.yaml#L55), [tests/test-authorship.py](tests/test-authorship.py#L38) |
| Testes | 3 | Suite esta mais robusta com 37 testes, incluindo consistencia de dependencias e cobertura de cenarios-chave. | [tests/test-structure.py](tests/test-structure.py#L14), [tests/test-dependencies.py](tests/test-dependencies.py#L94), [.github/workflows/validate-agent.yml](.github/workflows/validate-agent.yml#L28) |
| Observabilidade | 1 | Ainda nao ha trilha operacional estruturada de eventos, metricas de conformidade e painel de acompanhamento. | [README.md](README.md#L99), [guardrails/policy.yaml](guardrails/policy.yaml#L219) |
| Documentacao | 3 | Documentacao e ampla e alinhada com politicas e referencias, com catalogo atualizado de skills. | [README.md](README.md#L46), [references/guardrails.md](references/guardrails.md#L11), [references/skill-standard.md](references/skill-standard.md#L49) |
| Prontidao para piloto | 3 | Estado atual e adequado para piloto controlado, com bloqueios anteriores resolvidos; ainda sem evidencia para uso em producao. | [README.md](README.md#L105), [skills/catalog.yaml](skills/catalog.yaml#L4), [tests/test-dependencies.py](tests/test-dependencies.py#L113) |

## Sintese executiva

O agente evoluiu de forma consistente em relacao ao ciclo anterior: cadeia de dependencias agora esta fechada, skills foram padronizadas e CI ganhou teste dedicado de consistencia. O conjunto atual suporta piloto controlado com revisao humana. Ainda faltam capacidades de observabilidade operacional e criterios mais fortes de readiness para uso controlado amplo.

Classificacao geral sugerida: 3.0/4.

## Falhas encontradas (estado atual)

1. Risco de parsing YAML no frontmatter de skill:
- A skill de orquestracao usa tabulacao no frontmatter; validadores YAML estritos podem falhar.
- Evidencia: [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L4).

2. Gap de observabilidade operacional:
- Nao existe log estruturado de decisoes de bloqueio/escalonamento nem indicadores de conformidade em runtime.
- Evidencias: [README.md](README.md#L99), [guardrails/policy.yaml](guardrails/policy.yaml#L219).

3. Ausencia de validador formal de formato de skill:
- Ha padrao oficial documentado, mas ainda sem validador automatico dedicado para todas as regras do padrao.
- Evidencias: [references/skill-standard.md](references/skill-standard.md#L238), [tests/test-dependencies.py](tests/test-dependencies.py#L1).

## Evolucoes relevantes desde a auditoria anterior

- Skill de arquitetura adicionada: [skills/planejar-arquitetura/SKILL.md](skills/planejar-arquitetura/SKILL.md#L1).
- Cadeia no catalogo corrigida: [skills/catalog.yaml](skills/catalog.yaml#L12).
- Skills antes resumidas agora padronizadas: [skills/iniciar-ideathon/SKILL.md](skills/iniciar-ideathon/SKILL.md#L1), [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L1).
- Teste de consistencia de dependencias criado e integrado ao CI: [tests/test-dependencies.py](tests/test-dependencies.py#L113), [.github/workflows/validate-agent.yml](.github/workflows/validate-agent.yml#L28).

## Riscos principais

- Risco tecnico de regressao de formatacao em frontmatter por tabulacao.
- Risco de auditoria incompleta por falta de observabilidade operacional.
- Risco pedagogico residual por ausencia de template institucional padrao para registro de revisao humana.

## Debito tecnico

- Implementar validador de conformidade de skills contra o padrao oficial (campos, secoes, semver, ASCII, indentacao).
- Criar verificacao automatica de frontmatter YAML estrito em CI.
- Implantar camada minima de telemetria de conformidade (eventos block/warning/escalate).

## Debito pedagogico

- Definir artefato padrao para registrar validacoes da equipe pedagogica (responsavel, criterio, data, decisao).
- Formalizar rubrica minima de qualidade de evidencias por etapa IPIT.
- Consolidar protocolo operacional de confirmacao documental de BNCC no fluxo de uso.

## Acoes bloqueantes

1. Remover tabulacao do frontmatter em [skills/orquestrar-ipit/SKILL.md](skills/orquestrar-ipit/SKILL.md#L4) e validar parsing YAML estrito em CI.
2. Criar validador de skill-standard como etapa obrigatoria de pipeline.
3. Definir template institucional de revisao humana para decisao pedagogica/curricular.

## Acoes recomendadas

1. Adicionar teste de integracao fim a fim do fluxo de skills com fixtures dedicados por etapa.
2. Criar checklist automatica de privacidade para identificar PII/segredos em docs e fixtures.
3. Incluir secao de observabilidade no README com indicadores e rotina de revisao.
4. Registrar evidencias pedagogicas em template unico versionado.

## Roadmap de 30, 60 e 90 dias

### 30 dias

- Normalizar frontmatter de todas as skills para indentacao por espacos.
- Adicionar validador de skill-standard e parsing YAML estrito ao CI.
- Publicar template de revisao humana institucional.
- Entregavel: baseline tecnico-pedagogico sem bloqueios formais de formato.

### 60 dias

- Implementar teste de integracao de cadeia completa de skills.
- Definir rubrica de qualidade das evidencias pedagogicas por etapa.
- Padronizar registro de decisao curricular e BNCC no fluxo de uso.
- Entregavel: piloto controlado com rastreabilidade pedagogica e tecnica fortalecida.

### 90 dias

- Implantar observabilidade minima de conformidade (eventos, trilhas, indicadores).
- Rodar ciclo de piloto com coleta de feedback docente/equipe pedagogica.
- Revisar pontuacao de prontidao com evidencias operacionais consolidadas.
- Entregavel: versao candidata a uso controlado institucional.

## Conclusao

Com as evidencias atuais, o agente esta adequado para piloto controlado (nota 3 em prontidao para piloto), desde que as acoes bloqueantes de formato e governanca operacional sejam tratadas no curto prazo. Nao ha evidencia suficiente para declarar prontidao para producao.
