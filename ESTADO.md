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
- GOAL-005 — concluído, revalidado e validado
- GOAL-006 — concluído, revalidado e validado
- GOAL-007 — concluído, revalidado e validado
- GOAL-008 — preparado; não liberado
- GOAL-009 — preparado; não liberado
- GOAL-010 — preparado; não liberado

A sequência 005→006→007 foi completamente liberada, executada, revalidada semanticamente/epistemologicamente e teve validação mecânica executada no ambiente Code, informada pelo operador humano como aprovada. Os relatórios em `execucoes/` preservam a distinção entre essas camadas de validação.

A sequência 008→009→010 está preparada para execução sequencial condicional. Ela incorpora a visão de que GOAL-001–010 formam o bootstrap inicial do EurekAI e que, após o GOAL-010, novas fontes devem entrar por pipelines permanentes.

## Próximo foco preparado
GOAL-008 inicia a produção de unidades de conhecimento rastreáveis.

GOAL-009 audita o lote do GOAL-008 e consolida o contrato de ingestão/classificação/mineração.

GOAL-010 encerra o bootstrap inicial e define a transição para pipelines permanentes, usando Google Takeout/Drive como primeiro caso candidato de operação contínua.

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
