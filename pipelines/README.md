# Pipelines

**Estado atual:** área operacional principal pós-GOAL-010.

## Função

`pipelines/` define como novas fontes entram no EurekAI depois do bootstrap.

Esta pasta substitui a ideia de criar Goals infinitos para cada rotina. O fluxo normal agora é pipeline permanente, retomável e auditável.

## Arquivos atuais

- `CONTRATO-INGESTAO.md`: contrato geral de ingestão incremental.
- `PIPELINE-TAKEOUT-DRIVE.md`: pipeline candidata para Google Takeout/Drive.

## Estado pós-bootstrap

- GOAL-001–010 concluídos.
- Pipelines permanentes definidas como próximo modo de operação.
- Google Takeout/Drive definido como primeiro caso candidato.
- Nenhum Takeout foi processado ou canonizado ainda.

## Regra operacional

Uma pipeline deve seguir a ordem:

```text
fonte → manifesto → inventário → indexação → deduplicação → classificação → mineração seletiva → validação → canonização
```

Código determinístico deve cuidar de descoberta, hashes, contagens, filas, checkpoints e validação mecânica.

LLM deve ser reservado para classificação semântica, mineração seletiva, síntese, revisão epistemológica e pedagogia.

## Regra de custo e contexto

Não enviar corpus inteiro para LLM. Cada conversa, documento ou artefato deve ser processado como unidade de trabalho delimitada.

## Relação com o produto

As pipelines alimentam o motor interno. Elas não são a experiência do usuário final. O produto por link está documentado em `produto/`.