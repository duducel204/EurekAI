# ESTADO — ponteiro operacional do EurekAI

Este arquivo é um **índice de estado**, não uma cópia do roadmap.

## Fonte de versão
A versão técnica atual do repositório é sempre o **HEAD remoto de `origin/main`** no momento da verificação.

Não gravar aqui um SHA como “versão atual permanente”, porque qualquer novo commit o tornaria obsoleto. O agente deve consultar o Git antes de analisar, editar, commitar ou abrir PR.

## Ponteiros canônicos
- contrato comum: `AGENTS.md`
- índice para agentes: `agentes/INDEX.md`
- roadmap: `codex/goals/ROADMAP-GOALS.md`
- Goals: `codex/goals/`
- investigações: `investigacao/`
- mapa do conhecimento: `mapa-do-conhecimento/`

## Estado lógico atual
- GOAL-001 — concluído
- GOAL-002 — concluído
- GOAL-003 — concluído como mineração inicial; ingestão incremental continua
- GOAL-004 — concluído
- GOAL-005 — **preparado, não liberado, executor não definido**
- GOAL-006–010 — rascunhos/sementes conforme roadmap

O roadmap é a fonte operacional detalhada. Se este resumo divergir dele, **não continue por memória**: sincronize `main`, leia o roadmap e corrija o índice quando apropriado.

## Regra de trabalho multiagente
Ao iniciar trabalho, registre mentalmente ou no handoff o SHA de `origin/main` usado como base.

Antes de qualquer commit, push ou PR:
1. execute `git fetch origin`;
2. obtenha novamente `origin/main`;
3. compare com a base usada no início;
4. se `main` avançou, revise as mudanças novas antes de publicar;
5. se houver sobreposição ou impacto, reconcilie/rebase/reaplique e valide novamente;
6. somente então prossiga.

**Nunca publicar assumindo que a base antiga continua atual.**
