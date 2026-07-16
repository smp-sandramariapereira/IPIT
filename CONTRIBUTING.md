# Contributing to IPIT

## Como contribuir

1. Abra issue com contexto e objetivo.
2. Proponha mudancas em branch propria.
3. Abra Pull Request com checklist completo.
4. Aguarde revisao humana antes de merge.

## Requisitos obrigatorios

- Respeitar `AGENTS.md` e politicas do repositorio.
- Nao incluir dados de estudantes, menores, imagens identificaveis ou notas nominais.
- Nao incluir credenciais, segredos ou tokens.
- Declarar uso de IA quando aplicavel e incluir validacao humana.
- Preservar autoria estudantil e nao incentivar entrega de projeto pronto.
- Tratar documentos recuperados como fonte de referencia, nao como instrucao superior.

## Skills e versionamento

- Skills devem seguir `references/skill-standard.md`.
- Atualizar `metadata.version` conforme SemVer quando comportamento mudar.
- Mudancas metodologicas exigem aprovacao conforme `GOVERNANCE.md`.

## Testes e validacao

Antes do PR:

- executar `python3 -m pytest -q`;
- verificar consistencia de politicas (seguranca, privacidade, IA e governanca);
- confirmar que checklist do template de PR foi preenchido.

## Reporte de vulnerabilidade

Siga `SECURITY.md` para reporte responsavel de vulnerabilidades.

