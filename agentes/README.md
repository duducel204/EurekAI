# Agentes

**Estado atual:** contrato multiagente ativo. Bootstrap 001–010 concluído.

## Função

`agentes/` define como Codex, Gemini, Cloud Code/Gemini Code Assist, ChatGPT e futuros agentes devem colaborar sem depender de memória de sessão.

## Arquivos atuais

- `INDEX.md`: protocolo resumido de retomada e validação de versão.
- `codex/README.md`: adaptador do Codex.
- `gemini/README.md`: adaptador do Gemini.
- `cloud-code/README.md`: adaptador do Cloud Code/Gemini Code Assist.

## Ordem mínima de leitura para agentes

1. `ESTADO.md`
2. `AGENTS.md`
3. `agentes/INDEX.md`
4. adaptador específico do agente
5. `produto/VISAO-ORIGINAL.md` quando a tarefa tocar produto, interface ou conteúdo
6. README da área afetada

## Estado pós-GOAL-010

O repositório entrou em modo de pipelines permanentes. Agentes não devem reabrir os Goals concluídos nem tratar rascunhos obsoletos como estado atual.

## Regra semântica

Capacidade de agente, configuração local, artefato operacional, decisão do projeto e conhecimento canônico são coisas diferentes.