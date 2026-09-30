# EurekAI — Web MVP

Este diretório contém o protótipo da interface web interativa do EurekAI, projetada para a experiência de alfabetização em inteligência artificial para usuários leigos.

## Recursos atuais (Fase 1 — Desktop / Web)

- **Acesso direto sem cadastro:** sem logins, senhas ou termos complexos.
- **Seletor de Trilhas:**
  - 🌱 *Iniciante / Adulto Curioso*
  - 🚀 *Criança / Jovem*
  - 🛡️ *Pai, Mãe ou Professor*
- **Laboratório de Contexto (Causa e Efeito):**
  - Simulação de respostas ajustadas por tópico, perfil do ouvinte e nível de temperatura/criatividade.
  - Exibição de princípios fundamentais de uso da IA.
- **Radar Crítico (Caça à Alucinação):**
  - Desafio interativo para treinar a identificação de informações inventadas pela IA.

## Como publicar via GitHub Pages

Um workflow automatizado de deploy está configurado em `.github/workflows/deploy-pages.yml`.

Para ativar no repositório GitHub:

1. Acesse **Settings** > **Pages** no repositório do GitHub.
2. Em **Source**, selecione **GitHub Actions**.
3. A cada push na branch `main`, o conteúdo de `produto/web/` será publicado automaticamente.

## Próximas fases (Roadmap)

1. **Fase 2 (Em breve):** Narração/Áudio guiado usando Web Speech API para acessibilidade.
2. **Fase 3 (Em breve):** Otimização dedicada para telas de smartphones (PWA / Mobile-first).
