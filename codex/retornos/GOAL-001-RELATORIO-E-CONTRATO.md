# GOAL-001 — Inspeção e contrato operacional

**Referência inspecionada:** `main@e0d091e1e20a46188d84895f1c36b324c1f53010`  
**Estado:** proposta para revisão; GOAL-002 não iniciado.

## Inspeção

Foram lidos a [árvore completa](https://api.github.com/repos/duducel204/EurekAI/git/trees/e0d091e1e20a46188d84895f1c36b324c1f53010?recursive=1), os 17 arquivos versionados e o [histórico de 17 commits](https://github.com/duducel204/EurekAI/commits/main/). O repositório tem 14 diretórios de primeiro nível. Exceto pelo [contexto de origem](../../contexto/ORIGEM-E-DIRECAO.md) e pelo [GOAL-001](../goals/GOAL-001-CONTRATO-OPERACIONAL.md), os arquivos são READMEs que descrevem áreas ainda sem registros individuais. Não há código versionado nem registros individuais de experiência ou conhecimento.

| Área | Função declarada no README | Estado |
| --- | --- | --- |
| `capturas/` | Entrada bruta sem validação implícita | Só README |
| `codex/` | Mecanismo de construção separado do conteúdo | README e subáreas |
| `codex/goals/` | Objetivos convergidos | README e GOAL-001 |
| `codex/retornos/` | Retornos, evidências e lacunas | Só README antes deste retorno |
| `conhecimento/` | Conhecimento estruturado em algum grau | Só README |
| `contexto/` | Origem e direção exploratória | ORIGEM-E-DIRECAO.md |
| `decisoes/` | Decisões com contexto e motivo | Só README |
| `descobertas/` | Descobertas do estudo e prática | Só README |
| `erros/` | Problemas, tentativas e soluções | Só README |
| `experiencias/` | Experiências práticas | Só README |
| `hipoteses/` | Possibilidades não confirmadas | Só README |
| `ideias-de-produto/` | Possibilidades futuras sem aprovação implícita | Só README |
| `mapa-do-conhecimento/` | Conexões, dependências e lacunas | Só README |
| `pedagogia/` | Estudo futuro de aprendizagem progressiva | Só README |
| `templates/` | Modelos após validação | Só README |

O documento de contexto deixa níveis, ordem e taxonomia em aberto. Site, aplicativo e jogo são possibilidades futuras, não decisões de execução.

## Inventário de fontes

O estado indica acesso confirmado nesta inspeção. Possibilidade técnica de ingestão não significa fonte já acessível.

| Fonte | Classificação | Evidência ou condição |
| --- | --- | --- |
| Repositório EurekAI em `main` | **DISPONÍVEL** | Árvore e 17 arquivos lidos. |
| Histórico Git do EurekAI | **DISPONÍVEL** | 17 commits listados; não comprovam domínio do autor. |
| Contexto e GOAL-001 | **DISPONÍVEL** | Lidos integralmente. |
| Experiências, erros, soluções e capturas individuais no EurekAI | **NÃO DISPONÍVEL** | Áreas correspondentes contêm só README. |
| Outros repositórios e documentação de projetos | **NÃO DISPONÍVEL como fontes identificadas** | Nenhum endereço foi indicado pelos arquivos examinados; cada acesso deve ser testado quando identificado. |
| Conversas e handoffs históricos | **PRECISA SER EXPORTADA**; **EXIGE INTERVENÇÃO DO ANDRÉ** | Nenhum corpus foi fornecido no repositório. Uma exportação selecionada **PODE SER AUTOMATIZADA** para ingestão após disponibilização e revisão. |
| Código e registros históricos externos de erros/soluções | **PRECISA SER EXPORTADA** ou vinculada | Não encontrados na árvore examinada; origem e permissão ainda desconhecidas. |

Nenhuma fonte ausente foi tratada como evidência sobre o conhecimento do autor.

## Contrato operacional mínimo proposto

1. Ler o Goal, o contexto pertinente e a árvore atual. Registrar a referência Git inspecionada. Distinguir PLAN de EXECUTE; não iniciar outro Goal por implicação.
2. Para cada afirmação aproveitada, registrar enunciado, origem identificável (URL/caminho e trecho específico), data conhecida ou “desconhecida”, autoria quando identificável, tipo epistemológico, inferência feita e estado de confirmação. Não completar campos ausentes por suposição.
3. Separar **FATO** (observação verificável), **EVIDÊNCIA** (registro de suporte), **EXPERIÊNCIA** (ação/tentativa documentada), **HIPÓTESE** (interpretação pendente) e **DECISÃO** (escolha explícita do autor). Preservar **TENSÃO**, **LACUNA**, **NÃO DECIDIDO** e **CONHECIMENTO TÁCITO** como estados distintos. Uma proposta do assistente permanece proposta até confirmação.
4. Distinguir observação de inferência. Pergunta prova exposição; uso documentado sustenta prática naquele contexto; solução ou explicação própria sustenta compreensão mais específica. Nenhum sinal isolado autoriza afirmar domínio. Registrar contraevidência e incerteza.
5. Preservar a fonte bruta e ligar sínteses a ela. Confirmar uma decisão com o autor antes de promovê-la. Revisar sínteses sem apagar versões ou conflitos. Preferir referência à duplicação de conteúdo.
6. No retorno, informar alterações, evidências, validação, lacunas e decisões pendentes. Parar diante de credencial, dados privados, sobrescrita, ambiguidade arquitetônica material ou impossibilidade de concluir sem inventar fatos.

Este contrato não estabelece esquema de dados nem taxonomia pedagógica definitiva.

## Riscos e mitigação

| Risco | Medida mínima |
| --- | --- |
| Exposição confundida com domínio | Registrar o ato observado e o limite da inferência; não atribuir proficiência sem critérios aprovados e evidências suficientes. |
| Interpretação do assistente atribuída ao autor | Registrar autoria e confirmação; só escolha explícita vira decisão. |
| Perda de contexto | Manter fonte e trecho; preservar bruto e histórico Git. |
| Duplicação e versões conflitantes | Referência estável, registro de tensão e revisão sem apagar versões. |
| Drift de fonte | Fixar commit e revalidar antes de cada Goal. |
| Exposição de conversas ou dados de terceiros | André seleciona o corpus e revisa dados sensíveis antes da importação. |
| Estrutura provisória tratada como definitiva | Tratar diretórios como áreas de trabalho e validar organização com evidências. |

## Prontidão para GOAL-002

**Estrutura suficiente para planejar; corpus insuficiente para reconstrução substancial.** Há contexto, Goal, histórico e áreas de trabalho, mas não há registros individuais de ações, soluções, conversas ou projetos que sustentem inferências sobre o mapa de conhecimento de André. GOAL-002 pode ser preparado após revisão deste retorno. Sua execução depende de fontes reais selecionadas e testadas. Não foi iniciado aqui.

## Perguntas para André antes da execução do GOAL-002

1. Quais conversas, projetos, repositórios ou exportações devem formar o corpus inicial, e onde estarão acessíveis?
2. Quais fontes privadas ou de terceiros devem ser excluídas ou redigidas antes de entrar no repositório?

Essas respostas não eram necessárias para concluir a inspeção do GOAL-001.
