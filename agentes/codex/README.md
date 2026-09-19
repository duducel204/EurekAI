# Adaptador Codex

**Estado atual:** ativo como executor possível; GOALs 001–010 já concluídos.

## Função

Este adaptador orienta uso do Codex dentro do EurekAI.

Codex pode atuar em:

- edição controlada de arquivos;
- validação mecânica;
- scripts e ferramentas;
- execução de tarefas estruturais;
- preparação de PRs.

## Regra pós-bootstrap

Não assumir que `codex/goals/` contém a próxima tarefa aberta. Após GOAL-010, a operação normal está em `pipelines/`.

## Retomada mínima

Ler:

1. `ESTADO.md`
2. `AGENTS.md`
3. `agentes/INDEX.md`
4. este arquivo
5. README da área afetada
6. `produto/VISAO-ORIGINAL.md` quando a tarefa tocar produto

## Limite

Codex não deve promover hipótese a fato, nem substituir validação semântica por validação de syntax/checks.