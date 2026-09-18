# GOAL-002 — Retorno de execução e validação

**Base examinada:** `main@6f11296776668055aa94ce5c139541bcb97381ad`  
**Escopo:** aquisição e investigação; GOAL-003 não executado.

## Estado Git e estrutura

O `main` foi revalidado antes da execução: contém GOAL-001 concluído, GOAL-002, GOAL-003 previsto e o retorno do GOAL-001. Foram acrescentados apenas `fontes/` (instruções e registro), `investigacao/` (instruções e uma pendência) e este retorno. Nenhuma área existente foi reorganizada ou apagada.

## Fontes e aquisição

O [registro](../../fontes/REGISTRO.md) fixa as fontes acessíveis e o escopo testado: repositório EurekAI e seu histórico. Fontes históricas externas seguem sem localizador e sem teste de acesso, portanto não geraram lote fictício. O [procedimento de aquisição](../../fontes/README.md) define ID estável, recorte, versão, teste de acesso, referência ao original, ator/data quando conhecidos, derivação, deduplicação e processamento incremental. Para material sensível, a referência segura substitui a cópia pública.

## Investigação e handoff

A [fila](../../investigacao/README.md) define quando abrir ticket, campos adaptáveis, estados, handoff e fechamento por ponteiro à evidência incorporada. A única [pendência inicial](../../investigacao/pendencias/INV-001-CORPUS-HISTORICO.md) trata da localização e seleção do corpus histórico necessário ao GOAL-003; decorre do contexto e da lacuna encontrada no GOAL-001. Não foram criadas perguntas especulativas por tópico.

## Validação e limites

O fluxo administrativo pode ser seguido ponta a ponta: a fonte testada recebe ID e lote no registro; a ausência material gera INV-001; o handoff exige fonte, localizador, interpretação separada e limites; o fechamento exige ponteiros ao lote/evidência incorporada. L-001 e L-002 têm sobreposição declarada para evitar dupla contagem. Não houve importação de dados privados, classificação de domínio, criação de capítulos ou mineração do GOAL-003.

**Limite:** ainda não há corpus histórico externo identificado ou selecionado. A fila está funcional, mas o GOAL-003 só terá mineração substantiva quando ao menos uma fonte útil for disponibilizada e testada. “Não encontrado no EurekAI” não equivale a “inexistente”.

## Próxima decisão

André precisa indicar o corpus inicial ou seus localizadores e o que deve permanecer fora do repositório público. Depois de testar acesso e registrar lotes, revisar a prontidão do GOAL-003; não iniciá-lo automaticamente.
