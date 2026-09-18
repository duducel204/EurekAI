# Contexto Gemini — EurekAI

Este arquivo é um adaptador, não uma segunda fonte de regras.

1. Leia primeiro `AGENTS.md`.
2. Leia o README da área em que trabalhará e o Goal/INV aplicável.
3. Trate GitHub/`main` como estado canônico; contexto do Gemini é auxiliar.
4. Use `.gemini/` apenas para configuração, skills e recursos próprios do ambiente Gemini/Google.
5. Não mova scripts operacionais, configurações de IDE ou arquivos gerados por ferramentas para `contexto/`, `conhecimento/` ou outras áreas semânticas.
6. Ferramentas compartilhadas entre agentes pertencem a `ferramentas/`; regras de colaboração pertencem a `agentes/`.
7. Use Gemini CLI, Cloud Code/Gemini Code Assist, MCP e Google Cloud para pesquisa, análise ou execução apenas dentro do escopo autorizado.
8. Não trate acesso a BigQuery, Cloud SQL, Spanner, AlloyDB, Catalog, notebooks ou outros serviços como evidência de que esses serviços fazem parte da arquitetura do EurekAI. São capacidades/fontes até decisão explícita.
9. Não transforme a própria configuração do Gemini em decisão, evidência pessoal ou conhecimento canônico.
10. Credenciais, ADC, tokens, chaves, configurações locais e logs sensíveis não pertencem ao corpus.
11. Não aprove nem faça merge automático de PR sem autorização explícita do workflow canônico.

Consulte `agentes/gemini/README.md`, `agentes/cloud-code/README.md` e `agentes/README.md`.
