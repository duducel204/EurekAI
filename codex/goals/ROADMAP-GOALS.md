# Roadmap de Goals — EurekAI

Este arquivo registra direção e estado. Autorização de execução depende do status explícito de cada Goal.

## Regra
Goals posteriores devem ser refinados pelas evidências dos anteriores. Não executar um Goal apenas porque aparece aqui.

## Ciclo
- GOAL-001 — Contrato operacional e inspeção — CONCLUÍDO.
- GOAL-002 — Aquisição de evidências e fila de investigação — CONCLUÍDO.
- GOAL-003 — Mineração inicial e inventário — CONCLUÍDO COMO MINERAÇÃO INICIAL; ingestão incremental continua.
- GOAL-004 — Modelar o conhecimento atual — CONCLUÍDO.
- GOAL-005 — Relações, dependências e transferências — PREPARADO; EXECUTOR NÃO DEFINIDO; NÃO LIBERADO.
- GOAL-006 — Progressão do zero à fronteira atual — SEED_DRAFT.
- GOAL-007 — Engenharia pedagógica atemporal — SEED_DRAFT.
- GOAL-008 — Produção sistemática do conteúdo — SEED_DRAFT.
- GOAL-009 — Auditoria, validação e correção — SEED_DRAFT.
- GOAL-010 — Ingestão contínua e evolução — SEED_DRAFT.

## Macrofluxo
fontes históricas → aquisição/investigação → evidências → inventário → modelo do conhecimento → relações/dependências → progressão → engenharia pedagógica → conteúdo → auditoria/validação → evolução contínua.

## Princípio de velocidade
Acelerar significa reduzir trabalho manual, duplicação, espera e releitura — não remover controles de evidência. Automatizar etapas seguras. Não criar gate artificial quando uma descoberta não alterar materialmente a próxima arquitetura; preservar gates quando houver dependência real.

## Pesquisa distribuída
Lacunas podem gerar investigações para Codex, ChatGPT, Gemini/Cloud Code, outras IAs, André, repositórios, arquivos ou documentação. GitHub é memória canônica das perguntas, evidências incorporadas, decisões e estado; não precisa conter cópia indiscriminada de todo histórico externo.

## Execução multiagente
Um Goal pode futuramente ser executado por agente diferente do Codex, desde que:
- o executor seja explicitamente registrado;
- o adaptador do agente e `AGENTS.md` sejam lidos;
- o estado executável seja inequívoco;
- o destino do retorno/handoff seja definido antes da execução;
- nenhuma automação interprete “preparado” como autorização.

`READY_FOR_CODEX` continua sendo gatilho operacional do watcher Codex. Portanto, não usar esse status quando a intenção for apenas preparar ou quando o executor ainda não estiver escolhido.

## Derivação antecipada sem convergência prematura
A partir do GOAL-003, aplicar [DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md](DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md): uma leitura histórica pode produzir evidência e, quando sustentado, relações, transições cognitivas e matéria-prima candidata para Goals futuros. Essas derivações não executam nem decidem os Goals posteriores.

Observar especialmente conceito antes do nome, nome antes da compreensão, transições de modelo mental, retenção/reaprendizagem, transferência entre projetos, conhecimento tácito e autoria cognitiva humano–IA.

A hipótese de três mapas — conceitual, histórico e cognitivo — permanece aberta para teste; não é arquitetura canonizada.

## Pipeline sobreposto
Enquanto o Goal N executa, planejamento pode amadurecer N+1 e registrar sementes de N+2...N+k. Somente um Goal dependente deve se tornar executável quando suas dependências estiverem observadas e o executor estiver definido; os posteriores permanecem rascunhos explicitamente revisáveis.
