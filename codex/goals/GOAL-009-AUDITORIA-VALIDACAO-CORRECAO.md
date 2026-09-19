# GOAL-009 — Auditoria, validação, correção e contrato de ingestão

**Status:** PREPARADO — NÃO LIBERADO
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO
**Dependência:** GOAL-008 concluído e validado
**Sequência:** segundo passo da sequência 008→009→010

## Intent
Auditar as unidades produzidas no GOAL-008 e consolidar um contrato geral de ingestão para fontes futuras.

O GOAL-009 não deve minerar massivamente Google Takeout, NotebookLM ou qualquer outro corpus. Ele deve definir o funil seguro pelo qual fontes grandes serão tratadas depois do bootstrap: inventário, classificação, mineração, validação e canonização.

## Premissa incorporada
Nem toda conversa ou documento contém conhecimento canônico. Muitas conversas são apenas operacionais, como comandos, ações rápidas, consultas pontuais ou interações de controle.

Antes de minerar conhecimento, o sistema deve classificar a natureza do material.

## Classes mínimas de conversa/fonte
- **Operacional:** ação, comando, consulta simples, automação pontual. Pode ser lida para triagem, mas não vira conhecimento por padrão.
- **Execução:** produção de código, arquivo, script, documento ou configuração. Pode gerar artefato/experiência.
- **Exploração:** brainstorm, hipótese, comparação, possibilidade. Pode gerar hipótese ou linha de investigação.
- **Aprendizado:** aquisição ou reorganização de conhecimento. Pode gerar evidência/conhecimento.
- **Decisão:** escolha explícita, canonização, descarte, mudança de direção. Pode gerar decisão.
- **Governança:** regra, contrato, arquitetura de agentes, protocolo ou gate. Pode gerar norma canônica.

## Operação
1. Consumir o lote real do GOAL-008.
2. Auditar cada unidade por:
   - procedência;
   - evidência;
   - limites epistemológicos;
   - coerência com relações;
   - coerência pedagógica;
   - duplicação;
   - tags;
   - atemporalidade;
   - dependência de ferramenta/versão;
   - drift entre agentes.
3. Corrigir somente o necessário, preservando histórico e registrando alteração material.
4. Consolidar um contrato de ingestão que possa ser usado por fontes grandes.
5. Definir o que é resolvido por código determinístico e o que exige LLM.

## Separação de custos/contexto
O contrato deve preservar esta divisão:

- **Indexação sem IA:** listar arquivos, gerar hashes, tamanhos, datas, IDs, contagem de mensagens, formatos e fila.
- **Classificação com IA leve:** analisar amostras/metadados para definir classe, prioridade e descarte.
- **Mineração com IA:** processar somente itens classificados como relevantes.
- **Auditoria/canonização:** validar inferências, corrigir drift e publicar artefatos canônicos.

A unidade de trabalho preferencial é a conversa/documento individual, não o Takeout inteiro.

## Deliverables
- Relatório de auditoria do lote do GOAL-008 em `execucoes/EXEC-GOAL-009.md`.
- Contrato geral de ingestão, preferencialmente em `pipelines/` ou área equivalente, contendo:
  - fonte;
  - inventário;
  - índice;
  - classificação;
  - mineração;
  - validação;
  - canonização;
  - retomada;
  - deduplicação;
  - controle de custo/contexto.
- Lista de correções aplicadas às unidades do GOAL-008.
- Lista de pendências para o GOAL-010.

## Acceptance
- Nenhuma validação simulada pode ser registrada como executada.
- Correções devem ser cirúrgicas e justificadas.
- Conteúdo operacional deve poder ser descartado como ação sem virar conhecimento.
- O contrato de ingestão deve permitir processamento incremental e retomável.
- O contrato deve ser aplicável ao Google Takeout/Drive, mas não exclusivo dele.
- Deve ficar claro quando código tradicional basta e quando LLM é necessário.

## Validação
- Validar as unidades corrigidas contra o contrato do GOAL-008.
- Validar o contrato de ingestão contra o caso Google Takeout/Drive observado:
  - pasta `Takeout/Gemini`;
  - pasta `Takeout/NotebookLM`;
  - pasta `Takeout/Gemini no Workspace/Conversation History`.
- Executar validações mecânicas disponíveis quando aplicável.
- Registrar lacunas sem inventar acesso, conteúdo ou execução não comprovada.

## Stop conditions
Parar se:

- o executor tentar processar massa de dados sem inventário;
- houver mistura entre ação operacional e conhecimento canônico;
- o contrato exigir ler corpus inteiro em contexto de LLM;
- a auditoria encontrar falha material no lote do GOAL-008 que impeça o GOAL-010.

## Gate
Este Goal está preparado, mas não liberado. Ele só pode ser executado após GOAL-008 estar `CONCLUÍDO` e validado. Em sequência autorizada, conclusão validada do GOAL-009 libera o GOAL-010.
