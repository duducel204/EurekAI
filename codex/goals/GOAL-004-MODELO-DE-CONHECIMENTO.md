# GOAL-004 — Modelar o conhecimento atual

**Status:** CONCLUÍDO
**Dependência:** GOAL-003 mineração inicial concluída
**Modo:** EXECUTADO + VALIDADO

## Intent
Transformar o inventário existente em um modelo simples e navegável do conhecimento observado, sem classificar domínio e sem impor taxonomia definitiva.

## Operação
1. Sincronizar `main` antes de agir.
2. Ler GOAL-001–003, retornos, corpus, INDEX-TAGS e diretriz transversal.
3. Aplicar/normalizar tags somente onde sustentadas.
4. Construir uma matriz/índice compacto: evidência ↔ tags ↔ projeto/contexto ↔ eventos ↔ artefatos/documentos/ideias/planos.
5. Detectar clusters emergentes por interseção e recorrência, sem transformar cluster em categoria definitiva.
6. Identificar sinais de conceito-antes-do-nome, nome-antes-da-compreensão, transição mental, reaprendizagem, transferência e conhecimento tácito.
7. Distinguir participação humano–IA quando houver evidência.
8. Registrar lacunas/tensões e criar pendência apenas quando material.
9. Preservar derivações úteis para Goals 005–008 sem executá-los.

## Simplificação
Preferir **corpus único + tags + consultas/lentes**. Não criar mapa físico separado quando uma visão puder ser derivada das mesmas unidades.

## Deliverables
- modelo/índice inicial do conhecimento;
- tags novas/aliases realmente justificados;
- clusters candidatos;
- lacunas/tensões;
- derivações reutilizáveis;
- relatório em `codex/retornos/`.

## Acceptance
O modelo deve permitir responder, sem reler todo corpus: quais assuntos aparecem; em quais contextos; que tipos de eventos existem; quais itens se conectam; onde há transferência/tensão; e quais evidências sustentam cada visão.

Não afirmar domínio. Não transformar frequência em competência. Não criar taxonomia definitiva.

## Return
Base/commit; corpus consumido; unidades/tagueamento; clusters candidatos; relações relevantes; lacunas; arquivos alterados; validação; prontidão para GOAL-005. Não executar GOAL-005.
