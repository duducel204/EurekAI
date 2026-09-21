# EKL-0 — Dicionário canônico

**Nome:** EurekAI Compact Language v0  
**Estado:** experimental controlado  
**Uso inicial:** leitura do histórico/Takeout de André  
**Camada:** intermediária, pré-canonização

## Propósito

EKL-0 reduz repetição de metadados nas saídas de classificação e mineração por LLM.

A ideia é manter o schema completo documentado uma vez e fazer a IA devolver apenas registros compactos.

```text
schema fixo + dicionário → registros compactos → validação → expansão opcional → canonização humana
```

## Limites

EKL-0 não substitui:

- `conhecimento/`;
- `decisoes/`;
- `produto/`;
- `pedagogia/`;
- auditoria;
- validação semântica;
- documentação humana.

EKL-0 também não autoriza leitura massiva do Takeout. Ele só define formato de saída quando uma etapa de classificação ou mineração já estiver autorizada.

## Campos gerais

| Código | Significado | Uso |
| --- | --- | --- |
| `i` | item_id | identificador compacto do item |
| `s` | source_id | fonte/lote quando necessário |
| `cv` | conversation_id | conversa, quando existir |
| `r` | range/localizador | mensagens, linhas, seção ou trecho |
| `cl` | classes | lista de classes compactas |
| `ev` | valor epistemológico | valor estimado do item |
| `m` | ação de mineração | decisão operacional pós-classificação |
| `cf` | confiança | confiança na classificação ou extração |
| `rs` | razão curta | motivo curto e legível |
| `x` | extrações | lista de extrações na mineração |
| `k` | tipo da extração | tipo do elemento extraído |
| `v` | valor semântico | conteúdo extraído em linguagem humana |
| `lk` | lacuna | lacuna observada quando separada de `x` |
| `p` | path lógico | caminho lógico/redigido quando aplicável |
| `tp` | tipo/formato | extensão, MIME ou formato lógico |
| `sz` | size_bytes | tamanho em bytes |
| `h` | hash | hash calculado por código determinístico |
| `mc` | message_count | contagem aproximada de mensagens |
| `st` | status | estado do item na pipeline |

## Classes (`cl`)

| Código | Classe |
| --- | --- |
| `P` | produto |
| `A` | aprendizado |
| `D` | decisão |
| `G` | governança |
| `E` | execução |
| `O` | operacional |
| `H` | hipótese |
| `R` | erro |
| `F` | fonte/evidência |
| `L` | lacuna |

## Valor epistemológico (`ev`)

| Código | Valor |
| --- | --- |
| `A` | alto |
| `M` | médio |
| `B` | baixo |
| `N` | nulo |

## Ação de mineração (`m`)

| Código | Ação |
| --- | --- |
| `0` | não minerar |
| `1` | minerar |
| `2` | revisar |
| `3` | bloquear |

## Confiança (`cf`)

| Código | Confiança |
| --- | --- |
| `H` | alta |
| `M` | média |
| `L` | baixa |
| `U` | indefinida |

## Tipos de extração (`k`)

| Código | Tipo |
| --- | --- |
| `DEC` | decisão |
| `HIP` | hipótese |
| `APR` | aprendizado |
| `PRO` | produto |
| `GOV` | governança |
| `ERR` | erro |
| `EVD` | evidência |
| `LAC` | lacuna |
| `REL` | relação |

## Status de pipeline (`st`)

| Código | Status |
| --- | --- |
| `INV` | inventariado |
| `IDX` | indexado |
| `CLS` | classificado |
| `SEL` | selecionado |
| `MIN` | minerado |
| `VAL` | validado |
| `CAN` | canonizado |
| `DSC` | descartado nesta rodada |
| `BLQ` | bloqueado |

## Regras de escrita

1. Usar JSONL: uma linha JSON por item.
2. Não repetir o dicionário na saída da IA.
3. Não usar campos fora do dicionário sem revisão do schema.
4. Não codificar o campo `v` de modo que o significado fique ilegível.
5. `rs` deve ser curto, mas compreensível.
6. Quando houver dúvida, usar `m=2` e `cf=L` ou `cf=U`.
7. Saída EKL-0 é derivação, não conhecimento final.

## Exemplo de classificação

```jsonl
{"i":"T000123","cl":["P","A"],"ev":"A","m":1,"cf":"M","rs":"visão de produto por link"}
```

## Exemplo de mineração

```jsonl
{"i":"T000123","x":[{"k":"PRO","r":"m14-m22","v":"EurekAI deve ensinar IA desde a base zero por link.","cf":"H"},{"k":"LAC","r":"m40-m41","v":"Ainda falta especificar fluxo real da primeira experiência por link.","cf":"H"}]}
```

## Regra de canonização

Nada em EKL-0 entra automaticamente em `conhecimento/`, `produto/`, `decisoes/` ou `pedagogia/`.

Primeiro deve haver validação contra a fonte e transformação para formato humano apropriado.
