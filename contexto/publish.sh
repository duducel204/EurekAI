#!/bin/bash
# Script para automatizar Commit e Pull Request no EurekAI

SCRIPT_DIR="/home/duducel204/EurekAI/scripts"

# 1. Validar Tags antes de prosseguir
echo "🔍 Validando tags..."
"$SCRIPT_DIR/validate-tags.sh"
if [ $? -ne 0 ]; then
    echo "❌ Falha na validação das tags. Corrija antes de publicar."
    exit 1
fi

# 2. Verificar se há alterações
if [ -z "$(git status --porcelain)" ]; then
    echo "ℹ️  Nenhuma alteração para commitar."
    exit 0
fi

# 3. Preparar Branch e Mensagem
read -p "Digite a mensagem do commit: " MESSAGE
if [ -z "$MESSAGE" ]; then
    MESSAGE="Update EurekAI: $(date +'%Y-%m-%d %H:%M')"
fi

# Criar nome de branch baseado na mensagem (simplificado)
BRANCH_NAME="update-$(date +%s)"

echo "🚀 Iniciando processo de publicação..."

# 4. Git Flow
git checkout -b "$BRANCH_NAME"
git add .
git commit -m "$MESSAGE"
git push origin "$BRANCH_NAME"

# 5. Criar Pull Request usando GitHub CLI
# --fill usa o título do commit como título do PR e a descrição automática
if command -v gh &> /dev/null; then
    echo "📦 Criando e configurando Pull Request..."
    PR_URL=$(gh pr create --title "$MESSAGE" --body "Automação EurekAI: Atualização de evidências e documentos." --base main)
    
    if [ $? -eq 0 ]; then
        echo "✅ PR criado: $PR_URL"
        echo "🤖 Ativando aprovação automática e Auto-Merge..."
        gh pr review --approve "$PR_URL"
        gh pr merge --auto --squash "$PR_URL"
    fi
else
    echo "⚠️  GitHub CLI (gh) não encontrado. Faça o push manual ou instale o 'gh'."
fi

git checkout main
echo "🏁 Finalizado."