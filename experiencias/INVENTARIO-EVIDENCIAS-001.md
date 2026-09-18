# Inventário inicial de evidências — Lote L-003

> **Procedência pendente:** este primeiro passe histórico não registrou localizadores individuais das conversas/arquivos originais. E-001–E-013 são pistas provisórias, não evidências auditadas nem base para atribuir conhecimento a André. Consulte a [auditoria por entrada](AUDITORIA-EVIDENCIAS-001.md). O texto original foi preservado para permitir recuperação e correção, sem transformá-lo em fato confirmado.

**Goal:** GOAL-003  
**Fonte:** F-003 — contexto histórico recuperável do ChatGPT  
**Recorte:** primeiro passe, 2026-09-18  
**Estado:** evidência inicial; não é classificação de domínio.

## Corpus e método

Este lote registra eventos observáveis recuperados de conversas anteriores de André. A recuperação foi orientada a ações e resultados, não a palavras-chave isoladas. Exposição, pergunta, execução, erro, diagnóstico, solução e reaplicação permanecem eventos distintos. Conteúdo de assistente não é atribuído automaticamente a André.

## Evidências

| ID | Tópicos candidatos | Evento | Evidência observável | Data/contexto | Limites |
| --- | --- | --- | --- | --- | --- |
| E-001 | PowerShell; Windows; execução local | CONFIGUROU / USOU | Executou bootstrap PowerShell que verificou Python, criou `AI_WORKSPACE`, instalou `cptr` e iniciou o Computer. | 2026-09-16; IA local | Execução bem-sucedida não prova compreensão de todos os componentes instalados. |
| E-002 | APIs; Gemini; debugging | ERROU / TENTOU | Configuração Gemini via endpoint compatível com OpenAI retornou `404 Not Found` em `/v1beta/openai/chat/completions`. | 2026-09-17; integração IA local | A proposta de diagnóstico subsequente veio com assistência de IA; não atribuir diagnóstico integral ao autor. |
| E-003 | modelos; gateway; troubleshooting | CONFIGUROU / DIAGNOSTICOU | Verificou que o Gateway listava modelos Gemini e continuou isolando falha após novo 404. | 2026-09-17 | Há evidência de troubleshooting operacional; resolução final não foi recuperada neste lote. |
| E-004 | MCP; Termux; integração | USOU / CONFIGUROU | No projeto `duducel204/manuss`, a ponte MCP foi validada com `termux_exec` e `exit_code: 0`; Windows/PowerShell foi separado da trilha mobile/Termux. | 2026-09-17; manuss | Documenta funcionamento no contexto, não domínio geral de MCP. |
| E-005 | GitHub; branches; permissões | TENTOU / ERROU / DIAGNOSTICOU | Tentou criar branch `windows-separation`; encontrou 403 `Resource not accessible by integration` e relacionou o problema às permissões entre organização `DreamteamGe` e conta pessoal `duducel204`, preservando `main`. | 2026-09-17; manuss | Diagnóstico contextual; não generalizar para administração completa do GitHub. |
| E-006 | Codex; Windows; CLI | CONFIGUROU / ERROU | Codex desktop abria, enquanto `codex` não era reconhecido no PowerShell; houve investigação de autenticação/ambiente. | 2026-09-17 | Não há neste recorte prova de resolução completa do CLI. |
| E-007 | OAuth; Codex; autenticação | TENTOU / CONFIGUROU | Tentou autenticar Codex CLI via OAuth com callback local em `localhost:1455/auth/callback`. | 2026-09-17 | A URL/token temporário não é preservado neste inventário. |
| E-008 | GitHub; Codex; workflow | REAPLICOU / DECIDIU | Em EurekAI, adotou GitHub como ponte/memória canônica e Codex como executor, com ChatGPT no planejamento/auditoria. | 2026-09-18; EurekAI | É decisão arquitetural do projeto; não mede conhecimento técnico isoladamente. |
| E-009 | arquitetura cognitiva; agentes | CONSTRUIU / DECIDIU | Dream Team registra princípios de versionamento encadeado, rollback como evento, registrador sem poder decisório e gates explícitos; artefatos standalone de orquestrador/arquiteto foram versionados/canonizados. | 2026; Dream Team | Parte do material é documentação de projeto; execução individual de cada mecanismo deve ser verificada separadamente. |
| E-010 | desenvolvimento de produto; IA | DECIDIU / CONSTRUIU | FotoDu foi trabalhado por blueprint/roadmap, com decisões como resultado antes de tecnologia, evidência antes de compromisso, custo antes da geração e privacidade/consentimento. | 2026-09; FotoDu | Evidencia raciocínio de produto documentado; implementação técnica de cada decisão exige evidência própria. |
| E-011 | cloud; arquitetura | CONFIGUROU / DECIDIU | Em MVP anterior, trabalhou com Cloud Run, Cloud SQL/PostgreSQL, Cloud Storage, Secret Manager e avaliação de Vertex AI/BigQuery, com foco explícito em custo. | 2026-02; MVP inventário | Projeto foi posteriormente descontinuado; exposição/configuração não implica domínio de GCP. |
| E-012 | API; HMAC; autenticação | TENTOU / ERROU | Em integração BingX, trabalhou com endpoints, parâmetros, assinatura HMAC/SHA-256 e erro `signature verification failed`, incluindo problemas de ordem/encoding. | 2026-03; BingX API | Parte das soluções foi orientada por IA; resolução/autoria precisa de mineração mais granular. |
| E-013 | Pine Script; TradingView | TENTOU / AVALIOU | Iterou requisito de indicador Pine v6, comparou resultado visual com desenho manual e rejeitou implementação quando os círculos esperados não apareceram. | 2026-03; TradingView | Evidencia especificação/teste e crítica do resultado; capacidade de implementação em Pine não está estabelecida. |

## Relações iniciais

- **E-005 → E-007 → E-008:** GitHub/autenticação reaparece em contextos distintos e evolui para uma decisão explícita de arquitetura de trabalho.
- **E-001 → E-003 → E-004:** execução local, endpoints/gateway e MCP aparecem como cadeia prática de integração IA ↔ computador.
- **E-009 → E-008:** princípios anteriores de governança/versionamento reaparecem na separação entre executor, memória canônica e auditoria do EurekAI.
- **E-002 / E-005 / E-012:** erros concretos são usados como pontos de investigação; ainda é necessário distinguir diagnóstico próprio de solução conduzida por assistente.

## Tópicos candidatos provisórios

Git/GitHub; Codex; PowerShell/Windows; APIs e autenticação; OAuth; MCP; IA local/Gemini; debugging; agentes e orquestração; governança/versionamento; arquitetura de aplicações; cloud; desenvolvimento de produto com IA; Pine Script.

## Lacunas e tensões

1. Separar, por episódio, o que André diagnosticou do que apenas executou após instrução da IA.
2. Recuperar resultados finais de episódios com erro para distinguir TENTOU de RESOLVEU.
3. Procurar reaplicações independentes dos mesmos mecanismos em projetos diferentes.
4. Não converter documentação produzida com assistência de IA em prova automática de autoria intelectual.
5. Ampliar o corpus histórico antes de qualquer modelo de nível ou domínio.

## Cobertura

Este lote é deliberadamente pequeno e heterogêneo. Ele demonstra que existe corpus útil para o GOAL-003 e fornece uma primeira malha de eventos, mas não pretende representar toda a trajetória de André.
