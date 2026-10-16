# 🗺️ REGRA MESTRA: GESTÃO DE PORTAS E ISOLAMENTO DE INFRAESTRUTURA

> **Propósito:** Prevenir conflitos de portas de rede, concorrência desordenada e garantir o isolamento físico e lógico entre dezenas de microsserviços e aplicações locais ou em servidores remotos.

---

## ⚖️ 1. Política Padrão de Faixas de Portas (Port Ranges)

Para garantir determinismo em ambientes com múltiplos projetos simultâneos, adote as seguintes faixas padronizadas:

| Faixa de Portas | Categoria de Serviço | Exemplos Típicos |
| :--- | :--- | :--- |
| **`8000 - 8099`** | APIs Internas, Backends & Endpoints REST | FastAPI, Flask, Express APIs, microsserviços Python |
| **`3000 - 3099`** | Aplicações Web Completas & SSR | Next.js, Remotion Studio, Web Apps em Node/Bun |
| **`5173 - 5199`** | Dashboards Leves & SPAs Vite | Vite + React, CesiumJS 3D, Dashboards de monitoramento |
| **`5432 - 5433`** | Bancos de Dados Relacionais | PostgreSQL Local, Docker Containers |
| **`6379 - 6380`** | Bancos em Memória e Mensageria | Redis, BullMQ Cache |
| **`11434`** | Motor de Inferência LLM Local | Ollama (Llama, Mistral, Qwen, DeepSeek) |
| **`20128`** | Gateways de Inteligência Artificial | OmniRoute, Roteadores LLM Multi-Provider |
| **`49374`** | Memória Operacional Unificada (MCP) | `ai-memory` (Servidor Local Claude Code + Antigravity) |

---

## 🚀 2. Protocolo de Abertura de Novo Serviço

Antes de subir qualquer serviço, contêiner ou servidor de desenvolvimento:

1. **Consultar o Mapa Central:** Verifique a tabela de alocação de portas no arquivo `MAPA_DE_RECURSOS.md`.
2. **Checar Disponibilidade Real:**
   ```powershell
   # No Windows PowerShell:
   Test-NetConnection -ComputerName localhost -Port <PORTA>
   Get-NetTCPConnection -LocalPort <PORTA> -ErrorAction SilentlyContinue
   ```
   ```bash
   # No Linux / macOS:
   ss -tulnp | grep <PORTA> || lsof -i :<PORTA>
   ```
3. **Registrar Reserva:** Se a porta estiver livre, registre o nome do projeto, componente e porta no documento de infraestrutura antes de disparar o comando.
4. **Parametrização via Variáveis de Ambiente:** Nunca chumbar a porta no código-fonte. Sempre consumir a variável `PORT` vinda do `.env` com fallback para a porta reservada.

---

## 🔒 3. Isolamento Físico de Workspaces
* Cada projeto possui seu diretório isolado com seu próprio arquivo `.env.example`, dependências (`node_modules/` ou `.venv/`) e documentações.
* Comunicações entre microsserviços devem ocorrer por HTTP/REST ou gRPC respeitando as portas mapeadas, sem acoplamento direto de imports entre repositórios distintos.
