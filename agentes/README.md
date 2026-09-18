# Agentes

Camada de interoperabilidade para agentes que colaboram no EurekAI. Guarda contratos e adaptadores mínimos; **não** cria cópias do conhecimento por ferramenta.

## Princípio
`mesmo GitHub + mesmas evidências + mesmos estados → agentes diferentes → contribuições complementares`.

## Memória operacional
Sessões de agentes são voláteis. O repositório deve ser suficiente para reconstruir contexto e regras depois que uma conversa for encerrada.

Ao iniciar nova sessão, todo agente deve reler `/AGENTS.md`, seu adaptador, o README da área afetada e o Goal/INV aplicável antes de agir.

## Papéis atuais
- **Codex:** executor principal do workflow orientado a Goals e mudanças versionadas.
- **Gemini CLI:** exploração, pesquisa, análise, automação CLI e uso de capacidades Google/MCP quando autorizado.
- **Cloud Code / Gemini Code Assist:** trabalho sobre workspace, código e ecossistema Google Cloud, sem assumir que capacidade disponível virou arquitetura.
- **ChatGPT:** planejamento, síntese, auditoria e coordenação quando conectado às fontes necessárias.

Papéis são preferências operacionais, não exclusividade. O Goal e as permissões determinam o que cada agente pode fazer.

## Onde cada tipo de coisa deve viver
- regras entre agentes → `agentes/`;
- configuração Gemini/Google → `.gemini/`;
- configuração de editor → `.vscode/`;
- scripts/utilitários compartilhados → `ferramentas/`;
- Goals/retornos do Codex → `codex/`;
- conhecimento/evidência/contexto → somente nas pastas semânticas correspondentes.

Nenhum agente deve usar uma pasta semântica como “depósito genérico” de scripts ou configuração.

## Limites importantes
- `codex/retornos/` é saída do workflow Codex; outros agentes só escrevem ali quando explicitamente autorizados.
- `conhecimento/` estrutura conhecimento.
- `pedagogia/` transforma conhecimento em aprendizagem.
- capacidade instalada não equivale a decisão arquitetural.

## Regra de entrada
Todo agente começa em `/AGENTS.md`, depois lê o README da área e o Goal/pendência relevante. Adaptações específicas devem apontar de volta para o contrato comum.

## Regra de saída
Resultado relevante volta como mudança rastreável, evidência, retorno ou investigação. Sessão de chat não é armazenamento canônico.

Configuração de uma ferramenta pode permanecer apenas como configuração; ela não precisa ser promovida ao conhecimento do EurekAI.
