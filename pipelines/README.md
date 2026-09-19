# Pipelines permanentes do EurekAI

Esta área contém contratos de operação contínua. GitHub é o estado canônico; fontes grandes permanecem em seus locais autorizados. Pipelines não aprovam ou mesclam PRs automaticamente.

## Pipelines mínimas

| Pipeline | Entrada | Saída canônica | Gate |
| --- | --- | --- | --- |
| **Ingestão** | nova fonte autorizada | manifesto, índice, classificação e evidências derivadas | contrato de ingestão + validação |
| **Auditoria** | evidências/unidades candidatas | aceitar, corrigir, rejeitar ou investigar | procedência e limites aprovados |
| **Pedagogia/conteúdo** | conhecimento validado | progressões e unidades versionadas | mecanismo separado de representação/exemplo |
| **Investigação** | lacuna/tensão material | evidência incorporada ou bloqueio explícito | ticket com critério de fechamento |
| **Publicação/exportação futura** | conteúdo auditado | formato de destino ainda não decidido | autorização humana específica; não ativo agora |

## Estado comum

Cada execução usa `run_id`, versão do contrato, fonte/lote, cursor, itens por estado, erros, hashes de entrada/saída e commit/PR de destino. O estado operacional volumoso ou sensível permanece fora do Git; o repositório recebe manifestos compactos e artefatos canônicos revisáveis.

O [contrato de ingestão](CONTRATO-INGESTAO.md) rege fontes novas. [PIPELINE-TAKEOUT-DRIVE.md](PIPELINE-TAKEOUT-DRIVE.md) é o primeiro candidato e ainda não foi executado.
