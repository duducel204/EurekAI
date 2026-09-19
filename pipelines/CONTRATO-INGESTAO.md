# Contrato geral de ingestão — v1

**Estado:** CANÔNICO APÓS AUDITORIA DO GOAL-009
**Unidade de trabalho:** uma conversa, documento ou artefato individual; nunca o corpus inteiro em um único contexto de LLM.

## Princípios

GitHub guarda manifestos, contratos, evidências derivadas e conhecimento canonizado. A fonte pode permanecer no Drive, exportação ou armazenamento autorizado. Referência segura prevalece sobre cópia pública. Ação operacional não vira conhecimento por padrão.

## Funil retomável

| Etapa | Entrada → saída | Executor padrão | Estado persistido |
| --- | --- | --- | --- |
| 1. Registro da fonte | origem/autorização → `source_id` | humano + código | manifesto da fonte, acesso e limites |
| 2. Inventário | árvore/exportação → itens | código determinístico | `item_id`, caminho lógico, formato, tamanho, datas disponíveis |
| 3. Indexação | itens → índice | código determinístico | hash, contagens, relações de contêiner, cursor/checkpoint |
| 4. Deduplicação | índice → grupos | código determinístico | hash exato; similaridade apenas como candidata |
| 5. Classificação | metadados/amostra → classe/prioridade | regras; LLM leve somente para ambiguidade | classe, justificativa, modelo/prompt quando houver |
| 6. Mineração seletiva | itens relevantes → evidências/hipóteses | LLM com procedência por trecho | derivação, localizador, limites, assistência |
| 7. Validação | derivação + origem → aceita/corrigir/rejeitar | código + LLM/revisor | resultado, motivo e versão |
| 8. Canonização | validado → unidade/decisão/relação | executor autorizado | commit/PR; nunca merge automático |

Estados por item: `INVENTARIADO`, `CLASSIFICADO`, `SELECIONADO`, `MINERADO`, `VALIDADO`, `CANONIZADO`, `DESCARTADO` ou `BLOQUEADO`. Toda transição registra horário, executor, versão do processo e ponteiro para a entrada. Um item com falha retoma do último estado confirmado.

## Classes mínimas

- **OPERACIONAL:** comando, consulta ou ação pontual. Pode gerar log/experiência, mas não conhecimento por padrão.
- **EXECUÇÃO:** produção ou alteração de artefato. Pode gerar experiência/evidência.
- **EXPLORAÇÃO:** hipótese, comparação ou brainstorm. Não vira decisão.
- **APRENDIZADO:** explicação, reconstrução ou teste de compreensão. Pode gerar candidato a conhecimento.
- **DECISÃO:** escolha explícita com escopo e ator resolvidos.
- **GOVERNANÇA:** contrato, gate, protocolo ou regra.

Classificação pode ser múltipla quando trechos têm funções diferentes. Descarte significa “fora do escopo desta rodada”, preservando ID e motivo; não significa inexistência ou irrelevância universal.

## Código tradicional e LLM

**Código basta:** descoberta de arquivos, hashes, MIME/extensão, tamanhos, datas disponíveis, IDs, contagens, parsing estrutural conhecido, filas, checkpoints, duplicatas exatas, validação de schema/links/tags e relatórios quantitativos.

**LLM pode ser necessário:** classificação semântica ambígua, extração de afirmações, separação de vozes, síntese, detecção de hipótese/tensão, analogias e revisão epistemológica. A saída do LLM é derivação até validação; deve registrar modelo/configuração ou identificador de execução quando disponível.

## Deduplicação e linhagem

Hash idêntico consolida conteúdo binariamente igual, preservando todas as ocorrências. Conteúdo semelhante recebe relação `POSSÍVEL_DUPLICATA` e revisão; não se soma como corroboração. Cada unidade final aponta aos IDs de evidência e estes apontam a item, fonte, versão e localizador. Mudança na fonte cria nova versão e invalida apenas derivações dependentes.

## Custo, contexto e privacidade

Inventariar e filtrar antes de enviar conteúdo a LLM. Processar um item ou trecho delimitado por vez; limitar tamanho e usar resumo anterior somente com ponteiros verificáveis. Não registrar tokens, callbacks, credenciais, áudios ou dados de terceiros no GitHub. Uma política específica da fonte define retenção, redação e armazenamento.

## Caso de teste Google Takeout/Drive

As localizações observadas são somente candidatas:

- `Takeout/Gemini` — inventariar formatos e metadados antes de inferir conteúdo;
- `Takeout/NotebookLM` — cada notebook/documento é item; não presumir riqueza ou autoria;
- `Takeout/Gemini no Workspace/Conversation History` — cada conversa é unidade preferencial de classificação.

Drive permanece fonte; GitHub permanece estado canônico. O contrato não afirma acesso atual nem processamento dessas pastas. O primeiro passo futuro é um manifesto local com hashes/contagens e sem copiar gigabytes para o repositório.

## Saída de conhecimento

Itens validados que justificarem conhecimento usam [o contrato de unidade](../conhecimento/CONTRATO-UNIDADE-DE-CONHECIMENTO.md). Conteúdo operacional pode terminar como `DESCARTADO` ou experiência, sem produzir unidade. Canonização exige validação e PR revisável.
