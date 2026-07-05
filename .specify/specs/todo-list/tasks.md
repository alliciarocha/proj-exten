# Tasks — TODO List

Lista de tarefas de implementação do projeto. Como a aplicação já foi desenvolvida, o status atual reflete as entregas já concluídas.

---

## Fase 1: Setup do Projeto
- [x] T01 — Inicializar repositório Git e estrutura de diretórios
- [x] T02 — Configurar ambiente virtual e instalar dependências (`Flask`)

## Fase 2: Modelagem e Persistência
- [x] T03 — Criar classe genérica `Task` (DTO) com dataclasses e timestamps
- [x] T04 — Desenvolver o repositório `TaskStore` (Singleton)
- [x] T05 — Adicionar salvamento e carregamento via JSON
- [x] T06 — Implementar lógica de Soft Delete (`deleted_at`) e tratamento de erros (XSS sanitization)

## Fase 3: API REST (Controller)
- [x] T07 — Criar configuração principal do Flask (`main.py`)
- [x] T08 — Implementar Blueprint `api` para endpoints de listagem de tarefas
- [x] T09 — Criar rota de criação de tarefas (POST) com validações
- [x] T10 — Criar rotas de alternância de status (PATCH) e exclusão (DELETE)

## Fase 4: Frontend Imersivo
- [x] T11 — Criar documento HTML com marcações semânticas e arquitetura de classes baseada em grid
- [x] T12 — Estilizar painel com design Soft UI, Glassmorphism e Cool Blues
- [x] T13 — Implementar lógicas do DOM via Javascript para renderização assíncrona da lista
- [x] T14 — Conectar o frontend com os endpoints do backend via Fetch API
- [x] T15 — Adicionar contadores de tarefas e atualizar dinamicamente no placar

## Fase 5: Entrega e Qualidade
- [x] T16 — Estruturar a documentação arquitetural no diretório `docs` (MkDocs)
- [x] T17 — Criar arquivo `test_app.py` com a suíte de testes unitários em Python
- [x] T18 — Adicionar `vercel.json` e documentar pipeline de deploy contínuo na Vercel
