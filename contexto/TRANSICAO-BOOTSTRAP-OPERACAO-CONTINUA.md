# Transição do bootstrap para operação contínua

**Estado:** GOAL-001–010 formam o bootstrap inicial do EurekAI.  
**Transição:** concluída documentalmente pelo GOAL-010; pipelines ainda dependem de entradas e autorizações reais.

## O que o bootstrap estabeleceu

Contrato epistemológico, aquisição/investigação, inventário de evidências, modelo e relações, progressão/framework pedagógico, contrato de unidades, auditoria e contrato de ingestão. Isso permite incorporar fontes novas sem criar um Goal ad hoc para cada arquivo.

## Ciclo permanente

`nova fonte → autorização/manifesto → inventário → indexação → classificação → mineração seletiva → validação → canonização → atualização de conhecimento/pedagogia → auditoria`

Goals futuros continuam possíveis para mudanças materiais de arquitetura ou decisões delimitadas. O trabalho rotineiro de ingestão usa pipelines versionadas em `pipelines/`.

## Responsabilidades operacionais

- **Codex/local:** scripts determinísticos, indexação, validações, engenharia do repositório e PRs, quando configurado/autorizado.
- **Gemini/Cloud Code:** candidato a triagem ou processamento longo; capacidade depende de configuração, acesso e contrato da execução.
- **ChatGPT:** candidato a síntese, auditoria cognitiva e revisão epistemológica; saídas continuam sujeitas à procedência.
- **André:** autoriza fontes/gates e toma decisões materiais ou humanas.

Esses papéis são responsabilidades preferenciais, não prova de disponibilidade, exclusividade ou decisão de fornecedor.

## Estado e fronteiras

GitHub é memória canônica de contratos e resultados aprovados. Drive/Takeout é fonte, não substituto do repositório. Estado de execução, caches, filas volumosas e dados privados ficam fora do corpus canônico; manifestos compactos entram apenas quando seguros e úteis. Publicação/UI/produto permanecem decisões futuras.

## Primeiro candidato

A pipeline Google Takeout/Drive está definida, não executada. Ela começa por inventário determinístico e processa por item, com retomada e deduplicação. Não há afirmação de acesso, volume ou conteúdo do Takeout.
