# Roadmap de Goals — EurekAI

Este arquivo registra direção e estado. Autorização de execução depende dos gates e do escopo humano aplicável.

## Regra
Goals posteriores devem ser refinados pelas evidências dos anteriores. Não executar um Goal apenas porque aparece aqui.

## Gates
- `READY_FOR_CODEX` = **pronto para executor autorizado** (nome legado, sem exclusividade do Codex).
- `CONCLUÍDO` = execução validada e encerrada.

`SEED_DRAFT`, `DRAFT_EVOLUTIVO` e `PREPARADO` são estados de preparação.

## Ciclo
- GOAL-001 — Contrato operacional e inspeção — CONCLUÍDO.
- GOAL-002 — Aquisição de evidências e fila de investigação — CONCLUÍDO.
- GOAL-003 — Mineração inicial e inventário — CONCLUÍDO COMO MINERAÇÃO INICIAL; ingestão incremental continua.
- GOAL-004 — Modelar o conhecimento atual — CONCLUÍDO.
- GOAL-005 — Relações, dependências e transferências — PREPARADO; NÃO LIBERADO.
- GOAL-006 — Progressão do zero à fronteira atual — PREPARADO; depende de GOAL-005 CONCLUÍDO.
- GOAL-007 — Engenharia pedagógica atemporal — PREPARADO; depende de GOAL-006 CONCLUÍDO.
- GOAL-008 — Produção sistemática do conteúdo — SEED_DRAFT.
- GOAL-009 — Auditoria, validação e correção — SEED_DRAFT.
- GOAL-010 — Ingestão contínua e evolução — SEED_DRAFT.

## Sequência preparada
GOAL-005 → GOAL-006 → GOAL-007 está preparada para execução sequencial condicional segundo [PROTOCOLO-EXECUCAO-SEQUENCIAL.md](PROTOCOLO-EXECUCAO-SEQUENCIAL.md).

Uma única autorização humana futura pode liberar a sequência inteira. O executor atravessa cada gate somente após validar a etapa anterior. Falha interrompe a sequência.

## Macrofluxo
fontes históricas → aquisição/investigação → evidências → inventário → modelo do conhecimento → relações/dependências → progressão → engenharia pedagógica → conteúdo → auditoria/validação → evolução contínua.

## Princípio de velocidade
Acelerar significa reduzir trabalho manual, duplicação, espera e releitura — não remover controles de evidência. Automatizar etapas seguras e gates verificáveis.

## Pesquisa distribuída
Lacunas podem gerar investigações para Codex, ChatGPT, Gemini/Cloud Code, outras IAs, André, repositórios, arquivos ou documentação. GitHub é memória canônica das perguntas, evidências incorporadas, decisões e estado.

## Execução multiagente
O executor específico não precisa ser definido durante a preparação. A ordem humana de execução seleciona/autoriza o executor da sessão.

O literal `READY_FOR_CODEX` é preservado por compatibilidade, mas sua semântica é genérica.

Relatórios novos devem preferir `execucoes/`.

## Derivação antecipada sem convergência prematura
A partir do GOAL-003, aplicar [DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md](DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md): uma leitura histórica pode produzir evidência e, quando sustentado, relações, transições cognitivas e matéria-prima candidata para Goals futuros.

## Pipeline sobreposto
Enquanto o Goal N executa, planejamento pode amadurecer N+1. Em sequência previamente autorizada, N+1 só atravessa o gate `READY_FOR_CODEX` quando N estiver `CONCLUÍDO` e validado.
