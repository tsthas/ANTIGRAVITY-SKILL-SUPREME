# 📐 Workflow: `/arquitetura` — Gestão Arquitetural & Portas Antigravity

Este fluxo define os padrões obrigatórios para a criação e manutenção de sistemas dentro do ecossistema Antigravity.

---

## 1. Gestão de Infraestrutura e Portas (CRÍTICO)

Antes de iniciar qualquer serviço backend ou frontend:

1. **Consultar o Mapa:** Leia a tabela no `MAPA_DE_RECURSOS.md`.
2. **Verificar Disponibilidade:** Certifique-se de que a porta planejada não está alocada.
3. **Registrar Reserva:** Adicione seu projeto e porta ao mapa.
4. **Respeitar as Faixas:**
   * `8000-8099`: APIs / Backends (FastAPI, Express)
   * `3000-3099`: Apps Web (Next.js, Remotion)
   * `5173-5199`: SPAs e Dashboards Vite
   * `11434`: Ollama Local LLMs
   * `20128`: AI Gateways (OmniRoute)

---

## 2. Isolamento de Projeto

* Cada projeto deve residir em seu próprio workspace físico e conter repositório Git isolado.
* Variáveis de ambiente devem residir estritamente no arquivo local `.env`, acompanhado de um `.env.example` sanitizado.

---

## 3. Segurança e Sanitização Defensiva

* Todo projeto que envolva manipulação de arquivos externos deve validar entradas e aplicar sanitização de dados confidenciais antes de persistir em disco.
