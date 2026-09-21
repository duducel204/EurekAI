# EurekAI

**Estado atual:** bootstrap inicial concluído. Os GOALs 001–010 estão encerrados no repositório canônico; a próxima fase é operação por pipelines permanentes.

EurekAI é uma base evolutiva de conhecimento sobre inteligência artificial construída a partir de experiências, fontes, decisões, erros, descobertas e relações observáveis. O repositório também é a memória canônica usada por agentes de IA para continuar o trabalho sem depender da conversa que originou cada artefato.

## Produto final

O produto final do EurekAI é uma experiência de alfabetização em inteligência artificial acessível por link. A pessoa usuária deve conseguir começar do zero, mesmo sem saber o que é IA, prompt, modelo, chatbot, automação ou GitHub.

A promessa do produto é conduzir qualquer pessoa a entender o básico de inteligência artificial de forma simples, segura, intuitiva, prática e crítica. A visão original está em [produto/VISAO-ORIGINAL.md](produto/VISAO-ORIGINAL.md).

O repositório é o motor interno: memória, evidências, unidades de conhecimento, pedagogia, auditoria e pipelines. A interface final não deve expor essa complexidade; ela deve transformar a base em uma experiência de aprendizagem clara.

## Estado operacional

- GOAL-001–010: concluídos.
- Bootstrap inicial: encerrado.
- Modo atual: operação contínua por pipelines.
- Primeiro caso candidato: Google Takeout/Drive.
- Takeout/Drive: pipeline definida, mas nenhum Takeout foi processado ou canonizado.
- EKL-0: schema compacto preparado para classificação/mineração futura do histórico/Takeout, sem execução real ainda.
- Corpus histórico: ainda parcial; a pendência é acompanhada em [investigacao/pendencias/INV-001-CORPUS-HISTORICO.md](investigacao/pendencias/INV-001-CORPUS-HISTORICO.md).

## Para quem começa do zero

A ambição pedagógica é permitir que alguém sem conhecimento prévio percorra uma progressão compreensível: primeiro intuição e contexto, depois exemplos, conceitos, mecanismos, experimentos, limites e aplicações.

A estrutura interna do repositório não deve ser confundida com a interface final de aprendizagem.

## Como o repositório pensa

`fontes → evidências/experiências → tags → relações → progressão → pedagogia → unidades de conhecimento → auditoria → pipelines → evolução`

O corpus é único. Tags funcionam como lentes. Relações explícitas só são criadas quando acrescentam significado que as tags não expressam. Ausência de evidência é lacuna, não prova de ausência de conhecimento.

## Colaboração por agentes

O repositório é multiagente. Codex, Gemini CLI, Cloud Code/Gemini Code Assist, ChatGPT e futuros agentes podem colaborar, mas o GitHub canoniza estado.

Ordem mínima de retomada:

1. [ESTADO.md](ESTADO.md)
2. [AGENTS.md](AGENTS.md)
3. [agentes/INDEX.md](agentes/INDEX.md)
4. [produto/VISAO-ORIGINAL.md](produto/VISAO-ORIGINAL.md)
5. [codex/goals/ROADMAP-GOALS.md](codex/goals/ROADMAP-GOALS.md)
6. README da área afetada

O Gemini possui também [GEMINI.md](GEMINI.md), que adapta o contexto comum ao ambiente Gemini.

## Navegação

- `produto/`: visão do produto final, experiência por link, público, promessa e limites do MVP.
- `capturas/`: entrada bruta ainda não estruturada.
- `fontes/`: procedência e lotes consultáveis.
- `experiencias/`: ações, testes e evidências práticas.
- `conhecimento/`: contrato e unidades de conhecimento estruturado.
- `mapa-do-conhecimento/`: tags, relações e modelos derivados.
- `decisoes/`, `hipoteses/`, `descobertas/`, `erros/`: estados epistemológicos e trajetória.
- `investigacao/`: lacunas que exigem pesquisa/validação.
- `pedagogia/`: transformação do conhecimento em aprendizagem; inclui exemplo didático de otimização de tokens com EKL-0.
- `ideias-de-produto/`: possibilidades derivadas, sem aprovação implícita.
- `contexto/`: memória contextual do projeto; não é diretório de scripts.
- `templates/`: formatos reutilizáveis validados.
- `codex/`: Goals, roadmap e protocolos de execução. Histórico de bootstrap, não fila infinita.
- `execucoes/`: relatórios/handoffs de execução independentes do agente.
- `agentes/`: contratos, índice e adaptadores para colaboração multiagente.
- `ESTADO.md`: ponteiro operacional leve; a versão técnica corrente é o HEAD de `origin/main`.
- `ferramentas/`: scripts/utilitários compartilhados entre agentes, incluindo validação/expansão EKL-0.
- `pipelines/`: contratos de operação contínua, ingestão incremental e schemas compactos de pipeline.
- `.gemini/`: configuração e skills do ambiente Gemini; não é corpus canônico.
- `.vscode/`: configuração compartilhável do workspace/editor.

## EKL-0

EKL-0 — EurekAI Compact Language v0 — é uma linguagem compacta intermediária para reduzir repetição de metadados nas etapas futuras de classificação e mineração do histórico/Takeout.

Documentação principal:

- [pipelines/schemas/EKL-0-DICIONARIO.md](pipelines/schemas/EKL-0-DICIONARIO.md)
- [pipelines/schemas/EKL-0-CLASSIFICACAO-TAKEOUT.md](pipelines/schemas/EKL-0-CLASSIFICACAO-TAKEOUT.md)
- [pipelines/schemas/EKL-0-MINERACAO-TAKEOUT.md](pipelines/schemas/EKL-0-MINERACAO-TAKEOUT.md)
- [pedagogia/OTIMIZACAO-TOKENS-EKL-0.md](pedagogia/OTIMIZACAO-TOKENS-EKL-0.md)

EKL-0 não é formato final de conhecimento nem linguagem para usuário final. É bastidor técnico e exemplo pedagógico.

## Regra de alinhamento

Antes de propor produto, interface, conteúdo ou automação, validar a pergunta central:

> Isso ajuda alguém que não sabe nada de IA a começar a entender, usar e questionar IA com segurança?

Se a resposta for não, provavelmente é camada posterior, suporte interno ou desvio de foco.