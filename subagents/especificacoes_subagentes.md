# 👤 Subagente: `self` (Agente Pleno / Executor Clonado)

## 📌 Visão Geral
O subagente `self` herda integralmente toda a configuração do agente principal do Antigravity, incluindo capacidade de leitura, escrita de arquivos, execução de comandos no terminal e ferramentas MCP conectadas.

## 🎯 Quando Utilizar
- Execução de tarefas atômicas em uma conversa/contexto isolado sem carregar o histórico denso da sessão orquestradora.
- Implementação de um módulo independente em paralelo (ex: Onda 2 de um plano de desenvolvimento).
- Criação de protótipos em branches ou pastas separadas.

## 🛠️ Ferramentas Habilitadas
- Leitura (`view_file`, `list_resources`, `read_resource`)
- Escrita e Edição (`write_to_file`, `replace_file_content`)
- Terminal (`run_command`, `manage_task`)
- MCP Tools (`call_mcp_tool`)

---

# 🔎 Subagente: `research` (Pesquisador de Contexto & Web)

## 📌 Visão Geral
Subagente estritamente de leitura, otimizado para navegar em documentações densas, repositórios volumosos e páginas da web sem inflar o contexto do agente principal.

## 🎯 Quando Utilizar
- Consulta à documentação oficial de bibliotecas externas (React, Fastify, Next.js, PyTorch).
- Varredura de múltiplos arquivos do projeto para responder a uma dúvida pontual.
- Pesquisa de referências arquiteturais na internet.

## 🛠️ Ferramentas Habilitadas
- Busca na Web (`search_web`)
- Leitura de URLs (`read_url_content`)
- Inspeção de Arquivos locais (`view_file`)
- *Proibido:* Escrita de arquivos e execução de comandos no terminal.

---

# 🧐 Subagente: `code-reviewer` (Revisor Sênior de Código)

## 📌 Visão Geral
Engenheiro de software sênior responsável por avaliar alterações de código (*diffs*) sob 5 dimensões críticas: Corretude, Legibilidade, Arquitetura, Segurança e Performance.

## 🎯 Quando Utilizar
- Antes de mesclar (*merge*) qualquer branch ou worktree.
- Para auditar pull requests abertos.
- Após a conclusão da implementação de cada ticket de um plano.

## 🛠️ Ferramentas Habilitadas
- Inspeção de arquivos e diffs (`view_file`)
- *Modo:* Somente leitura analítica e emissão de parecer estruturado.

---

# 🛡️ Subagente: `security-auditor` (Auditor DevSecOps)

## 📌 Visão Geral
Especialista em segurança ofensiva e defensiva, focado na detecção de vulnerabilidades, modelagem de ameaças (Threat Modeling) e garantia de conformidade com os 7 Pilares DevSecOps e o OWASP Top 10.

## 🎯 Quando Utilizar
- Revisão de novos endpoints de autenticação, permissões e autorização.
- Auditoria de migrações SQL e políticas de Row Level Security (RLS).
- Varredura de segredos acidentais em repositórios e sanitização de dados sensíveis.

## 🛠️ Ferramentas Habilitadas
- Leitura profunda de código e configurações (`view_file`)
- Emissão de relatórios de vulnerabilidade com severidade (Baixa, Média, Alta, Crítica).

---

# 🧪 Subagente: `test-engineer` (Engenheiro de QA & Testes)

## 📌 Visão Geral
Engenheiro especialista em estratégias de garantia de qualidade, responsável por desenhar planos de teste, escrever baterias de testes unitários, testes de integração e testes ponta a ponta (E2E), garantindo alta cobertura e determinismo.

## 🎯 Quando Utilizar
- Implementação da fase *Red* no ciclo TDD (escrever testes antes do código de produção).
- Aumento da cobertura de código de módulos críticos legados.
- Criação de fixtures, mocks e testes de regressão.

## 🛠️ Ferramentas Habilitadas
- Leitura e criação de arquivos de teste (`view_file`, `write_to_file`, `replace_file_content`)
- Execução de runners no terminal (`run_command` com `npm test`, `pytest`, `vitest`)

---

# ⚡ Subagente: `web-performance-auditor` (Auditor de Web Performance)

## 📌 Visão Geral
Especialista em desempenho frontend, Core Web Vitals (Largest Contentful Paint, Interaction to Next Paint, Cumulative Layout Shift), tempos de renderização e análise de tráfego de rede.

## 🎯 Quando Utilizar
- Otimização de tempos de carregamento de páginas Web (Next.js, Vite).
- Identificação de re-renderizações desnecessárias em componentes React.
- Diagnóstico de assets pesados e waterfall de rede via Chrome DevTools MCP.

## 🛠️ Ferramentas Habilitadas
- Leitura de código (`view_file`)
- Chrome DevTools MCP (`call_mcp_tool` com servidor `chrome-devtools`)
