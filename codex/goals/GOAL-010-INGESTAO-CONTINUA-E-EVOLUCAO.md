# GOAL-010 — Ingestão contínua e evolução

**Status:** SEED_DRAFT
**Dependência:** padrões estáveis observados nos Goals anteriores

## Intent
Transformar EurekAI em sistema evolutivo: novas conversas, projetos, erros, artefatos e descobertas entram incrementalmente sem exigir reconstrução integral.

## Fluxo candidato
`nova fonte → lote → extração → tags → relações/derivações → validação → corpus → índices/trilhas/conteúdo afetados`

## Requisitos candidatos
- incremental e idempotente quando possível;
- deduplicação;
- lineage/procedência;
- detectar quais saídas são afetadas por nova evidência;
- investigação para lacunas;
- não sobrescrever história;
- permitir revisão humana/IA onde inferência for material.

## Não decidir ainda
Stack de automação, banco, scheduler, agentes permanentes ou infraestrutura até volume/padrões justificarem.
