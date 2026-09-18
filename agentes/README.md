# Agentes

Camada de interoperabilidade para agentes que colaboram no EurekAI. Guarda contratos e adaptadores mínimos; **não** cria cópias do conhecimento por ferramenta.

## Princípio
`mesmo GitHub + mesmas evidências + mesmos estados → agentes diferentes → contribuições complementares`.

## Papéis atuais
- **Codex:** executor principal do workflow orientado a Goals e mudanças versionadas.
- **Gemini CLI:** exploração, pesquisa, análise, automação CLI e uso de capacidades Google/MCP quando autorizado.
- **Cloud Code / Gemini Code Assist:** contexto de workspace e tarefas relacionadas ao ecossistema Google Cloud/desenvolvimento.
- **ChatGPT:** planejamento, síntese, auditoria e coordenação quando conectado às fontes necessárias.

Papéis são preferências operacionais, não exclusividade. O Goal e as permissões determinam o que cada agente pode fazer.

## Regra de entrada
Todo agente começa em `/AGENTS.md`, depois lê o README da área e o Goal/pendência relevante. Adaptações específicas devem apontar de volta para o contrato comum.

## Regra de saída
Resultado relevante volta como mudança rastreável, evidência, retorno ou investigação. Sessão de chat não é armazenamento canônico.
