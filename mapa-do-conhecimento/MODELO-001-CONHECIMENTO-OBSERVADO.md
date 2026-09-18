# Modelo inicial do conhecimento observado — recorte M-001

**Estado:** índice experimental de evidências, não classificação de domínio.  
**Base:** `main@b3a1d0b71b8bd3d44b2f876b118fbce762ecbd87`.  
**Corpus modelado:** [L-004/L-005](../fontes/REGISTRO.md), seis observações E-014–E-019 do [inventário auditável](../experiencias/INVENTARIO-EVIDENCIAS-002.md).  
**Fora da matriz inferencial:** L-003, E-001–E-013, preservadas na [auditoria de procedência](../experiencias/AUDITORIA-EVIDENCIAS-001.md) como pistas sem localizador individual. L-001/L-002 servem como contexto e histórico de construção, não como prova independente de capacidade pessoal.

## Como ler

Cada linha aponta a **uma unidade de evidência já existente**. Tags são lentes de recuperação, não resultados de avaliação. “Evento” descreve o que o artefato mostra ou relata; o campo de limite controla a inferência. Uma mesma fonte em duas linhas não cria corroboração independente. O login de commit não resolve identidade civil, autoria intelectual nem participação de IA. Datas de commit não datam automaticamente eventos narrados dentro de documentos.

## Matriz de consulta

| Evidência | Tags sustentadas | Projeto/contexto | Evento observável e objeto | Tipo/limite |
| --- | --- | --- | --- | --- |
| [E-014](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#mcp #github #termux #decisao #mudanca-de-direcao #autoria-incerta` | Aindre Termux e separação do repositório Windows | Decisão **documentada/versionada** de separar projetos; README + commit | Atribuição à conta GitHub no commit; concepção individual não demonstrada. |
| [E-015](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#mcp #termux #artefato #construcao #autoria-incerta` | Aindre Termux; teste e CI | Código de teste da ponte, workflow e CI concluída com sucesso | Execução no runner; não comprova aparelho nem autoria intelectual. |
| [E-016](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#mcp #termux #documento #experiencia #autoria-incerta` | Aindre Termux; STATUS | **Relato** de chamada `termux_exec` com saída e `exit_code: 0` | Log original e ator da chamada não localizados; `#experiencia` etiqueta o relato, não valida execução pessoal. |
| [E-017](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#termux #decisao #documento #autoria-incerta` | Aindre Termux; DECISIONS | Prioridades declaradas de processamento local, privacidade e wizard idempotente | Direção do projeto; implementação e confirmação pessoal não demonstradas. |
| [E-018](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#termux #pendencia #documento` | Aindre Termux; STATUS/DECISIONS | Tradução offline declarada não concluída | Contraevidência a uma leitura de “tradutor local pronto”; não prova incapacidade de alguém. |
| [E-019](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | `#agentes #artefato #construcao #autoria-incerta` | DTGEapp; contratos/canonizações | Artefatos de governança multiagente existem na árvore | Execução de agentes e contribuição individual não comprovadas. |

`#termux` foi adicionada ao [índice de tags](INDEX-TAGS.md) por conectar cinco unidades no mesmo contexto técnico. `#mcp`, `#agentes`, tipos de item, eventos e `#autoria-incerta` já pertenciam ao vocabulário experimental. Não foram atribuídas tags de diagnóstico, solução ou reaplicação pessoal: o corpus não mostra a sequência e o ator necessários.

## Lentes úteis sem duplicar o corpus

- **Assuntos e contextos:** `#mcp #termux` recupera E-014–E-016; `#agentes` recupera E-019. `#termux #decisao` recupera E-014/E-017, que são decisões de projeto de naturezas distintas.
- **Tipo de evento:** `#artefato #construcao` mostra E-015/E-019; `#documento #autoria-incerta` mostra E-016/E-017; `#pendencia` mostra E-018. Essa consulta não ordena proficiência.
- **Conexões candidatas:** C-001 (E-014/E-015/E-016) reúne separação de projetos, teste de ponte e relato de uso no contexto Termux. C-002 (E-017/E-018) coloca direção de processamento local ao lado de tradução offline ainda aberta. São interseções de contexto, não causalidade nem transferência pessoal.
- **Tensão T-001:** em DTGEapp, o README descreve módulos ativos cujos nomes não aparecem na árvore do commit inspecionado; a memória relata correções, mas reconhece ausência de teste integrado. Referências e limite estão no [inventário 002](../experiencias/INVENTARIO-EVIDENCIAS-002.md). E-019 sustenta artefatos, não a alegação de execução.

## Dimensão cognitiva e participação humano–IA

| Sinal pedido pelo GOAL-004 | Resultado neste recorte |
| --- | --- |
| Conceito antes do nome / nome antes da compreensão | **Não demonstrado.** Faltam eventos datados de formulação pessoal e explicação/uso posterior; menção de termo não prova incompreensão. |
| Transição mental / reaprendizagem | **Não demonstrada.** Documentos fixam estados de projeto, sem sequência pessoal antes/depois. |
| Transferência entre projetos | **Candidata apenas como pergunta.** Sem origem pessoal e reaplicação posterior verificáveis, não etiquetar `#reaplicacao`. |
| Conhecimento tácito | **Não inferível** de autoria incerta ou código isolado. Exigiria ação recorrente atribuível e ausência de articulação em corpus suficiente. |
| Participação de IA | **Não determinável** para E-014–E-019. A CI executou automaticamente; isso não resolve quem propôs, escreveu, aceitou ou corrigiu cada artefato. |

## Derivações reutilizáveis, ainda não decisões dos Goals seguintes

- **GOAL-005:** C-001/C-002 e T-001 são pontos de partida para testar relações com direção e força. Não há pré-requisito conceitual ou transferência comprovados.
- **GOAL-006:** faltam sequências de aprendizagem atribuídas e datadas; nenhuma ordem pedagógica deriva deste índice.
- **GOAL-007/008:** a distinção “CI passou ↔ aparelho funcionou” e “direção declarada ↔ recurso concluído” pode fornecer casos didáticos se a execução e os fatos forem validados; não são capítulos.
- **GOAL-009:** checar localizadores de L-003, identidade/autoria, logs de Termux e módulos DTGE antes de elevar evidência.
- **GOAL-010:** novas fontes podem ser indexadas por ID/lote e tags, sem duplicar os inventários. Reavaliar clusters quando houver observações independentes.

## Limites de cobertura e próxima consulta

O modelo responde quais temas/eventos/documentos aparecem **neste recorte** e aponta as fontes por ID. Não representa todo o conhecimento de André. O [ticket INV-001](../investigacao/pendencias/INV-001-CORPUS-HISTORICO.md) continua parcial para recuperar originais do L-003 e ampliar a cobertura. Nenhuma categoria, nível de domínio ou mapa físico separado foi criado.
