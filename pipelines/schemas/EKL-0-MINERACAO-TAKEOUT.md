# EKL-0 — Mineração Takeout

**Estado:** preparado, não executado  
**Uso:** mineração seletiva de itens classificados  
**Entrada:** item ou trecho autorizado  
**Saída:** JSONL compacto com extrações

## Objetivo

Extrair decisões, hipóteses, aprendizados, produto, governança, erros, evidências, lacunas e relações de itens relevantes do histórico/Takeout.

A mineração só deve ocorrer depois de inventário, classificação e autorização da unidade de trabalho.

## Saída obrigatória

Uma linha JSON por item, usando:

```text
i, x
```

Cada elemento de `x` usa:

```text
k, r, v, cf
```

## Campos

- `i`: item_id.
- `x`: lista de extrações.
- `k`: tipo da extração.
- `r`: localizador dentro do item.
- `v`: valor semântico extraído.
- `cf`: confiança.

## Tipos de extração

- `DEC`: decisão.
- `HIP`: hipótese.
- `APR`: aprendizado.
- `PRO`: produto.
- `GOV`: governança.
- `ERR`: erro.
- `EVD`: evidência.
- `LAC`: lacuna.
- `REL`: relação.

## Regras semânticas

1. Não inventar decisão.
2. Não transformar hipótese em fato.
3. Não promover comando operacional a conhecimento.
4. Não resumir o item inteiro quando houver apenas trecho relevante.
5. Não usar informação fora do trecho fornecido.
6. Preservar localizador em `r`.
7. Manter `v` curto, fiel e legível.
8. Quando o item for operacional sem valor reutilizável, retornar `x: []`.
9. Quando houver lacuna, registrar `k=LAC`.
10. Relações (`REL`) devem indicar associação observada, não causalidade, salvo evidência explícita.

## Exemplos

```jsonl
{"i":"T000001","x":[{"k":"PRO","r":"m14-m22","v":"EurekAI deve ensinar IA desde a base zero por link.","cf":"H"},{"k":"DEC","r":"m30-m34","v":"Minijogo é evolução futura, não requisito do MVP.","cf":"M"},{"k":"LAC","r":"m40-m41","v":"Ainda falta especificar fluxo real da primeira experiência por link.","cf":"H"}]}
{"i":"T000002","x":[]}
{"i":"T000003","x":[{"k":"GOV","r":"m5-m12","v":"Agentes devem consultar o GitHub antes de continuar o projeto.","cf":"H"}]}
```

## Prompt base

```text
Minere o item abaixo usando EKL-0.

Regras:
- Saída somente JSONL.
- Uma linha para o item.
- Use campos: i, x.
- x é lista de extrações.
- Cada extração usa: k, r, v, cf.
- Preserve o texto semântico em v de forma curta, clara e fiel.
- Não invente decisão.
- Não transforme hipótese em fato.
- Não use informação fora do trecho.
- Se houver lacuna, registre k=LAC.
- Se for operacional sem valor reutilizável, retorne x vazio.
```

## Condição de validade

Mineração EKL-0 é derivação. Antes de canonizar, deve ser validada contra o trecho original e expandida para o formato humano adequado quando necessário.
