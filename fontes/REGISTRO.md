# Registro de fontes e lotes

**Última verificação:** 2026-09-18. Estado de acesso e qualidade da procedência são coisas distintas. “Não localizado” em um recorte não significa inexistente.

| ID | Fonte | Acesso testado e escopo | Estado e limite |
| --- | --- | --- | --- |
| F-001 | [EurekAI](https://github.com/duducel204/EurekAI) | Árvore e arquivos lidos em `6f11296776668055aa94ce5c139541bcb97381ad`; revalidação de `main@3f88c0605b4ee21389383fac01d2617f549c5b51` | **DISPONÍVEL**. Contexto e Goals são documentação; não equivalem a experiência pessoal comprovada. |
| F-002 | [Histórico Git do EurekAI](https://github.com/duducel204/EurekAI/commits/main/) | Listagem de commits acessível | **DISPONÍVEL**. Commit não prova autoria intelectual ou domínio. |
| F-003 | Contexto histórico de conversas/projetos via ChatGPT | O retorno parcial anterior relata recuperação em 2026-09-18; o inventário derivado não contém localizadores individuais de origem | **PARCIAL, COM PROCEDÊNCIA PENDENTE**. As 13 entradas E-001 a E-013 não podem ser tratadas como confirmadas sem referências por episódio. |
| F-004 | [Aindre-termux-tradutor](https://github.com/duducel204/Aindre-termux-tradutor) | Árvore, README, STATUS, DECISIONS, teste, workflow e execução de CI consultados em `f29de5b2deb2efe4216a7dc39a0af29184f1ad7f` | **DISPONÍVEL**. Código, relatório de projeto e teste em CI têm forças probatórias diferentes. |
| F-005 | [DTGEapp](https://github.com/duducel204/DTGEapp) | Árvore, README e MEMORIA consultados em `f5d476871dc925421a138a920516b9e93823a2fd` | **DISPONÍVEL**. Documentos relatam mais módulos/testes do que a árvore atual permite confirmar. |

## Lotes registrados

| ID | Fonte | Recorte e versão | Original/localizador | Derivação e sobreposição |
| --- | --- | --- | --- | --- |
| L-001 | F-001 | Árvore de `main@6f11296776668055aa94ce5c139541bcb97381ad` | [Árvore no commit](https://api.github.com/repos/duducel204/EurekAI/git/trees/6f11296776668055aa94ce5c139541bcb97381ad?recursive=1) | Sem extração de conhecimento pessoal; arquivos preservados na origem. |
| L-002 | F-002 | Histórico até `6f11296776668055aa94ce5c139541bcb97381ad` | [Commits](https://github.com/duducel204/EurekAI/commits/main/) | Sobrepõe L-001; commit e arquivo não são corroborações independentes. |
| L-003 | F-003 | Primeiro passe histórico relatado em 2026-09-18 | [Inventário derivado](../experiencias/INVENTARIO-EVIDENCIAS-001.md); originais por episódio **não registrados** | **Provisório**. [Auditoria](../experiencias/AUDITORIA-EVIDENCIAS-001.md) separa corroboração parcial de lacunas; deduplicar contra novas fontes. |
| L-004 | F-004 | Repositório em `f29de5b2deb2efe4216a7dc39a0af29184f1ad7f` e [CI do mesmo commit](https://github.com/duducel204/Aindre-termux-tradutor/actions/runs/35187509452) | Arquivos e URLs por observação no [inventário 002](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | Não tratar STATUS e código do mesmo projeto como fontes pessoais independentes. |
| L-005 | F-005 | Repositório em `f5d476871dc925421a138a920516b9e93823a2fd` | Arquivos e URLs por observação no [inventário 002](../experiencias/INVENTARIO-EVIDENCIAS-002.md) | Relatos de MEMORIA requerem log/código original para comprovar execução. |

A [INV-001](../investigacao/pendencias/INV-001-CORPUS-HISTORICO.md) acompanha a ampliação do corpus e a recuperação de localizadores. Reprocessar por commit/recorte e ID do lote; preservar ocorrências duplicadas, sem contá-las como confirmação independente.
