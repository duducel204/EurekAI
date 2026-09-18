# INDEX — orientação rápida para agentes

Este é o índice de entrada para colaboração multiagente no EurekAI.

## Leia nesta ordem
1. `/ESTADO.md` — ponteiro operacional e regra de versão;
2. `/AGENTS.md` — contrato comum;
3. adaptador do agente em `/agentes/`;
4. README da área afetada;
5. roadmap + Goal/INV aplicável;
6. commits/PRs recentes antes de agir.

## Gates de execução
- `READY_FOR_CODEX` — nome legado; significa **pronto para executor autorizado**.
- `CONCLUÍDO` — etapa executada e validada.

Para sequências automáticas, leia `codex/goals/PROTOCOLO-EXECUCAO-SEQUENCIAL.md`. Um próximo Goal só atravessa o gate de entrada após a dependência anterior atravessar o gate de saída.

## Quem faz o quê
- **Codex:** execução sistemática de Goals quando explicitamente liberados.
- **Gemini CLI:** exploração, pesquisa, análise e capacidades Google/MCP quando autorizadas.
- **Cloud Code / Gemini Code Assist:** trabalho sobre workspace/código/Google Cloud seguindo o mesmo estado canônico.
- **ChatGPT:** planejamento, síntese, auditoria e coordenação quando conectado às fontes necessárias.

Papéis não são exclusividades. O escopo autorizado e o estado do Goal prevalecem.

## Índice de zonas
- `agentes/` → contratos/adaptadores de agentes
- `.gemini/` → configuração/skills Gemini
- `.vscode/` → configuração compartilhável do editor
- `ferramentas/` → scripts/utilitários compartilhados
- `codex/goals/` → planejamento executável
- `execucoes/` → relatórios/handoffs genéricos de execução
- `codex/retornos/` → histórico/retornos do workflow Codex
- `contexto/` → memória contextual, não scripts
- `fontes/`, `experiencias/`, `conhecimento/`, `decisoes/`, `hipoteses/`, `descobertas/`, `erros/`, `investigacao/`, `mapa-do-conhecimento/`, `pedagogia/` → corpus e camadas semânticas

## Protocolo simples de versão

### Ao começar
```bash
git fetch origin
git rev-parse origin/main
```

Trate o SHA retornado como **BASE_MAIN_SHA** do trabalho.

### Antes de declarar “estado atual”
Repita o fetch e confirme que está lendo o HEAD remoto atual. Não reconstrua estado apenas de memória de sessão.

### Antes de commit/push/PR
```bash
git fetch origin
git rev-parse origin/main
```

Compare com **BASE_MAIN_SHA**.

Se for igual: valide o trabalho e prossiga.

Se for diferente:
1. leia os commits novos desde a base;
2. veja quais arquivos mudaram;
3. verifique conflito semântico, não apenas conflito textual;
4. rebase/reaplique/revise o trabalho conforme necessário;
5. rode novamente as validações;
6. atualize a base verificada;
7. só então publique.

## Regra de convivência
Um agente não deve “ganhar” de outro sobrescrevendo o que chegou primeiro. Mudança nova em `main` é informação que precisa ser considerada.

Quando dois agentes trabalham em paralelo:
`base comum → trabalhos independentes → verificação do main → reconciliação → validação → PR/commit`.

## Handoff mínimo de versão
Em trabalho material, registrar quando útil:
- base usada;
- HEAD de `main` verificado antes da publicação;
- se houve avanço de `main`;
- como o trabalho foi reconciliado;
- validações refeitas.
