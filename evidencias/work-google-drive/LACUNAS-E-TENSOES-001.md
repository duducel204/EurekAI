# Lacunas e tensões 001 — Work Google Drive

## T-001 — Norma versus implementação

O briefing define regras rígidas, mas sua existência não comprova enforcement. Localizar contratos, código, testes e logs correspondentes antes de classificar uma regra como implementada.

## T-002 — Estados diferentes do Dream Team

O briefing de 2026-02-20 e a memória de 2026-07-23 descrevem estágios distintos. A memória relata agentes codificados e testados, porém ainda aponta integração ponta a ponta ausente. Não fundir os estados.

## T-003 — Datas internas versus datas do Drive

Alguns arquivos nomeados com 2025 foram criados/modificados no Drive em 2026. Podem ser migrações, reconstruções ou conteúdo simulado. A data no título não deve ser usada como data de origem sem outra evidência.

## T-004 — “Completo” não equivale a cobertura comprovada

O nome `segundo_cerebro_grafo_2026-09-04_completo.json` declara completude, mas isso requer conferência do esquema, fontes ingeridas, contagens e localizadores.

## T-005 — Confiança declarada pela IA

Arquivos derivados registram “confiança cognitiva: 100%”. Esse número é metadado do processo gerador, não medida de veracidade nem validação humana.

## T-006 — Intenção versus operação real

O bootstrap Gemini + Apps Script descreve ciclos automáticos e resultados esperados, mas não foram lidos neste lote logs de execução, `AUDIT.jsonl`, gatilhos ou artefatos gerados que provem implantação.

## Próximos alvos de coleta

- contratos canonizados e eventos de canonização do Dream Team;
- ledger/índice e logs dos testes citados por GD-F-004;
- conteúdo e esquema integral do grafo GD-F-007;
- arquivos de `99_AUDITORIA`, `02_MEMORIA` e `03_PROCESSADOS`;
- código Apps Script e registros de execução;
- originais que sustentam as sínteses de arquitetura;
- linha do tempo que conecte Dream Team, Segundo Cérebro, Eureka e EurekAI.

## Regra de promoção

Uma unidade só deve migrar desta área para o corpus principal após:

1. procedência suficiente;
2. distinção entre declaração, plano, execução e validação;
3. conflito temporal tratado;
4. ausência de segredo ou dado pessoal desnecessário;
5. validação explícita no fluxo do projeto.
