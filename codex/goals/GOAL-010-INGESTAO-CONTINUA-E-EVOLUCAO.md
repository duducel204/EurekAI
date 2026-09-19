# GOAL-010 — Evolução contínua e transição para pipelines permanentes

**Status:** PREPARADO — NÃO LIBERADO
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO
**Dependência:** GOAL-009 concluído e validado
**Sequência:** terceiro passo da sequência 008→009→010

## Intent
Encerrar o bootstrap inicial do EurekAI e transformar o repositório em uma plataforma operacional de aquisição, organização, validação e reutilização contínua de conhecimento.

O GOAL-010 não significa “fim do EurekAI”. Ele marca a transição de um projeto guiado por Goals de fundação para um sistema operado por pipelines permanentes.

## Premissa incorporada
Depois do GOAL-010, não é desejável criar uma sequência infinita de novos Goals para cada nova fonte ou mineração. Goals 001–010 constroem a infraestrutura cognitiva inicial. A operação contínua deve acontecer por pipelines versionados, auditáveis e reutilizáveis.

## Ciclo operacional permanente
`nova fonte → inventário → indexação → classificação → mineração seletiva → validação → canonização → atualização de conhecimento/pedagogia/conteúdo → auditoria`

## Operação
1. Consumir os resultados reais dos GOALs 008 e 009.
2. Consolidar a transição de bootstrap para operação contínua.
3. Definir as pipelines permanentes mínimas:
   - ingestão;
   - auditoria;
   - pedagogia/conteúdo;
   - publicação ou exportação futura, se aplicável;
   - investigação de lacunas.
4. Registrar como fontes grandes entram sem estourar contexto:
   - indexação determinística antes de LLM;
   - classificação antes de mineração;
   - mineração seletiva;
   - processamento por item;
   - retomada por manifesto/fila;
   - deduplicação por hash/ID;
   - validação antes da canonização.
5. Definir o papel de cada executor:
   - Codex/local: scripts, indexação, validação, automação e engenharia do repositório;
   - Gemini/Cloud Code: processamento longo, triagem e mineração assistida;
   - ChatGPT: auditoria cognitiva, síntese e revisão epistemológica;
   - André: decisões materiais, autorização de gates e validação humana.

## Caso real de referência
Google Takeout/Drive é o primeiro caso de uso candidato para a operação contínua, mas não deve ser tratado como fonte já minerada enquanto não houver inventário e manifesto.

Estrutura observada a considerar como caso de teste do contrato:

- `Takeout/Gemini` — metadados/configuração do Gemini;
- `Takeout/NotebookLM` — notebooks organizados e possivelmente ricos para mineração;
- `Takeout/Gemini no Workspace/Conversation History` — histórico bruto de conversas do Gemini Workspace.

## Deliverables
- Documento de transição do bootstrap para operação contínua.
- Estrutura inicial de `pipelines/` ou atualização da estrutura existente.
- Contrato operacional mínimo das pipelines permanentes.
- Definição do primeiro pipeline candidato: ingestão Google Takeout/Drive.
- Relatório em `execucoes/EXEC-GOAL-010.md` com:
  - estado final do bootstrap;
  - pipelines criadas/definidas;
  - pendências;
  - próximos modos de operação;
  - limites não resolvidos.

## Acceptance
- Ficar explícito que GOAL-001–010 compõem o bootstrap inicial.
- Ficar explícito que novas fontes entram por pipelines, não por novos Goals ad hoc.
- O Google Takeout deve estar representado como caso candidato, não como corpus já processado.
- O modelo deve preservar GitHub como estado canônico e Google Drive como fonte.
- O pipeline deve evitar leitura integral de grandes corpora por LLM.
- A operação contínua deve ser incremental, retomável e auditável.
- A distinção ação operacional ≠ conhecimento canônico deve permanecer preservada.

## Validação
- Validar o GOAL-010 contra os contratos produzidos no GOAL-008 e GOAL-009.
- Validar se a estrutura final permite processar Google Takeout sem mover gigabytes para o repositório.
- Executar validações mecânicas disponíveis quando aplicável.
- Registrar explicitamente validações não executadas.

## Stop conditions
Parar se:

- o executor tentar iniciar mineração massiva em vez de definir a operação contínua;
- o Google Drive for tratado como estado canônico em vez de fonte;
- pipelines forem criadas sem contrato, estado, fila ou retomada;
- a operação proposta exigir contexto de LLM proporcional ao tamanho total do corpus.

## Gate
Este Goal está preparado, mas não liberado. Ele só pode ser executado após GOAL-009 estar `CONCLUÍDO` e validado. Quando concluído e validado, encerra o bootstrap inicial do EurekAI e inaugura o modo de pipelines permanentes.
