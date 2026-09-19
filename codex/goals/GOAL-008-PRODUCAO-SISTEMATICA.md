# GOAL-008 — Produção sistemática de unidades de conhecimento

**Status:** PREPARADO — NÃO LIBERADO
**Executor-alvo:** QUALQUER EXECUTOR AUTORIZADO
**Dependência:** GOAL-007 concluído, revalidado e validado
**Sequência:** primeiro passo da sequência 008→009→010

## Intent
Produzir as primeiras unidades sistemáticas de conhecimento do EurekAI a partir do corpus já validado, criando ao mesmo tempo o contrato mínimo de uma unidade reutilizável.

O objetivo não é publicar conteúdo final nem escolher uma interface. O objetivo é transformar o framework pedagógico do GOAL-007 em unidades rastreáveis, auditáveis e reaproveitáveis por agentes futuros.

## Premissa nova incorporada
O EurekAI passa a tratar grandes fontes históricas, como Google Takeout, NotebookLM, Google Drive, ChatGPT Export, GitHub, documentos e conversas, como **fontes de ingestão**. Porém o GOAL-008 ainda não executa a ingestão massiva dessas fontes.

Este Goal define o formato da saída que qualquer ingestão futura deverá produzir: uma unidade de conhecimento com procedência, metadados e limites claros.

## Operação
1. Consumir os artefatos validados dos GOALs 005–007:
   - `mapa-do-conhecimento/RELACOES-001.md`;
   - `pedagogia/PROGRESSAO-001.md`;
   - `pedagogia/FRAMEWORK-PEDAGOGICO.md`;
   - relatórios de execução/revalidação em `execucoes/`.
2. Definir o contrato canônico de uma unidade de conhecimento.
3. Produzir um lote pequeno de unidades reais, suficiente para testar o contrato.
4. Preservar separação entre:
   - evidência;
   - relação;
   - hipótese;
   - escolha pedagógica;
   - mecanismo atemporal;
   - exemplo versionado;
   - decisão de executor.
5. Registrar lacunas e pontos que exigem auditoria no GOAL-009.

## Contrato mínimo de unidade
Cada unidade deve registrar, quando aplicável:

- `id` estável;
- título;
- objetivo de compreensão;
- origem/fonte;
- evidências utilizadas;
- relações utilizadas;
- hipóteses utilizadas;
- mecanismo atemporal;
- exemplos versionados;
- representação/analogia inicial;
- alternativa de representação;
- terminologia técnica;
- experimento ou aplicação;
- tags;
- nível de confiança;
- lacunas;
- executor;
- data/versão de geração;
- versão do framework pedagógico usado.

Campos podem ser omitidos somente quando a omissão for explicitamente justificada.

## Pipeline candidato
`evidência + tags + relações + progressão + framework pedagógico → unidade de conhecimento → fila de auditoria`

## Deliverables
- Um contrato de unidade em `conhecimento/` ou `pedagogia/`, conforme a estrutura vigente.
- Um lote inicial pequeno de unidades reais derivadas do corpus já validado.
- Um relatório em `execucoes/EXEC-GOAL-008.md` contendo:
  - unidades produzidas;
  - fontes/evidências usadas;
  - hipóteses preservadas;
  - lacunas;
  - itens enviados para auditoria no GOAL-009.

## Acceptance
- Nenhuma unidade pode perder procedência.
- Nenhuma hipótese pode ser promovida a fato.
- Nenhuma sequência pedagógica pode ser tratada como pré-requisito técnico sem evidência.
- Toda unidade deve distinguir mecanismo atemporal de ferramenta/versão.
- O lote inicial deve ser pequeno o suficiente para auditoria completa no GOAL-009.
- O resultado deve servir de formato de saída para pipelines futuros de ingestão, incluindo Google Takeout, sem depender de Google Takeout para existir.

## Validação
- Revisar consistência das unidades contra GOAL-005, GOAL-006 e GOAL-007.
- Executar validações mecânicas disponíveis (`check_all.py`, links, tags) quando aplicável.
- Registrar explicitamente qualquer validação não executada.

## Stop conditions
Parar se:

- não houver evidência suficiente para produzir unidade real;
- a unidade exigir inferência não suportada;
- o executor tentar decidir UI, produto, plataforma comercial ou publicação;
- o formato começar a duplicar corpus bruto em vez de sintetizar conhecimento rastreável.

## Gate
Este Goal está preparado, mas não liberado. Em uma sequência autorizada 008→009→010, ele deve ser executado primeiro; somente após `CONCLUÍDO` e validado o GOAL-009 pode atravessar seu gate de entrada.
