# Pipelines

**Estado atual:** área operacional principal pós-GOAL-010.

## Função

`pipelines/` define como novas fontes entram no EurekAI depois do bootstrap.

Esta pasta substitui a ideia de criar Goals infinitos para cada rotina. O fluxo normal agora é pipeline permanente, retomável e auditável.

## Arquivos atuais

- `CONTRATO-INGESTAO.md`: contrato geral de ingestão incremental.
- `PIPELINE-TAKEOUT-DRIVE.md`: pipeline candidata para Google Takeout/Drive.
- `schemas/`: contratos de formatos intermediários compactos para pipeline.

## Schemas compactos

`schemas/` contém o EKL-0 — **EurekAI Compact Language v0**.

EKL-0 é um schema compacto experimental para classificação e mineração do histórico/Takeout. Ele reduz repetição de cabeçalhos e metadados, preservando procedência mínima e significado semântico.

Arquivos principais:

- `schemas/README.md`: índice da área.
- `schemas/EKL-0-DICIONARIO.md`: códigos e campos canônicos.
- `schemas/EKL-0-CLASSIFICACAO-TAKEOUT.md`: saída compacta para classificação leve.
- `schemas/EKL-0-MINERACAO-TAKEOUT.md`: saída compacta para mineração seletiva.

EKL-0 é intermediário e pré-canonização. Não substitui documentação humana, unidades de conhecimento, decisões canonizadas, auditoria ou produto final.

## Estado pós-bootstrap

- GOAL-001–010 concluídos.
- Pipelines permanentes definidas como próximo modo de operação.
- Google Takeout/Drive definido como primeiro caso candidato.
- Nenhum Takeout foi processado ou canonizado ainda.
- EKL-0 preparado como linguagem compacta para etapas futuras de classificação/mineração, sem executar leitura real.

## Regra operacional

Uma pipeline deve seguir a ordem:

```text
fonte → manifesto → inventário → indexação → deduplicação → classificação → mineração seletiva → validação → canonização
```

Código determinístico deve cuidar de descoberta, hashes, contagens, filas, checkpoints e validação mecânica.

LLM deve ser reservado para classificação semântica, mineração seletiva, síntese, revisão epistemológica e pedagogia.

EKL-0 pode ser usado como formato de saída nas etapas de classificação e mineração seletiva.

## Regra de custo e contexto

Não enviar corpus inteiro para LLM. Cada conversa, documento ou artefato deve ser processado como unidade de trabalho delimitada.

A lógica compacta é:

```text
schema fixo documentado uma vez
↓
registro EKL-0 compacto por item
↓
validação mecânica
↓
expansão quando necessário
↓
validação semântica
↓
canonização humana
```

## Relação com o produto

As pipelines alimentam o motor interno. Elas não são a experiência do usuário final. O produto por link está documentado em `produto/`.
