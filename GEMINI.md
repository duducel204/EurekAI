# Contexto Gemini — EurekAI

Este arquivo é um adaptador, não uma segunda fonte de regras.

## Bootstrap obrigatório a cada nova sessão
O Gemini Code Assist, Gemini CLI ou outro agente Gemini deve assumir que **não possui memória confiável da sessão anterior**.

Antes de executar qualquer tarefa material:
1. execute `git fetch origin` e confirme o HEAD de `origin/main`;
2. leia `ESTADO.md`, `AGENTS.md` e `agentes/INDEX.md`;
3. leia `agentes/gemini/README.md` e, quando aplicável, `agentes/cloud-code/README.md`;
4. leia o README da área em que trabalhará;
5. consulte o Goal/INV aplicável e o roadmap;
6. registre a base usada e verifique PRs/branches/commits recentes.

Não dependa de instruções que existam apenas no chat.

## Regras
1. Trate GitHub/`main` como estado canônico; contexto do Gemini é auxiliar.
2. Use `.gemini/` apenas para configuração, skills e recursos próprios do ambiente Gemini/Google.
3. Não mova scripts operacionais, configurações de IDE ou arquivos gerados por ferramentas para `contexto/`, `conhecimento/` ou outras áreas semânticas.
4. Ferramentas compartilhadas entre agentes pertencem a `ferramentas/`; regras de colaboração pertencem a `agentes/`.
5. Use Gemini CLI, Cloud Code/Gemini Code Assist, MCP e Google Cloud para pesquisa, análise ou execução apenas dentro do escopo autorizado.
6. Não trate acesso a BigQuery, Cloud SQL, Spanner, AlloyDB, Catalog, notebooks ou outros serviços como evidência de que esses serviços fazem parte da arquitetura do EurekAI. São capacidades/fontes até decisão explícita.
7. Não transforme a própria configuração do Gemini em decisão, evidência pessoal ou conhecimento canônico.
8. Credenciais, ADC, tokens, chaves, configurações locais e logs sensíveis não pertencem ao corpus.
9. Não aprove nem faça merge automático de PR sem autorização explícita do workflow canônico.
10. `codex/retornos/` não é área padrão de saída do Gemini; escreva ali apenas quando um Goal ou instrução explícita autorizar.
11. `conhecimento/` contém conhecimento estruturado; `pedagogia/` contém sua transformação em aprendizagem. Não trate esses papéis como equivalentes.
12. Antes de commit, push ou PR, faça novo `git fetch origin`, compare o HEAD atual de `origin/main` com a base do trabalho e revise/reconcilie qualquer avanço antes de publicar.

Consulte `agentes/gemini/README.md`, `agentes/cloud-code/README.md` e `agentes/README.md`.
