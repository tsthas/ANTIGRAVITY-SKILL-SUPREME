# 🔌 Model Context Protocol (MCP) no Antigravity

O **Model Context Protocol (MCP)** é o padrão aberto universal que permite aos agentes de inteligência artificial interagir com fontes de dados externas, serviços de terceiros e ferramentas de infraestrutura com determinismo.

---

## 🚀 Servidores MCP Homologados na Stack

### 1. 🎨 StitchMCP (Google Stitch)
* **Objetivo:** Geração visual de interfaces de usuário a partir de especificações de texto, criação e aplicação de design systems sem sair do chat.
* **Ferramentas Disponibilizadas:**
  * `create_project`, `get_project`, `list_projects`
  * `generate_screen_from_text`, `get_screen`, `edit_screens`
  * `create_design_system`, `apply_design_system`
* **Configuração:** Requer uma chave da API do Google Cloud (`X-Goog-Api-Key`).

### 2. 🐙 GitHub MCP (`@modelcontextprotocol/server-github`)
* **Objetivo:** Gestão autônoma de repositórios do GitHub, criação de branches, abertura de pull requests, revisão de código e automação de issues.
* **Ferramentas Disponibilizadas:**
  * `create_repository`, `fork_repository`
  * `create_pull_request`, `get_pull_request`, `merge_pull_request`
  * `create_or_update_file`, `push_files`, `list_commits`
  * `create_issue`, `list_issues`, `add_issue_comment`
* **Configuração:** Requer um GitHub Personal Access Token (`GITHUB_PERSONAL_ACCESS_TOKEN`) com escopo `repo`, `workflow`, `read:org`.

### 3. 🎙️ NotebookLM MCP (`notebooklm-mcp`)
* **Objetivo:** Integração com a base de conhecimento do Google NotebookLM, permitindo ingestão de fontes de pesquisa, consultas semânticas em cadernos e geração de visão geral em áudio.
* **Ferramentas Disponibilizadas:**
  * `list_notebooks`, `get_notebook`, `add_notebook`
  * `add_source`, `ask_question`
  * `generate_audio`, `get_audio_status`, `download_audio`
* **Configuração:** Executado via `npx -y notebooklm-mcp run` com autenticação local do Google.

### 4. 🌐 Chrome DevTools MCP (`chrome-devtools-mcp`)
* **Objetivo:** Controle direto de uma instância real do Google Chrome em modo de depuração. Permite inspecionar o DOM em tempo de execução, capturar erros do console e auditar Core Web Vitals.
* **Ferramentas Disponibilizadas:**
  * Inspeção de elementos, captura de prints de tela, análise de rede (waterfall) e auditoria de renderização.

---

## 🛠️ Como Instalar e Ativar

1. Copie o template:
   ```bash
   cp mcp/mcp_config.template.json ~/.gemini/config/mcp_config.json
   ```
2. Substitua os placeholders (`${GITHUB_PERSONAL_ACCESS_TOKEN}`, etc.) com suas chaves reais.
3. Reinicie o Antigravity ou recarregue a sessão. As ferramentas MCP estarão disponíveis imediatamente!
