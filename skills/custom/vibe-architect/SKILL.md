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

### Etapa 1: Clarificar a Intenção (Sem Código)
Faça perguntas diretas para travar:
1. Como será validado que a tarefa está 'pronta'.
2. O que fica explicitamente de fora do escopo.
3. Restrições de ambiente e arquiteturais.

### Etapa 2: Desenho da Arquitetura e Plano
- Gere a especificação técnica em `DOCUMENTACOES/`.
- Divida o plano em tickets atômicos por ondas paralelas (`DOCUMENTACOES/planos_de_implementacao/`).
- Defina o comando de teste ou verificação de cada ticket.

### Etapa 3: Execução Cirúrgica
- Processe estritamente um ticket por vez (Red -> Green -> Refactor).
- Valide antes de avançar (testes automatizados ou verificação determinística).

### Etapa 4: Governança de Subagentes, Ledger & Circuit Breaker
Quando a execução for delegada a subagentes (`invoke_subagent` com `self`, `code-reviewer`, etc.):
1. **Ledger em Disco (`DOCUMENTACOES/planos_de_implementacao/LEDGER_[PROJETO].md`):**
   - Mantenha o log de bordo append-only com o estado de cada tarefa, commits gerados e pendências abertas.
   - Isso garante que, caso ocorra compactação de contexto (*context compaction*), o orquestrador apenas releia o Ledger e continue sem desvios ou retrabalho.
2. **Circuit Breaker de Revisão (Teto de 5 Rodadas):**
   - No ciclo de revisão entre implementador e revisor, o limite máximo é de **5 rodadas de ajuste**.
   - Se na 5ª rodada ainda existirem apontamentos pendentes, o loop é travado:
     - O orquestrador assume o papel de árbitro (**Ruling**).
     - Decide explicitamente: aceitar o trade-off temporário com justificativa técnica OU estacionar a pendência como débito técnico menor.
     - Registra a decisão no Ledger e avança para a próxima tarefa. Proibido loop infinito.

### Etapa 5: Heurística de Depuração ("Pare no 3º Patch")
Se um bug persistir após **3 patches de correção consecutivos** (ou se cada patch causar novos erros em cascata):
- **Pare imediatamente.**
- Reconheça o sintoma como defeito estrutural/arquitetural, e não um bug simples.
- Pause o código, relate o diagnóstico ao usuário e discuta a refatoração da arquitetura antes de qualquer nova tentativa.

