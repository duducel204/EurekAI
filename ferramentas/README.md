# Ferramentas compartilhadas

Área para scripts e utilitários que servem ao EurekAI como projeto, independentemente de um agente específico.

A ideia é simples: **se Codex, Gemini/Cloud Code e um humano precisam fazer a mesma verificação, ela é candidata a viver aqui**.

## Ferramentas atuais

### `repo_state.py` — versão e concorrência
Verificação read-only do estado Git.

Mostra branch, HEAD local, HEAD remoto de `origin/main`, working tree e, quando recebe a base usada no início do trabalho, informa se essa base ficou antiga e lista arquivos alterados desde então.

```bash
python ferramentas/repo_state.py
python ferramentas/repo_state.py --base <BASE_MAIN_SHA>
```

Se a base ficou antiga, retorna código `2`: isso significa **revisar/reconciliar antes de publicar**, não erro destrutivo.

### `validate_tags.py` — tags canônicas
Confere linhas explícitas `Tags:` nos Markdown do corpus contra `mapa-do-conhecimento/INDEX-TAGS.md`.

```bash
python ferramentas/validate_tags.py
```

Não escaneia `.gemini/`, porque skills de ferramenta não pertencem ao corpus canônico.

### `validate_links.py` — links internos
Confere links Markdown relativos entre arquivos do repositório, ignorando URLs externas, anchors e conteúdo de tooling em `.gemini/`.

```bash
python ferramentas/validate_links.py
```

### `validate_goal_sequence.py` — preflight estrutural da sequência 005→006→007
Confere se os três Goals preparados possuem dependências e seções mínimas de execução/validação.

```bash
python ferramentas/validate_goal_sequence.py
```

Esse teste é estrutural: não substitui Acceptance nem validação semântica de cada Goal.

### `check_all.py` — preflight comum
Executa as verificações compartilhadas acima.

```bash
python ferramentas/check_all.py
python ferramentas/check_all.py --base <BASE_MAIN_SHA>
```

É o comando preferencial antes de commit/push/PR quando o ambiente possui Python.

## Fluxo multiagente recomendado

Ao começar:

```bash
git fetch origin
git rev-parse origin/main
```

Guarde o SHA como `BASE_MAIN_SHA`.

Antes de publicar:

```bash
python ferramentas/check_all.py --base <BASE_MAIN_SHA>
```

Se `repo_state.py` indicar `STALE`, revise o que entrou em `main`, confira conflito textual **e semântico**, reconcilie e rode o preflight novamente.

## Entram aqui
- validações mecânicas;
- utilitários de auditoria;
- scripts reprodutíveis;
- preflights de versão/concorrência;
- automações compartilhadas entre Codex, Gemini/Cloud Code e humanos.

## Não entram aqui
- skills exclusivas do Gemini/Google;
- runtime/locks do Codex;
- credenciais;
- lógica que canonize conhecimento automaticamente;
- ferramentas que façam merge, aprovação ou escrita destrutiva sem gate explícito.

## Regras
- preferir Python standard library quando isso aumentar portabilidade entre Windows, Cloud Shell e outros ambientes;
- usar caminhos relativos ao repositório;
- não conter segredos ou credenciais;
- ser read-only por padrão;
- não usar `git add .` indiscriminadamente;
- não aprovar o próprio PR;
- não habilitar auto-merge sem decisão explícita;
- não escrever em `main` silenciosamente;
- documentar entrada, saída, pré-requisitos, códigos de saída e efeitos colaterais.

## Candidatas futuras — só se houver necessidade real
- auditor geral de coerência entre status dos Goals e roadmap;
- detector de arquivos sensíveis/segredos antes de publicação;
- gerador de handoff mínimo;
- auditor de procedência/localizadores de evidência.

Não criar ferramentas apenas por antecipação. Cada nova ferramenta deve resolver um problema observado por mais de um agente ou reduzir um risco recorrente.

Ferramentas específicas de um agente ficam na área nativa correspondente, como `.gemini/`. Esta pasta não é parte do corpus pedagógico; é infraestrutura compartilhada de construção.
