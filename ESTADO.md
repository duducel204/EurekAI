# ESTADO — ponteiro operacional do EurekAI

Este arquivo é um **índice de estado**, não uma cópia do roadmap.

## Fonte de versão

A versão técnica atual do repositório é sempre o **HEAD remoto de `origin/main`** no momento da verificação.

Não gravar aqui um SHA como “versão atual permanente”. O agente deve consultar o Git antes de analisar, editar, commitar ou abrir PR.

## Ponteiros canônicos

- visão do produto: `produto/VISAO-ORIGINAL.md`
- contrato comum: `AGENTS.md`
- índice para agentes: `agentes/INDEX.md`
- roadmap histórico: `codex/goals/ROADMAP-GOALS.md`
- protocolo de execução sequencial: `codex/goals/PROTOCOLO-EXECUCAO-SEQUENCIAL.md`
- Goals concluídos: `codex/goals/`
- execuções: `execucoes/`
- investigações: `investigacao/`
- mapa do conhecimento: `mapa-do-conhecimento/`
- pipelines permanentes: `pipelines/`
- schemas compactos: `pipelines/schemas/`

## Gates

- `READY_FOR_CODEX` = pronto para qualquer executor autorizado; nome legado.
- `CONCLUÍDO` = etapa validada e encerrada.

## Estado lógico atual

- GOAL-001 — concluído
- GOAL-002 — concluído
- GOAL-003 — concluído como mineração inicial; ingestão incremental continua por pipelines
- GOAL-004 — concluído
- GOAL-005 — concluído, revalidado e validado
- GOAL-006 — concluído, revalidado e validado
- GOAL-007 — concluído, revalidado e validado
- GOAL-008 — concluído
- GOAL-009 — concluído
- GOAL-010 — concluído

GOAL-001–010 formam o bootstrap inicial encerrado do EurekAI. Novas fontes rotineiras, grandes corpora e ingestões incrementais entram por pipelines permanentes.

## Produto

A visão canônica inicial do produto está em `produto/VISAO-ORIGINAL.md`.

O produto final é uma experiência de alfabetização em inteligência artificial acessível por link, voltada a pessoas que começam da base zero. O repositório é o motor interno; não é a interface final.

## Operação atual

Modo atual: **pós-bootstrap / operação contínua por pipelines**.

Próximo foco operacional recomendado:

1. manter READMEs e ponteiros coerentes com o estado pós-GOAL-010;
2. preparar a primeira execução autorizada da pipeline Google Takeout/Drive;
3. iniciar por política de dados e inventário determinístico;
4. usar EKL-0, quando apropriado, para classificação/mineração compacta;
5. somente depois validar, expandir e canonizar resultados aprovados.

A pipeline Google Takeout/Drive está definida, mas nenhum Takeout foi acessado, processado ou canonizado no `main` como corpus de conhecimento.

EKL-0 está documentado como schema compacto experimental e intermediário para leitura futura do histórico/Takeout. Ele não é conhecimento final, não substitui validação e não autoriza mineração massiva.

## Pendências conhecidas

- `investigacao/pendencias/INV-001-CORPUS-HISTORICO.md` permanece **PARCIAL**: há lotes iniciais, mas o corpus histórico ainda não é exaustivo e faltam localizadores individuais para parte das evidências.
- PRs ou branches antigos que ainda tratem GOAL-008–010 como “preparados” devem ser considerados obsoletos diante do `main` pós-merge, salvo revisão explícita.
- A PR de evidências Google Drive permanece material não canonizado enquanto não for revisada e reconciliada com os contratos de ingestão.

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