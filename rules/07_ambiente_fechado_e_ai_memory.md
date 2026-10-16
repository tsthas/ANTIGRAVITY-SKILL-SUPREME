# 🧠 AMBIENTE FECHADO (Claude Code + Antigravity) com ai-memory — resumo e modelo

> **Fonte única:** a versão operacional e completa deste contrato fica em `_AMBIENTE/REGRAS.md`, na raiz do seu workspace local. Este arquivo é um **resumo para quem baixa o repositório**: copie o `REGRAS.md` do seu ambiente, não mantenha duas versões. Se divergirem, vale o `REGRAS.md`.

## 1. Papéis
1. Tudo roda **local** por padrão; nada em servidor remoto sem pedido explícito.
2. **Claude Code = piloto** (decide, integra, confere `git diff`, valida). **Antigravity = copiloto** (lê, pesquisa, audita; edita só os arquivos listados).
3. **Um escritor por vez** em cada arquivo.

## 2. Duas camadas de conhecimento
- **`ai-memory`** (servidor local, MCP): handoff entre agentes, decisões, conceitos e armadilhas. Parâmetros nas chamadas MCP: `workspace` e `project` (nome da pasta do projeto).
- **`DOCUMENTACOES/` do projeto**: registro humano e auditável (decisões, especificações, planos, walkthroughs). Continua sendo mantida; o ai-memory não a substitui.

## 3. Abrir e fechar sessão
| Momento | Claude Code | Antigravity |
| :--- | :--- | :--- |
| Abrir | hooks do ai-memory entregam o briefing | `memory_handoff_accept` + `memory_briefing` e leitura de `DOCUMENTACOES/` |
| Fechar | hooks encerram a sessão | **obrigatório** `memory_handoff_begin` (resumo com hash do commit + próximos passos), pois não há gancho de fim de sessão |

## 4. Pronto = verificado
Nada é "pronto" sem a verificação do projeto retornando código 0 (testes + varredura de segredos). Novo código: teste que falha primeiro (Red), depois o mínimo para passar (Green). Todo bug corrigido ganha um teste de regressão.
> Status: Perfis Python e TypeScript implementados. Em projetos TypeScript, a verificação exige `tsc --noEmit` estrito quando há código em `src/` ou `tsconfig.json`, executa testes automatizados (nativos com Node 26 em `tests/smoke.test.ts` ou via `package.json` / `bun test`) e realiza varredura de segredos com `gitleaks`.

## 5. Capturar só o que deve ser capturado
Use o modo *allowlist* do ai-memory com um `.ai-memory.toml` na raiz do workspace e `ignore_paths` para `.env`, chaves e credenciais. Fora da árvore autorizada, nada é capturado.

## 6. Conexão MCP do ai-memory no Antigravity
O cliente MCP do Antigravity envia `{"method": "server/discover"}` antes do `initialize`, e o servidor Rust (`rmcp`) do ai-memory recusa a conexão direta. Use o adaptador [`mcp/ai_memory_antigravity.py`](../mcp/ai_memory_antigravity.py), que trata a descoberta, garante `notifications/initialized` antes de `tools/list` e lê o token em tempo de execução, sem segredos no `mcp_config.json`.
