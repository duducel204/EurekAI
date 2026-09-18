# GOAL-002 — Aquisição de evidências e fila de investigação

**Status:** CONCLUÍDO  
**Dependência:** GOAL-001 concluído  
**Modo:** EXECUTE + VALIDATE

## Intent
Construir mecanismo mínimo para receber evidências reais da trajetória de André sem entrevista conceito por conceito e transformar ausências materiais em investigações rastreáveis.

## Contrato preservado
1. Não encontrado ≠ inexistente.
2. Exposição ≠ compreensão ≠ uso ≠ solução ≠ reaplicação ≠ domínio.
3. Evidência pessoal deve estar ligada à trajetória de André.
4. Pesquisa pública pode validar conteúdo técnico; não prova conhecimento pessoal.
5. Preservar procedência e incerteza.
6. Pendência é ticket, não artigo.
7. Evitar proliferação de arquivos.
8. Automatizar com segurança.
9. Registrar fontes/lotes, recorte, versão, localizador, ator/data quando disponíveis, derivação e sobreposição.

## Investigação
Criar pendência somente quando a lacuna bloquear avanço, exigir outra fonte/validação, alterar materialmente o mapa ou envolver tensão relevante. Fechamento aponta para evidência incorporada; não duplica resultado.

## Regra transversal adicionada após conclusão
Fontes, lotes e pendências podem receber **tags** quando isso melhorar recuperação e conexão, seguindo [INDEX-TAGS](../../mapa-do-conhecimento/INDEX-TAGS.md).

Exemplos:
`#chatgpt #api #experiencia`
`#repositorio #mcp #artefato`
`#pendencia #oauth #autoria-incerta`

A tag é índice/lente, não substituto de F-ID/L-ID/INV-ID nem da procedência.

Ao adquirir uma fonte, preservar também derivações reaproveitáveis quando já forem sustentadas, conforme [DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL](DIRETRIZ-TRANSVERSAL-DERIVACAO-REUTILIZAVEL.md), evitando obrigar Goals futuros a reler o mesmo corpus.

## Resultado histórico
O mecanismo foi implementado em `fontes/` e `investigacao/`. GOAL-002 permanece concluído; melhorias futuras são evolução do mecanismo, não reabertura automática deste Goal.
