# GOAL-002 — Aquisição de evidências e fila de investigação

**Status:** READY_FOR_CODEX
**Dependência:** GOAL-001 concluído
**Modo:** EXECUTE + VALIDATE

## Intent
Construir o mecanismo mínimo e eficaz para o EurekAI receber evidências reais da trajetória de André sem exigir que ele reconte manualmente tudo o que sabe. Quando evidência necessária não estiver acessível ao Codex, transformar a ausência em pendência investigável para ChatGPT, outra IA, André ou outra fonte.

## Princípios
1. Não encontrado ≠ inexistente.
2. Exposição ≠ compreensão ≠ uso ≠ solução ≠ reaplicação ≠ domínio.
3. Evidência sobre André deve estar ligada à trajetória de André.
4. Pesquisa pública valida conteúdo técnico, mas não prova conhecimento pessoal.
5. Preservar procedência e incerteza.
6. Não criar arquivos apenas porque existe uma categoria.
7. Uma pendência é ticket de conhecimento, não outro artigo.
8. Evitar entrevista manual conceito por conceito.
9. Automatizar o que puder ser automatizado com segurança.

## In Scope
- Revalidar o estado atual da branch principal antes de agir.
- Usar o contrato do GOAL-001.
- Identificar fontes já acessíveis ao Codex.
- Implementar mecanismo mínimo para registrar fontes/lotes e futuras ingestões.
- Implementar fila de investigação.
- Criar somente diretórios/arquivos administrativos necessários.
- Preparar investigações por Codex, ChatGPT, outras IAs, André, repositórios/arquivos e documentação/web.
- Definir handoff simples para outro pesquisador/agente.
- Permitir fechamento da pendência apontando para a evidência incorporada, sem arquivo duplicado de resultado.
- Criar pendências iniciais somente quando sustentadas pelo contexto e úteis ao GOAL-003.

## Estrutura candidata
investigacao/README.md
investigacao/pendencias/
investigacao/resultados/ somente se necessidade real.

Não criar subpastas por agente sem necessidade demonstrada.

## Quando uma pendência merece arquivo
Somente quando bloquear avanço, exigir outra fonte, exigir validação humana, for material para reconstruir o mapa, houver tensão relevante ou não puder ser resolvida com segurança no Goal atual.

Campos mínimos adaptáveis: ID, status, tópico/pergunta, importância, conhecido, evidências, falta descobrir, fontes sugeridas, tipo de evidência procurada, conclusões proibidas, critério de fechamento, destino da evidência e procedência.

## Aquisição
Para cada fonte/lote: identificar origem; testar acesso; registrar escopo; preservar original ou referência estável; autoria/ator e data quando disponíveis; evitar segredos; registrar derivação; deduplicar sem apagar ocorrências; permitir processamento incremental.

Não exigir cópia integral para o GitHub quando referência/manifesto for suficiente e mais seguro.

## Handoff externo
O retorno deve registrar: pendência; fonte; evidência; localizador; interpretação separada; limitações; estado resolvida/parcial/não resolvida; novos caminhos.

## Out of Scope
Não reconstruir todo o conhecimento; não produzir capítulos; não criar taxonomia definitiva; não classificar domínio; não importar dados privados indiscriminadamente; não criar dezenas de pendências especulativas; não executar GOAL-003 automaticamente; não criar infraestrutura complexa prematuramente.

## Deliverables
Mecanismo de aquisição; mecanismo de investigação; template somente se reutilização justificar; handoff; inventário atualizado de fontes; pendências estritamente justificadas; relatório em codex/retornos/.

## Acceptance Criteria
Informação ausente pode virar investigação rastreável; investigação pode ser entregue isoladamente a outro agente; resultados retornam com procedência; pendência resolvida aponta ao destino final; sem proliferação de arquivos; ausência não vira desconhecimento; sem importação indevida; mecanismo simples e utilizável; GOAL-003 não executado.

## Stop Conditions
Aplicar GOAL-001. Parar se exigir acesso não autorizado, risco de perda, segredo sem política, escolha arquitetônica material sem evidência ou trabalho fora do Goal.

## Return
Estado Git; estrutura; fontes; mecanismo de aquisição; mecanismo de pendências; pendências e justificativas; validação; limitações; prontidão para GOAL-003. Não iniciar GOAL-003.
