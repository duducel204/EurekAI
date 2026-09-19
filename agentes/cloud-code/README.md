# Adaptador Cloud Code / Gemini Code Assist

**Estado atual:** ativo como executor possível em ambiente Google/Cloud Code.

## Função

Este adaptador orienta o uso do Cloud Code/Gemini Code Assist no EurekAI.

Pode ser útil para:

- tarefas longas no repositório;
- integração com ferramentas Google;
- apoio a pipelines;
- trabalho com código e validações;
- execução assistida em ambiente remoto.

## Regra pós-bootstrap

GOAL-001–010 estão concluídos. Cloud Code deve tratar `codex/goals/` como histórico de bootstrap e usar `pipelines/` para novas rotinas.

## Retomada mínima

Ler:

1. `ESTADO.md`
2. `AGENTS.md`
3. `agentes/INDEX.md`
4. `GEMINI.md` quando aplicável
5. este arquivo
6. README da área afetada

## Limite

Cloud Code não deve assumir que acesso a Google Drive, Cloud ou repositórios externos autoriza ingestão automática. Toda fonte exige manifesto, limites e validação.