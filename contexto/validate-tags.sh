#!/bin/bash
# Script para validar se as tags usadas nos arquivos commitados existem no índice.

INDEX_PATH="/home/duducel204/EurekAI/mapa-do-conhecimento/INDEX-TAGS.md"

# 1. Extrai todas as tags válidas do INDEX-TAGS.md (removendo duplicatas e ordenando)
VALID_TAGS=$(grep -o '#[a-z0-9-]\+' "$INDEX_PATH" | sort -u)

# 2. Identifica os arquivos que estão sendo commitados (staged)
FILES=$(git diff --cached --name-only)

ERROR_FOUND=0

for FILE in $FILES; do
    if [[ -f "$FILE" ]]; then
        # Procura por linhas que comecem com "Tags:" e extrai as tags
        TAGS_IN_FILE=$(grep "^Tags: " "$FILE" | grep -o '#[a-z0-9-]\+')

        for TAG in $TAGS_IN_FILE; do
            if ! echo "$VALID_TAGS" | grep -qxF "$TAG"; then
                echo "❌ ERRO: Tag '$TAG' no arquivo '$FILE' não encontrada em INDEX-TAGS.md"
                ERROR_FOUND=1
            fi
        done
    fi
done

if [ $ERROR_FOUND -eq 1 ]; then
    echo "⚠️  Commit bloqueado. Adicione as tags acima ao índice antes de prosseguir."
    exit 1
fi

echo "✅ Todas as tags validadas com sucesso."
exit 0