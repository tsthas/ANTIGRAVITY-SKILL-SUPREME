# 🧠 REGRA MESTRA: AMBIENTE FECHADO (CLAUDE CODE + ANTIGRAVITY) & AI-MEMORY

> **Propósito:** Padronizar a operação conjunta entre **Claude Code (Piloto)** e **Google Antigravity (Copiloto)** em ambiente 100% local, unificando a memória operacional via **`ai-memory`** sem abrir mão da documentação estruturada e auditável dentro da pasta `DOCUMENTACOES/` de cada projeto.

---

## 🤝 1. Papéis e Escopo Operacional
1. **Execução 100% Local:** Tudo roda na máquina local por padrão. Nenhuma alteração em servidores remotos sem solicitação explícita do desenvolvedor.
2. **Claude Code = PILOTO:** Decide, integra, executa `git diff` e valida a esteira (`npm run verify` / `bun run verify` ou `python verificar.py`).
3. **Google Antigravity = COPILOTO:** Lê, pesquisa, projeta arquiteturas, audita e edita estritamente os arquivos listados no escopo do projeto.
4. **Um Escritor por Vez:** Nunca dois agentes editam o mesmo arquivo simultaneamente. O dono temporário do arquivo é quem recebeu o handoff ativo.

---

## 🏛️ 2. Dupla Camada de Conhecimento: `ai-memory` + `DOCUMENTACOES/`

O ambiente opera com **duas camadas complementares e inegociáveis**:

### Camada A — Memória Operacional Integrada (`ai-memory`)
* **Servidor Local:** `http://127.0.0.1:49374` (MCP `ai-memory`, dados em `~/.ai-memory`).
* **Parâmetros Obrigatórios nas Tools MCP:**
  * `workspace = "antigravity"`
  * `project = "<NOME_DA_PASTA_DO_PROJETO>"`
* **Papel:** Substitui arquivos efêmeros de passagem de turno (`SESSION_HANDOFF.md` e `TRAPS.md` manuais), sincronizando handoffs entre agentes e indexando decisões rápidas (`decisions/`), conceitos (`concepts/`) e armadilhas (`gotchas/`).

### Camada B — Documentação Estruturada do Projeto (`DOCUMENTACOES/`)
* **Regra Inegociável:** A pasta `DOCUMENTACOES/` dentro de cada projeto **DEVE SER MANTIDA INTEGRALMENTE** como registro humano, histórico e auditável de alto valor.
* **Artefatos Obrigatórios por Projeto em `DOCUMENTACOES/`:**
  * `DECISOES.md` e `YYYYMMDD_HHMM_[PROJETO]_DECISOES.md` contendo no topo o `## 🎯 Prompt Fundacional / Demanda Original` (sanitizado de segredos).
  * Especificações técnicas (`_ESPECIFICACAO.md`) com contratos e critérios *Given/When/Then*.
  * Planos de implementação em `DOCUMENTACOES/planos_de_implementacao/` com tag explícita `[STATUS: SUCESSO/FALHA]` e `LEDGER_[PROJETO].md`.
  * Relatórios de auditoria e `_WALKTHROUGH.md` de entregas concluídas.

---

## 🔄 3. Rito de Abertura e Fechamento de Sessão

| Momento | Claude Code (Piloto) | Google Antigravity (Copiloto) |
| :--- | :--- | :--- |
| **Ao Abrir Sessão** | Os hooks nativos do `ai-memory` injetam o briefing automaticamente + leitura de `DOCUMENTACOES/`. | Chamar **`memory_handoff_accept`** + **`memory_briefing`** (`workspace="antigravity"`, `project="<PROJETO>"`) e inspecionar **`DOCUMENTACOES/`** do projeto. |
| **Durante a Sessão** | Gravar armadilhas/decisões com `memory_write_page` e manter `DOCUMENTACOES/` atualizada. | Gravar armadilhas/decisões com `memory_write_page` e atualizar os documentos em `DOCUMENTACOES/`. |
| **Ao Fechar Sessão** | Hooks encerram a sessão + `stop_gate.py` exige verificação verde (`npm run verify` / `verificar.py`). | **Obrigatório** chamar **`memory_handoff_begin`** (resumo com hash do commit + próximos passos) e atualizar `DOCUMENTACOES/`. |

---

## ✅ 4. Critério "Pronto = Verificado" (Verificação Híbrida TS / Python)
1. Nenhuma tarefa é considerada pronta sem a esteira de verificação retornando **código 0**:
   * **TypeScript (Stack Padrão):** `npm run verify` / `bun run verify` (ou via runner unificado `python verificar.py`), executando obrigatoriamente **`tsc --noEmit` (typecheck estrito)** + suíte de testes do `package.json` (`npm test` / `bun test`) + varredura `gitleaks` limpa.
   * **Python (Exceção Padronizada):** `python verificar.py` executando `unittest` + varredura `gitleaks` limpa.
2. Todo projeto novo nasce como repositório Git isolado, contendo pelo menos 1 teste automatizado na pasta `tests/`.
3. **Ciclo TDD Estrito:** Primeiro o teste que falha (*Red*), depois a menor implementação que passa (*Green*), seguido de refatoração limpa (*Refactor*).

---

## 🔌 5. Conexão MCP do `ai-memory` no Antigravity
Como o cliente MCP do Antigravity envia uma requisição de descoberta proprietária (`{"method": "server/discover"}`) antes do `initialize`, o servidor Rust (`rmcp`) do `ai-memory` rejeitaria a conexão direta se não houvesse tratamento prévio.

Para resolver isso sem expor tokens em arquivos de configuração:
* Utilize o adaptador [`mcp/ai_memory_antigravity.py`](../mcp/ai_memory_antigravity.py), que:
  1. Intercepta `server/discover` antes do handshake `initialize`.
  2. Garante o envio de `notifications/initialized` antes de `tools/list`.
  3. Suporta tanto `ai-memory.exe mcp-bridge` quanto `npx mcp-remote` lendo o token de `~/.ai-memory/auth-tokens/default` em tempo de execução (zero segredos no `mcp_config.json`).
