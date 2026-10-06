# 🗺️ Template de Mapa de Recursos & Gestão de Portas

> **Propósito:** Registro central de portas e recursos para garantir que projetos paralelos nunca colidam em portas de rede nem disputem portas de banco de dados.

---

## 📌 Tabela de Cadastro de Portas

| Projeto / Serviço | Componente | Porta Padrão | Protocolo / Stack | Status | Observações |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Portal Central** | Web Frontend | `3000` | Next.js / React | Ativo | Painel de controle principal |
| **API Backend** | Microsserviço Core | `8000` | FastAPI / Python | Ativo | Endpoints e documentação Swagger |
| **Dashboard SPA** | Painel Operacional | `5173` | Vite / React | Ativo | SPA de métricas e controle |
| **PostgreSQL** | Banco Primário | `5432` | Postgres Docker | Ativo | Armazenamento relacional com RLS |
| **Redis** | Filas e Cache | `6379` | Redis Docker | Ativo | Mensageria BullMQ / Celery |
| **Ollama** | LLM Local Offline | `11434` | Ollama Engine | Fixo | Modelos locais (Llama, DeepSeek) |
| **Gateway IA** | AI Router / Proxy | `20128` | OmniRoute | Ativo | Roteamento unificado multi-provedor |

---

## ⚖️ Padrão de Faixas de Rede Recomendado

* **`8000 - 8099`:** APIs Internas e Microsserviços Backend
* **`3000 - 3099`:** Aplicações Web Completas (Next.js, Remix, Remotion)
* **`5173 - 5199`:** Dashboards Leves e SPAs (Vite)
* **`5432 - 5433`:** Bancos de Dados Relacionais
