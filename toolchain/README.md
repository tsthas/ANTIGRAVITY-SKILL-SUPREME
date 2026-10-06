# 🛠️ Toolchain & Ecossistema de Programas (Antigravity Stack)

Este diretório documenta todos os programas, utilitários de linha de comando e ferramentas de infraestrutura que compõem o fluxo de desenvolvimento de alta performance do **Antigravity**.

---

## 💻 1. Softwares Essenciais do Desenvolvedor

| Software | Tipo | Finalidade Principal | Comando / Porta |
| :--- | :--- | :--- | :--- |
| **Google Antigravity IDE & CLI** | IDE / CLI Agêntico | Plataforma nativa de engenharia com IA, orquestrador de subagentes e ferramentas MCP. | `agy` |
| **Git para Windows** | Controle de Versão | Rastreamento determinístico de alterações, branches e worktrees. | `git` |
| **GitHub CLI** | Automação Git | Criação de repositórios, pull requests, issues e autenticação via terminal. | `gh` |
| **Node.js (LTS) & npm / npx** | Runtime JavaScript | Execução de tooling moderno, ferramentas MCP (`npx`), Next.js e Vite. | `node`, `npm`, `npx` |
| **Bun** | Runtime Ultra-Rápido | Alternativa de altíssima performance para scripts TypeScript e testes. | `bun` |
| **Python 3.12+ / 3.14** | Linguagem / Scripts | Motor para automações, web scrapers, data science e microsserviços FastAPI. | `python`, `pip` |
| **Astral `uv`** | Gerenciador Python | O resolvedor e instalador de pacotes Python mais rápido do mercado (10x a 100x mais rápido que pip). | `uv pip`, `uv run` |
| **Obsidian** | Segundo Cérebro | Base de conhecimento pessoal em Markdown puro com visualização em grafo para o protocolo Wiki Karpathy. | App Desktop |
| **Docker Desktop** | Virtualização | Orquestração de bancos de dados locais (PostgreSQL, Redis) e contêineres n8n. | `docker`, `docker compose` |
| **Ollama** | LLMs Locais | Execução de modelos de inteligência artificial open-source de forma offline e privada. | `ollama run` (Porta `11434`) |
| **Visual Studio Code** | Editor de Código | Editor secundário e suporte para extensões de linguagens e depuração. | `code` |
| **FFmpeg** | Processamento Multimídia | Manipulação, conversão e corte programático de áudio e vídeo de alta performance. | `ffmpeg` |
| **Cloudflare Tunnels & Turnstile** | Segurança de Borda | Proteção anti-bot inteligente (Turnstile) e publicação de microsserviços sem abrir portas no roteador (Cloudflare Tunnels). | `cloudflared` |
| **OpenSSH & cURL** | Conectividade e Rede | Execução remota segura em servidores Linux e testes rápidos de endpoints HTTP. | `ssh`, `curl` |

---

## ⚡ 2. Instalação com Um Clique (Windows)

Disponibilizamos o script `setup_windows.ps1` que utiliza o **Windows Package Manager (`winget`)** para provisionar todas as ferramentas automaticamente:

```powershell
# Executar como Administrador no PowerShell:
Set-ExecutionPolicy Bypass -Scope Process -Force
.\toolchain\setup_windows.ps1
```

O script instala Git, GitHub CLI, Node.js, Python, Astral uv, VS Code, FFmpeg, Docker Desktop, Ollama e Obsidian de forma silenciosa e configurada.
