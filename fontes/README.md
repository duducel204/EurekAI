# Fontes e lotes

Este diretório registra **referências** a fontes; não exige copiar conversas, arquivos privados ou histórico inteiro para o GitHub. O [registro](REGISTRO.md) é a lista operacional de fontes e lotes. Nenhum registro significa acesso presumido a uma fonte.

## Como adquirir uma fonte

1. Identificar a fonte e seu responsável. Testar leitura de um localizador específico antes de marcar **DISPONÍVEL**. Registrar data do teste, escopo efetivamente acessível e limitações.
2. Definir o lote: recorte, versão imutável quando houver (commit, revisão, checksum ou exportação datada) e localizador reproduzível. Registrar `desconhecido` quando data ou ator não puder ser verificado.
3. Preservar o original onde estiver. Para material sensível, registrar somente referência segura e restrita; nunca colar segredo ou dado de terceiro no repositório público. A seleção e revisão do corpus precedem qualquer publicação.
4. Atribuir um ID estável a cada fonte (`F-001`) e a cada lote (`L-001`). Em reprocessamentos, manter o mesmo ID para o mesmo recorte e acrescentar nova revisão ou lote apenas quando escopo/versão mudar. Guardar relações entre lotes sobrepostos para não contar duplicatas como corroboração.
5. Toda extração futura deve apontar ao ID do lote e a um localizador interno preciso (arquivo/linha, mensagem, commit, página ou equivalente), distinguindo texto observado de interpretação. Registrar também transformação, versão do processo e destino da derivação.
6. Marcar o resultado do acesso: **DISPONÍVEL**, **NÃO DISPONÍVEL**, **PRECISA SER EXPORTADA**, **PODE SER AUTOMATIZADA** (possibilidade técnica, não acesso concedido) ou **EXIGE INTERVENÇÃO DO ANDRÉ**. “Não encontrado” significa somente ausência no escopo testado.

## Campos para novas entradas no registro

**Fonte:** ID; nome; natureza; localizador seguro; responsável/ator se verificável; estado de acesso; teste/data/escopo; limites; política de exposição.  
**Lote:** ID; fonte; recorte; versão/checksum; período dos registros quando conhecido; acesso/teste; original ou referência; derivação e destino; sobreposição com outros lotes; próximo passo.

Não criar uma cópia por categoria nem uma pasta por agente. O GOAL-003 pode consumir lotes aprovados pelo ID e localizador, preservando suas limitações.
