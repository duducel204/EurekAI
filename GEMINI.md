# Contexto Gemini — EurekAI

Este arquivo é um adaptador, não uma segunda fonte de regras.

1. Leia primeiro `AGENTS.md`.
2. Leia o README da área em que trabalhará e o Goal aplicável.
3. Trate GitHub/`main` como estado canônico; contexto do Gemini é auxiliar.
4. Use capacidades do Gemini CLI, Cloud Code/Gemini Code Assist, MCP e Google Cloud para pesquisa, análise ou execução apenas dentro do escopo autorizado.
5. Não crie uma base paralela “do Gemini”. Resultados úteis devem voltar às estruturas canônicas com procedência.
6. Não trate acesso a BigQuery, Cloud SQL, Spanner, AlloyDB, Catalog, notebooks ou outros serviços como evidência de que esses serviços fazem parte da arquitetura do EurekAI. São capacidades/fontes até decisão explícita.
7. Credenciais, ADC, tokens, configurações locais e logs sensíveis não pertencem ao corpus.

Consulte `agentes/gemini/README.md` para orientações específicas e `agentes/README.md` para o modelo multiagente.
