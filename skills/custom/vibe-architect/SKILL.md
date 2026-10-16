---
name: vibe-architect
description: Framework socrático de Vibe Coding para conduzir brainstorm até plano de implementação, orquestração de subagentes em ondas paralelas e governança técnica de alta precisão. Ative para planejar novas features, estruturar projetos do zero ou desenhar arquiteturas com custo mínimo de tokens.
---

# 🏛️ Skill: Vibe Architect (Engenharia de Prompt & Arquitetura Socrática)

Esta skill consolida o framework de desenvolvimento assistido por IA de alta disciplina (baseado no Vibe Coding Toolkit e Superpowers).

## 🚀 Quando Ativar
- Sempre que o usuário trouxer uma ideia nova, recurso complexo ou projeto do zero.
- Quando for necessário transformar um pedido vago em um plano de implementação auditável.
- Para organizar grandes tarefas em ondas paralelas sem conflito de concorrência.

## 📋 Sequência de Operação

### Etapa 0: Boot de Memória Integrada (`ai-memory`) & `DOCUMENTACOES/`
- Ao iniciar a sessão no Antigravity, acione `memory_handoff_accept` e `memory_briefing` no MCP `ai-memory` (`workspace = "antigravity"`, `project = "<NOME_DO_PROJETO>"`).
- Inspecione a pasta `DOCUMENTACOES/` do projeto para carregar decisões fundacionais (`_DECISOES.md`), especificações e planos vigentes.

### Etapa 1: Clarificar a Intenção (Sem Código)
Faça perguntas diretas para travar:
1. Como será validado que a tarefa está 'pronta' (`npm run verify` / `bun run verify` em projetos TypeScript, ou `python verificar.py` com código 0).
2. O que fica explicitamente de fora do escopo.
3. Restrições de ambiente e arquiteturais.

### Etapa 2: Desenho da Arquitetura, Documentação e Memória
- **Manutenção Integral de `DOCUMENTACOES/`:** Gere e mantenha toda a documentação rica dentro da pasta `DOCUMENTACOES/` do projeto (`_DECISOES.md` com Prompt Fundacional, `_ESPECIFICACAO.md`, `_WALKTHROUGH.md` e planos em `DOCUMENTACOES/planos_de_implementacao/` com `[STATUS: SUCESSO/FALHA]`).
- **Sincronização `ai-memory`:** Registre decisões, conceitos e armadilhas operacionais no `ai-memory` via `memory_write_page` (`decisions/`, `concepts/`, `gotchas/`).
- Divida o plano em tickets atômicos por ondas paralelas e defina o comando de verificação de cada ticket.

### Etapa 3: Execução Cirúrgica & Verificação Híbrida (`verify` / `verificar.py`)
- Processe estritamente um ticket por vez (Red -> Green -> Refactor).
- Respeite a regra de **1 escritor por vez por arquivo** na colaboração Claude Code (Piloto) $\longleftrightarrow$ Antigravity (Copiloto).
- "Pronto" exige verificação com código `0`: em projetos **TypeScript**, `tsc --noEmit` + testes (`npm test` / `bun test`) + `gitleaks`; em projetos **Python**, `unittest` + `gitleaks`.

### Etapa 4: Governança de Subagentes, Ledger & Circuit Breaker
Quando a execução for delegada a subagentes (`invoke_subagent` com `self`, `code-reviewer`, etc.):
1. **Ledger em Disco (`DOCUMENTACOES/planos_de_implementacao/LEDGER_[PROJETO].md`) + `ai-memory`:**
   - Mantenha o log de bordo em `DOCUMENTACOES/` com o estado de cada tarefa, commits gerados e pendências abertas, e feche a sessão no Antigravity chamando `memory_handoff_begin` (resumo com hash do commit + próximos passos).
2. **Circuit Breaker de Revisão (Teto de 5 Rodadas):**
   - No ciclo de revisão entre implementador e revisor, o limite máximo é de **5 rodadas de ajuste**.
   - Se na 5ª rodada ainda existirem apontamentos pendentes, o loop é travado:
     - O orquestrador assume o papel de árbitro (**Ruling**).
     - Decide explicitamente: aceitar o trade-off temporário com justificativa técnica OU estacionar a pendência como débito técnico menor.
     - Registra a decisão no Ledger e no `ai-memory` e avança para a próxima tarefa. Proibido loop infinito.

### Etapa 5: Heurística de Depuração ("Pare no 3º Patch")
Se um bug persistir após **3 patches de correção consecutivos** (ou se cada patch causar novos erros em cascata):
- **Pare imediatamente.**
- Reconheça o sintoma como defeito estrutural/arquitetural, e não um bug simples.
- Pause o código, relate o diagnóstico ao usuário e discuta a refatoração da arquitetura antes de qualquer nova tentativa.
