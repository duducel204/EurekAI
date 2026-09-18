# Evidências 001 — Work Google Drive

As unidades abaixo registram o que as fontes demonstram. Elas não canonizam o conteúdo nem afirmam que a implementação descrita continua ativa.

## GD-E-001 — Separação entre avanço cognitivo e autorização operacional

**Fonte:** GD-F-002  
**Evidência:** o briefing diferencia `SEGUIR`, `DECIDIR` e `AUTORIZACAO_EXECUCAO`; execução depende de autorização humana explícita.  
**Conecta com:** governança, estados cognitivos, controle de execução, humano–IA.  
**Tags candidatas:** #dream-team #governanca #autorizacao #humano-ia #execucao  
**Força:** alta para intenção normativa; não comprova enforcement em código.

## GD-E-002 — Pipeline cognitivo e operacional por papéis

**Fontes:** GD-F-001, GD-F-002  
**Evidência:** há módulos e papéis para coletor, qualificador, orquestrador, sentinela, arquiteto, analista, executor, registrador e rollback.  
**Conecta com:** decomposição funcional, checkpoints, auditoria, reversibilidade.  
**Tags candidatas:** #agentes #pipeline #arquitetura-cognitiva #rollback #auditoria  
**Força:** alta para topologia documentada; implementação individual precisa de inspeção própria.

## GD-E-003 — Registro imutável como princípio recorrente

**Fontes:** GD-F-002, GD-F-004  
**Evidência:** decisões, autorizações e execuções devem gerar artefatos verificáveis; a memória posterior descreve ledger único, hashes, contratos e canonizações.  
**Conecta com:** procedência, não sobrescrita, eventos, evidência verificável.  
**Tags candidatas:** #registro #imutabilidade #proveniencia #eventos #hash  
**Força:** média-alta; parte é regra e parte é relato retrospectivo.

## GD-E-004 — Falhas reais atribuídas a colisão e falta de idempotência

**Fonte:** GD-F-004  
**Evidência:** a memória registra dois bugs: colisão de nomes por timestamp de segundo e reingestão duplicada pelo Registrador; ambos são descritos como corrigidos e retestados.  
**Conecta com:** idempotência, versionamento, ingestão incremental, auditoria.  
**Tags candidatas:** #erro #idempotencia #registrador #versionamento #teste  
**Força:** média; requer logs/commits/testes originais para confirmação independente.

## GD-E-005 — Distinção entre fonte, memória, processamento e auditoria

**Fontes:** GD-F-005, GD-F-006  
**Evidência:** a topologia do Segundo Cérebro separa entrada, memória, processados, prévias, originais, erros, revisão humana e auditoria.  
**Conecta com:** fonte imutável versus derivação recriável, gates, pipeline de conhecimento.  
**Tags candidatas:** #segundo-cerebro #memoria #fonte #derivacao #auditoria  
**Força:** alta para arquitetura de pastas; não confirma disciplina de uso.

## GD-E-006 — Conhecimento representado como grafo derivado

**Fonte:** GD-F-007  
**Evidência:** existe um artefato JSON nomeado como grafo completo, acompanhado de documentos derivados que registram nós, relações, intenções, hipóteses e comandos em modo preview.  
**Conecta com:** modelo navegável, relações, tags, inventário e consultas.  
**Tags candidatas:** #grafo #conhecimento #relacoes #artefatos #preview  
**Força:** média; esquema e cobertura ainda precisam de auditoria campo a campo.

## GD-E-007 — Mobile-first e sincronização aparecem como decisões arquiteturais

**Fontes:** GD-F-008, GD-F-009  
**Evidência:** os documentos registram priorização de núcleo mobile-first, estratégia de sincronização e propagação de credenciais por JSON-RPC.  
**Conecta com:** arquitetura técnica, decisões, autenticação, sincronização.  
**Tags candidatas:** #mobile-first #sincronizacao #json-rpc #autenticacao  
**Força:** média-baixa para estado real; os próprios documentos podem ser sínteses derivadas ou simuladas.

## GD-E-008 — Falhas tratadas como fluxo rastreável

**Fonte:** GD-F-010  
**Evidência:** o procedimento define detecção, causa raiz, mitigação, regressão, monitoramento e escalada por ID de artefato/incidente.  
**Conecta com:** auditoria, incidentes, validação, aprendizado operacional.  
**Tags candidatas:** #falhas #rca #regressao #monitoramento #incidente  
**Força:** alta como procedimento proposto; não comprova execução histórica.

## GD-E-009 — Ciclo autônomo limitado por revisão e auditoria

**Fonte:** GD-F-011  
**Evidência:** o plano de bootstrap descreve Google Drive como memória, Apps Script como execução, ciclos periódicos, staging, erros, fila humana e log de auditoria; também explicita idempotência e modo preview.  
**Conecta com:** ingestão contínua, humano no circuito, automação incremental, validação.  
**Tags candidatas:** #apps-script #gemini #automacao #revisao-humana #audit-log  
**Força:** alta como intenção/blueprint; não prova que o ciclo foi implantado.

## GD-E-010 — Evolução entre arquiteturas, não um único sistema estático

**Fontes:** GD-F-002, GD-F-004, GD-F-005, GD-F-011  
**Evidência:** os documentos mostram mudanças de ambiente, nomenclatura, módulos e implementação ao longo do tempo.  
**Conecta com:** reaprendizagem, transferência entre ferramentas, continuidade, drift.  
**Tags candidatas:** #evolucao #transferencia #continuidade #drift #reaprendizagem  
**Força:** alta para existência de evolução; causalidade e sequência exata ainda precisam de linha do tempo.

## Síntese provisória

O Drive oferece evidência de que o EurekAI não surgiu como ideia isolada. Ele converge padrões experimentados em dois troncos anteriores:

1. **Dream Team:** governança, papéis, autorização, registro e rollback.
2. **Segundo Cérebro:** ingestão, memória, processamento, grafo, revisão e auditoria.

Essa convergência é candidata a relação de ancestralidade conceitual, ainda não a dependência técnica confirmada.
