# .gemini — configuração e skills da ferramenta

Esta pasta pertence à camada operacional do Gemini/Google no workspace.

## O que pode viver aqui
- skills instaladas para Gemini;
- manifestos e metadados da própria ferramenta;
- configuração compartilhável necessária para o ambiente Gemini.

## O que esta pasta NÃO significa
A presença de uma skill ou integração aqui **não** significa que a tecnologia correspondente foi adotada pela arquitetura do EurekAI, nem que existe conhecimento pessoal validado sobre ela.

Exemplos:
- skill de BigQuery disponível ≠ EurekAI usa BigQuery;
- skill de Spark disponível ≠ Spark faz parte da solução;
- acesso a um serviço ≠ decisão de incorporá-lo.

## Regra
Conteúdo gerado/instalado por ferramenta deve permanecer identificado como tooling. Quando surgir conhecimento, decisão, evidência ou experiência relevante, promova somente o que estiver sustentado para a pasta semântica correta seguindo `/AGENTS.md`.

Não armazenar credenciais, tokens, ADC, chaves ou logs sensíveis no Git.
