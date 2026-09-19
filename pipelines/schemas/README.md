# Schemas de pipeline

**Estado atual:** área preparada para formatos intermediários de pipeline. O primeiro schema definido é o EKL-0, usado inicialmente para leitura compacta do histórico/Takeout de André.

## Função

`pipelines/schemas/` guarda contratos de formato para saídas intermediárias de inventário, classificação, mineração e validação.

A função desta pasta é separar:

```text
schema fixo = significado dos campos e códigos
registro compacto = saída gerada por IA ou script para cada item
```

Isso reduz repetição, custo de tokens e ambiguidade operacional sem remover procedência.

## EKL-0

EKL-0 significa **EurekAI Compact Language v0**.

É uma linguagem compacta controlada, baseada em JSONL, para classificação e mineração do histórico/Takeout.

Uso inicial autorizado:

- leitura do histórico/Takeout de André;
- classificação leve de conversas, notebooks, documentos e artefatos;
- mineração seletiva de itens autorizados;
- produção de registros intermediários antes da canonização.

EKL-0 não é:

- formato final de conhecimento;
- linguagem do produto por link;
- substituto de documentação humana;
- substituto de validação;
- autorização para mineração massiva;
- prova de que uma fonte foi processada.

## Arquivos

- `EKL-0-DICIONARIO.md`: dicionário canônico de campos, códigos e limites.
- `EKL-0-CLASSIFICACAO-TAKEOUT.md`: contrato de saída compacta para classificação leve.
- `EKL-0-MINERACAO-TAKEOUT.md`: contrato de saída compacta para mineração seletiva.

## Relação com a pipeline Takeout/Drive

A pipeline Takeout/Drive continua seguindo:

```text
fonte → manifesto → inventário → indexação → deduplicação → classificação → mineração seletiva → validação → canonização
```

EKL-0 entra apenas nas etapas de classificação e mineração seletiva, como formato intermediário compacto.

## Regra de preservação semântica

Compactar metadados e códigos. Não compactar até destruir significado.

O campo semântico principal (`v`) e motivos curtos (`rs`) devem continuar legíveis em linguagem humana.
