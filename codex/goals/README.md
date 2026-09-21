# Goals — EurekAI

**Estado atual:** GOAL-001–010 concluídos. Esta pasta preserva o bootstrap inicial do EurekAI e seus protocolos de execução.

## Função desta pasta

`codex/goals/` registra os Goals que estruturaram a fundação inicial do projeto:

- contrato operacional;
- aquisição e investigação;
- mineração inicial;
- modelo de conhecimento;
- relações;
- progressão pedagógica;
- engenharia pedagógica atemporal;
- produção sistemática de unidades de conhecimento;
- auditoria e contrato de ingestão;
- transição para pipelines permanentes.

Após GOAL-010, esta pasta deixa de ser fila principal de trabalho. Novas fontes e rotinas devem entrar por `pipelines/`, salvo decisão explícita de criar novo Goal estrutural.

## Gates

- `READY_FOR_CODEX` — nome legado; significa pronto para qualquer executor autorizado.
- `CONCLUÍDO` — execução validada e encerrada.

Todos os Goals 001–010 estão concluídos no estado canônico atual.

Não há Goal aberto nem arquivo no gate `READY_FOR_CODEX`. O processamento rotineiro de novas fontes deve seguir os contratos em `pipelines/`.

## Arquivos principais

- `ROADMAP-GOALS.md`: histórico e macrofluxo dos Goals.
- `PROTOCOLO-EXECUCAO-SEQUENCIAL.md`: regra de execução encadeada.
- `DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md`: regra para derivar conhecimento reutilizável sem convergência prematura.
- `GOAL-001...GOAL-010...`: escopo de cada Goal concluído.

## Regra pós-bootstrap

Não usar esta pasta para abrir uma sequência infinita de Goals operacionais. O fluxo normal agora é:

```text
nova fonte → pipeline → inventário → classificação → mineração seletiva → validação → canonização
```

Goals futuros só devem existir se houver mudança estrutural no projeto, não para processar rotina.
