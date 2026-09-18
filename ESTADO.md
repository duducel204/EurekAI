# ESTADO — ponteiro operacional do EurekAI

Este arquivo é um **índice de estado**, não uma cópia do roadmap.

## Fonte de versão
A versão técnica atual do repositório é sempre o **HEAD remoto de `origin/main`** no momento da verificação.

Não gravar aqui um SHA como “versão atual permanente”. O agente deve consultar o Git antes de analisar, editar, commitar ou abrir PR.

## Ponteiros canônicos
- contrato comum: `AGENTS.md`
- índice para agentes: `agentes/INDEX.md`
- roadmap: `codex/goals/ROADMAP-GOALS.md`
- protocolo de execução sequencial: `codex/goals/PROTOCOLO-EXECUCAO-SEQUENCIAL.md`
- Goals: `codex/goals/`
- execuções: `execucoes/`
- investigações: `investigacao/`
- mapa do conhecimento: `mapa-do-conhecimento/`

## Gates
- `READY_FOR_CODEX` = pronto para qualquer executor autorizado; nome legado.
- `CONCLUÍDO` = etapa validada e encerrada.

## Estado lógico atual
- GOAL-001 — concluído
- GOAL-002 — concluído
- GOAL-003 — concluído como mineração inicial; ingestão incremental continua
- GOAL-004 — concluído
- GOAL-005 — preparado, não liberado
- GOAL-006 — preparado, condicionado ao GOAL-005 concluído
- GOAL-007 — preparado, condicionado ao GOAL-006 concluído
- GOAL-008–010 — rascunhos/sementes conforme roadmap

A sequência 005→006→007 está preparada, mas **ainda não foi liberada para execução**.

## Regra de trabalho multiagente
Ao iniciar trabalho, registrar o SHA de `origin/main` usado como base.

Antes de qualquer commit, push ou PR:
1. `git fetch origin`;
2. obter novamente `origin/main`;
3. comparar com a base;
4. revisar mudanças novas;
5. reconciliar conflito textual/semântico quando houver;
6. validar novamente;
7. somente então publicar.

**Nunca publicar assumindo que a base antiga continua atual.**
