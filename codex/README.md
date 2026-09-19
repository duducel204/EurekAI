# Codex

**Estado atual:** histórico e suporte operacional. Os GOALs 001–010 foram concluídos.

## Função

Esta área concentra documentação ligada ao workflow Codex usado para estruturar o bootstrap inicial do EurekAI.

Ela contém:

- `goals/`: Goals, roadmap e protocolos de execução;
- `retornos/`: relatórios históricos do workflow Codex;
- referências que ajudam a reconstruir como o bootstrap foi executado.

## Situação pós-GOAL-010

`codex/` não é mais a fila principal de novas tarefas. A operação recorrente agora deve usar `pipelines/`.

O papel desta pasta é:

- preservar histórico de execução;
- permitir auditoria dos Goals concluídos;
- orientar agentes que precisem entender como o bootstrap foi formado;
- manter compatibilidade com o nome legado `READY_FOR_CODEX`.

## Regra

Não tratar rascunhos antigos ou PRs obsoletas como estado atual. O estado canônico é `main`, com ponteiro em `ESTADO.md` e roadmap em `codex/goals/ROADMAP-GOALS.md`.