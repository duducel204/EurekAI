# Contrato canônico de unidade de conhecimento — v1

**Estado:** CANÔNICO PARA O LOTE INICIAL DO GOAL-008
**Framework:** `pedagogia/FRAMEWORK-PEDAGOGICO.md`

Uma unidade sintetiza conhecimento rastreável. Ela não substitui a evidência, não transforma hipótese pedagógica em fato e não copia o corpus bruto.

## Campos

| Campo | Regra |
| --- | --- |
| `id` | Estável, no formato `UC-NNN`. |
| `titulo` | Nome do mecanismo, sem afirmar domínio pessoal. |
| `objetivo` | Compreensão que a unidade pretende permitir. |
| `origem` | Lotes, documentos e localizadores utilizados. |
| `evidencias` | IDs observáveis; distinguir relato, artefato, decisão e lacuna. |
| `relacoes` | IDs de relações; declarar limites e não inventar causalidade. |
| `hipoteses` | Escolhas pedagógicas ou interpretações ainda não demonstradas. Usar `nenhuma` somente com justificativa. |
| `mecanismo_atemporal` | Explicação independente de produto e versão. |
| `exemplos_versionados` | Instanciações com commit/versão e limite explícito. |
| `representacao_inicial` | Analogia ou modelo mental, rotulado como representação. |
| `representacao_alternativa` | Outra forma de explicar o mesmo mecanismo. |
| `terminologia` | Termos técnicos ligados ao mecanismo. |
| `experimento` | Aplicação reproduzível ou justificativa para omissão. |
| `tags` | Tags canônicas existentes. |
| `confianca` | `alta`, `moderada` ou `baixa`, aplicada à síntese e justificada; não mede competência humana. |
| `lacunas` | Ausências, tensões e validações ainda necessárias. |
| `executor` | Agente/processo que gerou a versão, sem atribuir autoria intelectual do corpus. |
| `geracao` | Data, versão da unidade e versão do framework. |

## Regras de validação

1. Cada afirmação factual aponta a uma evidência/localizador ou é removida.
2. Relação observada, hipótese, escolha pedagógica e mecanismo ficam em blocos distintos.
3. Mecanismo atemporal não depende do exemplo; o exemplo informa ferramenta, versão e ambiente.
4. Sucesso em um ambiente não valida outro ambiente.
5. Pendência não vira impossibilidade; frequência não vira competência; commit não resolve autoria intelectual.
6. Toda omissão de campo é explicada na própria unidade.
7. Alterações materiais incrementam a versão e permanecem no histórico Git.

## Entrada em auditoria

Uma unidade só pode ser canonizada após auditoria de procedência, coerência, duplicação, tags, atemporalidade e limites. Falha material devolve a unidade para correção; não é encoberta por aumento de confiança.
