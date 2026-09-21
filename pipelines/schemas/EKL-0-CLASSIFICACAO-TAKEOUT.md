# EKL-0 — Classificação Takeout

**Estado:** preparado, não executado  
**Uso:** classificação leve de itens do histórico/Takeout  
**Entrada:** metadados + amostra limitada  
**Saída:** JSONL compacto

## Objetivo

Classificar itens inventariados do Takeout sem enviar o corpus inteiro para a LLM.

A classificação decide se um item deve ser descartado, minerado, revisado ou bloqueado.

## Entrada esperada

A IA deve receber, por item, somente o necessário:

- `i`: item_id;
- título, quando houver;
- caminho lógico/redigido, quando permitido;
- tipo/formato;
- contagens geradas por script;
- primeira/última amostra ou trecho delimitado;
- metadados não sensíveis.

Não enviar conteúdo bruto completo nesta fase.

## Saída obrigatória

Uma linha JSON por item, usando apenas:

```text
i, cl, ev, m, cf, rs
```

## Campos

- `i`: item_id.
- `cl`: lista de classes.
- `ev`: valor epistemológico.
- `m`: ação de mineração.
- `cf`: confiança.
- `rs`: razão curta.

## Classes permitidas

- `P`: produto.
- `A`: aprendizado.
- `D`: decisão.
- `G`: governança.
- `E`: execução.
- `O`: operacional.
- `H`: hipótese.
- `R`: erro.
- `F`: fonte/evidência.
- `L`: lacuna.

## Ação de mineração

- `0`: não minerar.
- `1`: minerar.
- `2`: revisar.
- `3`: bloquear.

## Regras de classificação

1. Comando pontual sem reaproveitamento → `cl=["O"]`, `ev=B` ou `N`, `m=0`.
2. Definição de produto, público, promessa ou MVP → incluir `P`.
3. Escolha explícita, regra ou fechamento humano → incluir `D`.
4. Contrato, gate, protocolo, canonização ou regra de agente → incluir `G`.
5. Código, script, PR, erro técnico ou execução de artefato → incluir `E` ou `R` conforme o caso.
6. Explicação, entendimento, modelo mental ou aprendizagem → incluir `A`.
7. Brainstorm sem decisão → incluir `H`, não `D`.
8. Evidência com localizador ou prova de execução → incluir `F`.
9. Ausência, pendência ou coisa a verificar → incluir `L`.
10. Quando a amostra for insuficiente, usar `m=2` ou `m=3`, nunca inventar conteúdo.

## Exemplos

```jsonl
{"i":"T000001","cl":["P","A"],"ev":"A","m":1,"cf":"M","rs":"visão de produto por link"}
{"i":"T000002","cl":["O"],"ev":"N","m":0,"cf":"H","rs":"comando pontual sem conhecimento"}
{"i":"T000003","cl":["D","G"],"ev":"A","m":1,"cf":"H","rs":"define regra canônica do projeto"}
{"i":"T000004","cl":["E","R"],"ev":"M","m":1,"cf":"M","rs":"erro técnico com diagnóstico"}
{"i":"T000005","cl":["L"],"ev":"B","m":2,"cf":"L","rs":"amostra insuficiente"}
```

## Prompt base

```text
Classifique os itens abaixo usando EKL-0.

Regras:
- Saída somente JSONL.
- Uma linha por item.
- Não explique.
- Não repita o dicionário.
- Use apenas campos: i, cl, ev, m, cf, rs.
- Use apenas códigos definidos.
- rs deve ser curto, mas legível.
- Não marque como minerar quando for apenas comando operacional.
- Quando houver dúvida, use m=2 e cf=L ou cf=U.
```

## Condição de validade

Uma classificação EKL-0 válida não prova que o item foi minerado. Ela apenas orienta a próxima etapa da pipeline.
