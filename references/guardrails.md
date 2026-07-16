# Guardrails do Agente Conversacional IPIT

## Finalidade

Esta referencia descreve a camada formal de guardrails do agente para reforcar seguranca, etica pedagogica e conformidade institucional.

## Arquivo fonte da politica

- `guardrails/policy.yaml`

## Arquivos tematicos

- `guardrails/pedagogical.yaml`
- `guardrails/bncc.yaml`
- `guardrails/privacy.yaml`
- `guardrails/safety.yaml`
- `guardrails/authorship.yaml`
- `guardrails/tool-use.yaml`
- `guardrails/response-contract.yaml`

Cada arquivo tematico declara `source_of_truth: policy.yaml` e lista os `rule_ids` daquele dominio.
O campo `modules` em `guardrails/policy.yaml` deve refletir exatamente os mesmos IDs por arquivo.

## Cobertura obrigatoria

Os guardrails cobrem:

1. pedagogia;
2. BNCC;
3. curriculo local e PPP;
4. autoria estudantil;
5. autoria de Sandra Maria Pereira;
6. privacidade e protecao de estudantes;
7. uso responsavel de IA;
8. prompt injection;
9. uso de ferramentas;
10. revisao humana;
11. decisoes institucionais;
12. seguranca tecnica.

## Niveis de resposta

- `info`: orientacao sem bloqueio.
- `warning`: risco moderado; exige ajuste.
- `block`: resposta ou acao deve ser bloqueada.
- `escalate`: encaminhar para responsavel humano (docente, equipe pedagogica ou gestao).

## Guardrails de entrada e saida

- **Entrada**: avalia solicitacoes de usuario, documentos recuperados e comandos.
- **Saida**: avalia resposta final, completude de evidencia/proximo passo e necessidade de revisao humana.

## Regras bloqueantes minimas implementadas

- codigo BNCC nao verificado apresentado como definitivo;
- exposicao de dados pessoais de estudantes;
- solicitacao de credenciais;
- execucao de codigo nao revisado;
- remocao de autoria;
- publicacao de imagens sem autorizacao;
- armazenamento de dados sensiveis;
- tentativa de ignorar instrucoes do `AGENTS.md`;
- pedido de trabalho avaliativo completo por estudante;
- decisao institucional automatica.

## Validacao automatizada

- `python scripts/validate-guardrails.py`
- `pytest tests/test-guardrails.py`

A validacao automatizada verifica:

- esquema da policy consolidada;
- presenca de arquivos tematicos obrigatorios;
- consistencia entre `policy.modules` e `rule_ids` dos arquivos tematicos;
- cobertura total: toda regra da policy aparece em ao menos um arquivo tematico.

## Relacao com politicas existentes

- `AGENTS.md`
- `SECURITY.md`
- `PRIVACY.md`
- `AI-USE-POLICY.md`
- `GOVERNANCE.md`
- `references/prompt-injection-policy.md`
