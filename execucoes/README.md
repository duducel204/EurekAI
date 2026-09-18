# Execuções

Área comum para relatórios/handoffs de execução de Goals, independentemente do executor.

## Por que existe
O EurekAI deixou de tratar `READY_FOR_CODEX` como exclusivo do Codex. Codex, Gemini/Cloud Code, humano ou outro executor autorizado podem executar Goals.

Por isso, novas execuções multiagente devem registrar seu resultado aqui em vez de criar uma memória paralela por agente.

## Registro mínimo
Cada relatório deve indicar:
- Goal executado;
- executor;
- branch;
- base de `origin/main` usada;
- HEAD remoto verificado antes da publicação;
- arquivos/entregáveis;
- critérios de aceitação;
- validações executadas;
- lacunas, tensões e limitações;
- estado final: `CONCLUÍDO` ou `BLOQUEADO`.

## Convenção candidata
`GOAL-005-<executor>-<data-ou-id>.md`

A convenção pode evoluir; rastreabilidade é mais importante que o nome.

## Histórico
`codex/retornos/` continua válido para execuções históricas e para trabalhos explicitamente pertencentes ao workflow Codex.
