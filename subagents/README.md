# 🤖 Catálogo de Subagentes Especializados (Antigravity Multi-Agent Squad)

O ecossistema **Antigravity** adota arquitetura de múltiplos agentes cooperativos baseados na taxonomia de subagentes especializados. Em tarefas complexas, o agente orquestrador delega frentes de trabalho para subagentes independentes através do comando `invoke_subagent`.

---

## 👥 Especialistas Disponíveis

| Subagente | Especialidade | Ferramentas Típicas | Quando Convocar |
| :--- | :--- | :--- | :--- |
| **`self`** | Clone Pleno do Orquestrador | Full (Read, Write, Terminal, MCP) | Tarefas autônomas em paralelo em sub-espaços isolados |
| **`research`** | Pesquisador e Rastreador | Read-Only, Busca Web, URL, Docs | Varreduras densas na internet, leitura de docs sem poluir contexto |
| **`code-reviewer`** | Engenheiro Revisor Sênior | Read-Only (Diffs, AST, Codebase) | Auditoria de PRs, verificação pré-merge sob 5 eixos de qualidade |
| **`security-auditor`** | Auditor DevSecOps / Threat Modeling | Read-Only, AST, Security Scan | Auditoria OWASP Top 10, sanitização de inputs, validação RLS e segredos |
| **`test-engineer`** | Engenheiro de QA & Testes | Read, Write (Suítes de teste), Terminal | Criação de testes unitários, integração, E2E e cálculo de cobertura |
| **`web-performance-auditor`** | Engenheiro de Web Performance | Read-Only, Profiling, Chrome DevTools | Diagnóstico de Core Web Vitals (LCP, FID/INP, CLS) e assets |

---

## 🛡️ Protocolo de Governança Multiagente

1. **Ondas Paralelas:** Subagentes disparados na mesma rodada nunca operam no mesmo arquivo simultaneamente.
2. **Ledger Persistente:** O orquestrador mantém o registro em disco de cada tarefa concluída em `DOCUMENTACOES/planos_de_implementacao/LEDGER_[PROJETO].md`.
3. **Circuit Breaker:** Ciclos de bate-rebate entre implementador e revisor têm teto máximo de **5 rodadas**, após as quais o orquestrador arbitra formalmente a entrega.
