# AGENTS.md — Contrato comum de colaboração

Este é o ponto de entrada para qualquer agente de IA que trabalhe no EurekAI.

## Missão
Continuar o projeto sem depender da conversa que originou o trabalho. O GitHub é o estado canônico; sessões, prompts e memórias de agentes são contexto auxiliar.

## Antes de agir
1. Leia este arquivo e o README da área afetada.
2. Consulte `codex/goals/ROADMAP-GOALS.md` e o Goal aplicável quando houver.
3. Sincronize `main` e verifique PRs/branches/retornos antes de concluir que algo falta.
4. Preserve procedência e tipos epistemológicos.

## Modelo epistemológico mínimo
- **FATO:** observação verificável.
- **EXPERIÊNCIA:** ação/tentativa atribuível.
- **DECISÃO:** escolha explicitamente tomada.
- **HIPÓTESE:** interpretação a testar.
- **TENSÃO:** fontes/direções incompatíveis.
- **LACUNA:** informação necessária ausente.
- **EVIDÊNCIA:** unidade rastreável que sustenta/contesta afirmação.

Não converta exposição, frequência ou código existente em “domínio”. Diferencie `IA PROPÔS`, `AUTOR DISSE`, `AUTOR FEZ`, `AUTOR CONFIRMOU` e não confirmado.

## Arquitetura de conhecimento
Preferir corpus único + tags + consultas/lentes. Não criar cópias por agente, tecnologia ou categoria. Relações explícitas devem acrescentar significado que tags não expressem.

## Goals
`READY_FOR_CODEX` é estado operacional, não comentário. Um executor deve realizar apenas Goal autorizado, validar e produzir retorno auditável; não avançar autonomamente ao próximo Goal. Outros agentes podem investigar/preparar material sem falsificar o estado do Goal.

## Multiagente
Codex, Gemini CLI, Cloud Code/Gemini Code Assist, ChatGPT e futuros agentes podem ter especialidades diferentes. Nenhum agente possui uma “verdade própria”: descobertas retornam ao GitHub por evidência, documento ou PR apropriado. Não criar pasta de conhecimento por agente.

## Mudanças
Prefira alterações pequenas, rastreáveis e compatíveis com a estrutura existente. Não sobrescreva história para fazê-la parecer coerente. Não exponha segredos, tokens ou estado local. Quando faltar autorização/evidência, pare ou abra investigação adequada.

## Handoff mínimo
Ao terminar trabalho material, deixe: objetivo executado, fontes/evidências usadas, arquivos alterados, validações, limitações/lacunas e próximo estado permitido.
