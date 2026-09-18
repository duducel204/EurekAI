# AGENTS.md — Contrato comum de colaboração

Este é o ponto de entrada para qualquer agente de IA que trabalhe no EurekAI.

## Missão
Continuar o projeto sem depender da conversa que originou o trabalho. O GitHub é o estado canônico; sessões, prompts, memórias e configurações locais dos agentes são contexto auxiliar e podem desaparecer a qualquer momento.

## Regra de reinício de sessão
**Nenhum agente deve presumir memória entre sessões.**

Ao iniciar uma nova sessão, reabrir o workspace ou perder contexto:
1. sincronize referências remotas com `git fetch origin`;
2. leia `ESTADO.md` e confirme o HEAD atual de `origin/main`;
3. leia este arquivo e `agentes/INDEX.md`;
4. leia o adaptador específico do seu agente;
5. leia o README da área afetada;
6. consulte `codex/goals/ROADMAP-GOALS.md` e o Goal/INV aplicável;
7. verifique PRs, branches, retornos e commits recentes antes de agir.

A sessão nunca é a fonte de verdade. O repositório deve conter contexto suficiente para reconstruir o estado operacional.

## Antes de agir
1. Leia este arquivo e o README da área afetada.
2. Consulte `codex/goals/ROADMAP-GOALS.md` e o Goal aplicável quando houver.
3. Sincronize `main` e verifique PRs, branches e retornos antes de concluir que algo falta.
4. Preserve procedência e tipos epistemológicos.
5. Identifique **em qual zona a mudança pertence** antes de criar ou editar arquivo.

## Zonas de escrita

### Conhecimento e memória canônica
Use as pastas semânticas existentes: `fontes/`, `experiencias/`, `conhecimento/`, `decisoes/`, `hipoteses/`, `descobertas/`, `erros/`, `investigacao/`, `mapa-do-conhecimento/`, `pedagogia/`, `capturas/` e `contexto/`.

Só escreva nelas quando a mudança realmente pertencer ao significado daquela área. **Não coloque scripts, credenciais, configurações de IDE ou arquivos gerados por ferramenta em `contexto/` ou nas áreas de conhecimento.**

### Protocolo de agentes
Use `agentes/` para regras e adaptadores de colaboração. Não duplique conhecimento do projeto por agente.

### Ferramentas compartilhadas
Use `ferramentas/` para scripts/utilitários realmente compartilhados pelo projeto. Ferramentas devem usar caminhos relativos ao repositório, ser revisáveis e não aprovar/mesclar PRs automaticamente sem decisão explícita.

### Configuração específica de ferramenta
Use a área nativa da ferramenta quando apropriado, por exemplo `.gemini/` e `.vscode/`. Esses arquivos descrevem **capacidade/configuração da ferramenta**, não conhecimento nem decisão do EurekAI.

## Modelo epistemológico mínimo
- **FATO:** observação verificável.
- **EXPERIÊNCIA:** ação/tentativa atribuível.
- **DECISÃO:** escolha explicitamente tomada.
- **HIPÓTESE:** interpretação a testar.
- **TENSÃO:** fontes/direções incompatíveis.
- **LACUNA:** informação necessária ausente.
- **EVIDÊNCIA:** unidade rastreável que sustenta/contesta afirmação.

Não converta exposição, frequência, capacidade de ferramenta ou código existente em “domínio”, “decisão” ou “arquitetura adotada”. Diferencie `IA PROPÔS`, `AUTOR DISSE`, `AUTOR FEZ`, `AUTOR CONFIRMOU` e não confirmado.

## Arquitetura de conhecimento
Preferir corpus único + tags + consultas/lentes. Não criar cópias por agente, tecnologia ou categoria. Relações explícitas devem acrescentar significado que tags não expressem.

**`conhecimento/` contém conhecimento estruturado. `pedagogia/` contém a transformação desse conhecimento em progressão, ensino, explicação, exercícios e outras formas de aprendizagem. Não confundir as duas camadas.**

## Goals
Existem dois gates operacionais:
- `READY_FOR_CODEX` — nome legado que agora significa **pronto para executor autorizado**;
- `CONCLUÍDO` — gate de saída, somente após entregáveis, Acceptance e validação.

Estados de rascunho/preparação não autorizam execução por si só.

Uma sequência explicitamente autorizada pode promover automaticamente o Goal seguinte ao gate `READY_FOR_CODEX` somente quando a dependência anterior estiver `CONCLUÍDO` e validada. Aplicar `codex/goals/PROTOCOLO-EXECUCAO-SEQUENCIAL.md`.

Novos relatórios multiagente devem preferir `execucoes/`. `codex/retornos/` permanece válido para histórico e workflow Codex específico.

## Multiagente
Codex, Gemini CLI, Cloud Code/Gemini Code Assist, ChatGPT e futuros agentes podem ter especialidades diferentes. Nenhum agente possui uma “verdade própria”: descobertas retornam ao GitHub por evidência, documento ou PR apropriado.

**Capacidade do agente ≠ configuração local ≠ artefato operacional ≠ decisão do EurekAI ≠ conhecimento canônico.**

## Validação de versão e concorrência
Todo trabalho material deve ter uma base identificável: o SHA de `origin/main` observado no início.

Antes de declarar “estado atual”, commitar, fazer push ou abrir PR:
1. execute `git fetch origin`;
2. obtenha o HEAD atual de `origin/main`;
3. compare com a base usada no trabalho;
4. se `main` avançou, revise os commits/arquivos novos;
5. verifique conflito semântico, mesmo quando o Git não acusa conflito textual;
6. reconcilie/rebase/reaplique conforme necessário;
7. repita as validações antes de publicar.

Um agente **não deve publicar trabalho calculado sobre uma base antiga sem revisar o que mudou desde então**. Mudanças de outro agente devem ser tratadas como informação nova, não sobrescritas por conveniência.

O protocolo resumido está em `agentes/INDEX.md`.

## Git e publicação
Por padrão:
- não fazer `git add .` indiscriminadamente;
- não fazer force push;
- não aprovar o próprio PR;
- não habilitar auto-merge por conta própria;
- não escrever diretamente em `main` quando o trabalho exigir revisão;
- não transformar configuração local em afirmação canônica do projeto.

## Mudanças
Prefira alterações pequenas, rastreáveis e compatíveis com a estrutura existente. Não sobrescreva história para fazê-la parecer coerente. Não exponha segredos, tokens ou estado local. Quando faltar autorização/evidência, pare ou abra investigação adequada.

## Handoff mínimo
Ao terminar trabalho material, deixe: objetivo executado, fontes/evidências usadas, arquivos alterados, validações, limitações/lacunas e próximo estado permitido.
