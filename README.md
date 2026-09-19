# EurekAI

EurekAI é uma base evolutiva de conhecimento sobre inteligência artificial construída a partir de experiências, fontes, decisões, erros, descobertas e relações observáveis. O repositório também é a memória canônica usada por agentes de IA para continuar o trabalho sem depender da conversa que originou cada artefato.

## Produto final

O produto final do EurekAI é uma experiência de alfabetização em inteligência artificial acessível por link. A pessoa usuária deve conseguir começar do zero, mesmo sem saber o que é IA, prompt, modelo, chatbot ou automação.

A promessa do produto é conduzir qualquer pessoa a entender o básico de inteligência artificial de forma simples, segura, intuitiva, prática e crítica. A visão original está em [produto/VISAO-ORIGINAL.md](produto/VISAO-ORIGINAL.md).

O repositório é o motor interno: memória, evidências, unidades de conhecimento, pedagogia, auditoria e pipelines. A interface final não deve expor essa complexidade; ela deve transformar a base em uma experiência de aprendizagem clara.

## Para quem começa do zero
A ambição pedagógica é permitir que alguém sem conhecimento prévio percorra uma progressão compreensível: primeiro intuição e contexto, depois conceitos, mecanismos, experimentos e aplicações. A estrutura interna do repositório não deve ser confundida com a interface final de aprendizagem.

## Como o repositório pensa
`fontes → evidências/experiências → tags → relações → progressão → pedagogia → conteúdo → auditoria → evolução`.

O corpus é único. Tags funcionam como lentes. Relações explícitas só são criadas quando acrescentam significado que as tags não expressam. Ausência de evidência é lacuna, não prova de ausência de conhecimento.

## Colaboração por agentes
O repositório é multiagente. Codex, Gemini CLI, Cloud Code/Gemini Code Assist e futuros agentes podem colaborar, mas o GitHub canoniza estado. Comece por [ESTADO.md](ESTADO.md), depois [AGENTS.md](AGENTS.md) e [agentes/INDEX.md](agentes/INDEX.md). O Gemini possui também [GEMINI.md](GEMINI.md), que adapta o contexto comum ao ambiente Gemini.

## Navegação
- `produto/`: visão do produto final, experiência por link, público, promessa e limites do MVP.
- `capturas/`: entrada bruta ainda não estruturada.
- `fontes/`: procedência e lotes consultáveis.
- `experiencias/`: ações, testes e evidências práticas.
- `conhecimento/`: material já estruturado.
- `mapa-do-conhecimento/`: tags, relações e modelos derivados.
- `decisoes/`, `hipoteses/`, `descobertas/`, `erros/`: estados epistemológicos e trajetória.
- `investigacao/`: lacunas que exigem pesquisa/validação.
- `pedagogia/`: transformação do conhecimento em aprendizagem.
- `ideias-de-produto/`: possibilidades derivadas, sem aprovação implícita.
- `contexto/`: memória contextual do projeto; não é diretório de scripts.
- `templates/`: formatos reutilizáveis validados.
- `codex/`: Goals, roadmap e protocolos de execução.
- `execucoes/`: relatórios/handoffs de execução independentes do agente.
- `agentes/`: contratos, índice e adaptadores para colaboração multiagente.
- `ESTADO.md`: ponteiro operacional leve; a versão técnica corrente é o HEAD de `origin/main`.
- `ferramentas/`: scripts/utilitários compartilhados entre agentes.
- `.gemini/`: configuração e skills do ambiente Gemini; não é corpus canônico.
- `.vscode/`: configuração compartilhável do workspace/editor.

## Estado operacional
Consulte `codex/goals/ROADMAP-GOALS.md` para direção e estado dos Goals. O status de um arquivo deve refletir a realidade observável; PRs, commits e retornos são evidência de execução.
