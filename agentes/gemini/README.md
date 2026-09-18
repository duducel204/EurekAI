# Adaptador Gemini

Orientações para Gemini CLI e ambientes Gemini/Google que colaborarem no EurekAI.

## Reinício de sessão
Assuma memória volátil. A cada nova sessão:
1. execute `git fetch origin` e confirme o HEAD de `origin/main`;
2. leia `/ESTADO.md`, `/AGENTS.md` e `/agentes/INDEX.md`;
3. releia `/GEMINI.md` e este arquivo;
4. leia o README da área de trabalho e o Goal/INV aplicável;
5. registre a base usada e verifique mudanças recentes.

Não dependa de instruções preservadas apenas no chat anterior.

## Contexto
`/GEMINI.md` deve permanecer como adaptador e apontar para `/AGENTS.md`; não mantenha uma segunda verdade do projeto.

## Área própria
`.gemini/` é espaço de configuração/skills da ferramenta. Conteúdo ali descreve capacidades do ambiente e **não entra automaticamente no corpus, no mapa de conhecimento ou nas decisões do projeto**.

## Capacidades úteis
Gemini pode explorar documentação, código, Google Cloud e fontes conectadas; MCP pode ampliar ferramentas. Essas capacidades não autorizam ingestão nem alteração por si só.

## Google Cloud
BigQuery, Cloud SQL, Spanner, AlloyDB, catálogos, notebooks, Spark e demais serviços devem ser tratados inicialmente como **capacidades/fontes candidatas**. Só passam a componente arquitetural quando uma decisão/Goal justificar necessidade, custo, segurança e manutenção.

## Escrita
Configuração Gemini fica em `.gemini/`; regras de agentes em `agentes/`; scripts compartilhados em `ferramentas/`; conteúdo/evidência somente na pasta semântica correta. Não use `contexto/` como diretório operacional.

`codex/retornos/` não é destino normal do Gemini. Só escreva ali quando um Goal ou instrução explícita autorizar.

`conhecimento/` contém conhecimento estruturado. `pedagogia/` contém a transformação desse conhecimento em progressão, explicação, ensino, exercícios e experiências de aprendizagem.

## Antes de publicar
Faça novo `git fetch origin`. Se o HEAD de `origin/main` mudou desde o início, revise os commits e arquivos novos, reconcilie o trabalho e refaça as validações antes de commit/push/PR.

## Saída
Preserve localizador/procedência. Descobertas devem alimentar estruturas canônicas (fonte, evidência, investigação, mapa, decisão etc.), nunca uma base paralela do Gemini.
