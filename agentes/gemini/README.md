# Adaptador Gemini

Orientações para Gemini CLI e ambientes Gemini/Google que colaborarem no EurekAI.

## Contexto
`/GEMINI.md` deve permanecer curto e apontar para `/AGENTS.md`; não replique o contrato inteiro. Leia também o README da área e o Goal/INV aplicável.

## Área própria
`.gemini/` é espaço de configuração/skills da ferramenta. Conteúdo ali descreve capacidades do ambiente e **não entra automaticamente no corpus, no mapa de conhecimento ou nas decisões do projeto**.

## Capacidades úteis
Gemini pode explorar documentação, código, Google Cloud e fontes conectadas; MCP pode ampliar ferramentas. Essas capacidades não autorizam ingestão nem alteração por si só.

## Google Cloud
BigQuery, Cloud SQL, Spanner, AlloyDB, catálogos, notebooks, Spark e demais serviços devem ser tratados inicialmente como **capacidades/fontes candidatas**. Só passam a componente arquitetural quando uma decisão/Goal justificar necessidade, custo, segurança e manutenção.

## Escrita
Configuração Gemini fica em `.gemini/`; regras de agentes em `agentes/`; scripts compartilhados em `ferramentas/`; conteúdo/evidência somente na pasta semântica correta. Não use `contexto/` como diretório operacional.

## Saída
Preserve localizador/procedência. Descobertas devem alimentar estruturas canônicas (fonte, evidência, investigação, mapa, decisão etc.), nunca uma base paralela do Gemini.
