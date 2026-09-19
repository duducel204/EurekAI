# Lote inicial de unidades de conhecimento — U-001

**Contrato:** [CONTRATO-UNIDADE-DE-CONHECIMENTO.md](CONTRATO-UNIDADE-DE-CONHECIMENTO.md)
**Estado:** PRODUZIDO PELO GOAL-008; aguardando auditoria do GOAL-009.

## UC-001 — Verificação em um ambiente não prova funcionamento em outro

- **Objetivo:** distinguir o que um teste automatizado demonstra do que continua sem validação em hardware/ambiente diferente.
- **Origem:** L-004; [E-015](../experiencias/INVENTARIO-EVIDENCIAS-002.md); [R-001](../mapa-do-conhecimento/RELACOES-001.md); trilha B de [PROGRESSAO-001](../pedagogia/PROGRESSAO-001.md).
- **Evidências:** E-015 mostra código de teste, workflow e CI concluída no runner. Não comprova execução no aparelho.
- **Relações:** R-001 fornece contexto compartilhado com a separação do projeto; não fornece causalidade nem dependência.
- **Hipóteses:** apresentar primeiro a diferença entre ambientes é escolha pedagógica, não ordem histórica ou cognitiva demonstrada.
- **Mecanismo atemporal:** um resultado de teste é válido para as condições observadas. Mudar sistema operacional, arquitetura, dependências, permissões ou hardware cria outro conjunto de condições que precisa de validação própria.
- **Exemplo versionado:** Aindre-termux-tradutor em `f29de5b2deb2efe421a138a920516b9e93823a2fd`; CI `35187509452`. O exemplo demonstra execução no runner, não no Android de André.
- **Representação inicial:** um ensaio de ponte em maquete verifica a maquete; a ponte real ainda precisa de inspeção no terreno. Isto é analogia, não descrição do software.
- **Representação alternativa:** tabela com colunas “condição testada”, “resultado observado” e “condição ainda não testada”.
- **Terminologia:** ambiente de execução, runner de CI, validade de teste, portabilidade, evidência.
- **Experimento:** executar o mesmo teste em dois ambientes controlados, registrar versões e comparar; se o segundo ambiente não estiver disponível, registrar `não executado`.
- **Tags:** `#mcp #termux #artefato #construcao #autoria-incerta`.
- **Confiança:** alta para o mecanismo geral; moderada para o uso deste exemplo, porque autoria intelectual e aparelho físico não foram resolvidos.
- **Lacunas:** falta log de execução no aparelho e resolução de autoria/contribuição.
- **Executor:** Codex, síntese sobre corpus versionado.
- **Geração:** 2026-09-19; unidade v1; framework pedagógico v1.

## UC-002 — Direção arquitetural e implementação concluída são estados diferentes

- **Objetivo:** compreender por que uma decisão de projeto não deve ser lida como recurso pronto.
- **Origem:** L-004; [E-017 e E-018](../experiencias/INVENTARIO-EVIDENCIAS-002.md); [R-003](../mapa-do-conhecimento/RELACOES-001.md); trilha A de [PROGRESSAO-001](../pedagogia/PROGRESSAO-001.md).
- **Evidências:** E-017 documenta prioridade por processamento local e privacidade. E-018 registra tradução offline como não concluída.
- **Relações:** R-003 sustenta coexistência contextual tensionada. Não demonstra que a decisão cause a lacuna nem que tradução seja requisito universal.
- **Hipóteses:** usar a tensão decisão–lacuna como gancho pedagógico é escolha didática candidata.
- **Mecanismo atemporal:** requisitos, decisões e implementação possuem estados próprios. Uma decisão orienta trabalho futuro; somente evidência de implementação e validação sustenta que o comportamento existe.
- **Exemplo versionado:** `DECISIONS.md` e `STATUS.md` do Aindre-termux-tradutor em `f29de5b2deb2efe421a138a920516b9e93823a2fd`. São documentos do projeto, não confirmação pessoal de André.
- **Representação inicial:** escolher um destino no mapa não significa ter chegado; a rota escolhida e a posição atual são informações diferentes.
- **Representação alternativa:** quadro de estados `pretendido → implementado → validado`, permitindo “pendente” sem chamar de falha definitiva.
- **Terminologia:** requisito, decisão arquitetural, implementação, validação, lacuna, rastreabilidade.
- **Experimento:** classificar afirmações de um projeto em “direção”, “artefato existente”, “resultado validado” e “pendência”, citando a fonte de cada uma.
- **Tags:** `#termux #decisao #documento #pendencia #autoria-incerta`.
- **Confiança:** alta para o mecanismo geral; moderada para a síntese do caso, pois os autores dos documentos não estão resolvidos.
- **Lacunas:** implementação posterior pode ter alterado o estado; revalidar o commit antes de usar o exemplo como estado atual.
- **Executor:** Codex, síntese sobre corpus versionado.
- **Geração:** 2026-09-19; unidade v1; framework pedagógico v1.
