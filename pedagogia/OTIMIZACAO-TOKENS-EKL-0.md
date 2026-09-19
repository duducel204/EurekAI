# Otimização de tokens com EKL-0

**Estado:** exemplo pedagógico derivado da preparação da leitura do Takeout  
**Relação:** `pipelines/schemas/EKL-0-*`  
**Uso:** explicar um princípio de IA aprendido no desenvolvimento do EurekAI

## Princípio

Uma LLM não precisa repetir cabeçalhos longos quando o schema já é conhecido.

Quando o significado dos campos está fixado em um dicionário, a saída pode ser compacta, validável e expansível.

```text
schema fixo salvo uma vez
↓
registro compacto por item
↓
validação mecânica
↓
expansão quando necessário
↓
uso humano/canonização
```

## Problema observado

Ao pedir que uma IA leia muitas conversas, existe tendência a:

- resumir cedo demais;
- repetir estruturas longas;
- consumir tokens com cabeçalhos padronizados;
- perder rastreabilidade;
- confundir hipótese, decisão e fato;
- transformar interação operacional em conhecimento.

## Solução aplicada

EKL-0 cria uma linguagem compacta controlada para saídas intermediárias.

Exemplo verboso:

```json
{
  "item_uid": "T000123",
  "classification": ["PRODUTO", "APRENDIZADO"],
  "epistemic_value": "alto",
  "should_mine": true,
  "confidence": "media",
  "reason": "define visão de produto por link"
}
```

Exemplo EKL-0:

```jsonl
{"i":"T000123","cl":["P","A"],"ev":"A","m":1,"cf":"M","rs":"visão de produto por link"}
```

## O que é otimizado

Compactar:

- nomes de campos;
- classes;
- status;
- confiança;
- decisão operacional de mineração;
- metadados repetidos.

Preservar em linguagem humana:

- decisão;
- hipótese;
- aprendizado;
- motivo;
- lacuna;
- afirmação semântica principal.

## Regra didática

A otimização correta não é esconder significado. É remover repetição estrutural.

```text
metadados compactos
significado preservado
procedência mantida
validação obrigatória
```

## Relação com pensamento crítico

EKL-0 é um exemplo de como usar IA sem depender de memória ou improviso do modelo.

A estrutura obriga a IA a responder dentro de um contrato, reduzindo:

- variação desnecessária;
- excesso de texto;
- ambiguidade operacional;
- custo de contexto;
- chance de confundir estágios da pipeline.

## Limite

EKL-0 não é linguagem para usuário final e não substitui explicação humana.

No produto por link, o usuário deve receber linguagem simples e acessível. EKL-0 pertence ao bastidor técnico do repositório.

## Aprendizado canonizável

Separar **schema** de **registro** é uma técnica de economia cognitiva e operacional.

A IA trabalha melhor quando:

1. o formato esperado é fixo;
2. códigos são definidos antes;
3. campos semânticos importantes continuam legíveis;
4. scripts validam a forma;
5. humanos validam o significado.
