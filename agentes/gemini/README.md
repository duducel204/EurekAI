# Adaptador Gemini

**Estado atual:** ativo como executor possível, especialmente para tarefas longas, classificação e mineração seletiva.

## Função

Este adaptador orienta o uso do Gemini/Gemini CLI dentro do EurekAI.

Gemini pode ajudar em:

- leitura controlada de fontes extensas;
- classificação semântica;
- mineração seletiva;
- síntese de lotes;
- apoio a pipelines de ingestão.

## Regra pós-bootstrap

GOAL-001–010 estão concluídos. Gemini não deve reexecutar ou reinterpretar os Goals como pendentes. Novas fontes devem entrar por `pipelines/`.

## Retomada mínima

Ler:

1. `ESTADO.md`
2. `AGENTS.md`
3. `agentes/INDEX.md`
4. `GEMINI.md`
5. este arquivo
6. README da área afetada

## Limite

Não enviar corpus inteiro ao modelo. Primeiro inventariar, indexar, deduplicar e classificar. Conteúdo só deve entrar no contexto em unidades delimitadas.