# Tasks: todo-list

**Input**: Design documents from `/specs/001-todo-list/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan em `scr/`
- [X] T002 Inicializar repositório local e configurar `requirements.txt`
- [X] T003 [P] Configure templates folder and CSS base directory em `scr/templates/` e `scr/static/css/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Setup do microframework Flask básico (App instance) em `scr/main.py`
- [X] T005 Setup da engine de dados baseada em JSON (leitura/escrita básica do `storage.json`) em `scr/models.py`
- [X] T006 Setup base do index.html (Soft UI Premium layout) em `scr/templates/index.html`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Cadastro de Novas Tarefas (Priority: P1) 🎯 MVP

**Goal**: Adicionar novas tarefas com título, descrição e lembrete.

**Independent Test**: Preencher formulário e validar aparecimento na lista de tarefas visível.

### Implementation for User Story 1

- [X] T007 [P] [US1] Criar lógica de adição (append) no Model `scr/models.py`
- [X] T008 [US1] Implementar endpoint GET e POST `/api/tasks` no Controller `scr/views.py` (inclui sanitização e validação de tamanho)
- [X] T009 [P] [US1] Adicionar formulário de nova tarefa com prevenção de isSubmitting no Frontend `scr/templates/index.html`
- [X] T010 [US1] Implementar fetch API (AJAX) no script frontend `scr/static/js/app.js` para chamar POST `/api/tasks`
- [X] T011 [US1] Renderizar dinamicamente a nova tarefa na lista na UI

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Controle de Conclusão (Priority: P1)

**Goal**: Marcar tarefas como concluídas ou pendentes.

**Independent Test**: Clicar no checkbox da tarefa e validar risco no texto e atualização de contador.

### Implementation for User Story 2

- [X] T012 [P] [US2] Criar método toggle no Model `scr/models.py` para alterar o campo booleano `done`
- [X] T013 [US2] Implementar endpoint PUT `/api/tasks/<id>/toggle` no Controller `scr/views.py`
- [X] T014 [US2] Adicionar click event listener nos checkboxes em `scr/static/js/app.js`
- [X] T015 [P] [US2] Estilizar estilo de conclusão (ex: text-decoration: line-through) em `scr/static/css/style.css`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Exclusão Segura (Priority: P2)

**Goal**: Exclusão lógica das tarefas da lista (soft-delete).

**Independent Test**: Clicar na lixeira, validar sumiço da interface e flag `deleted_at` no storage.json.

### Implementation for User Story 3

- [X] T016 [P] [US3] Criar método de soft delete (inserir timestamp em deleted_at) no Model `scr/models.py`
- [X] T017 [US3] Implementar endpoint DELETE `/api/tasks/<id>` no Controller `scr/views.py`
- [X] T018 [US3] Filtrar itens com `deleted_at != null` na listagem principal no GET `/api/tasks` (`scr/views.py`)
- [X] T019 [P] [US3] Adicionar botão de exclusão e seu listener AJAX em `scr/static/js/app.js`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T020 [P] Implementar atualização em tempo real do painel de métricas (Total, Pendentes, Concluídas) no `scr/static/js/app.js`
- [X] T021 Validar prevenção completa de XSS nos outputs no Frontend.
- [X] T022 Escrever o Procfile e render.yaml para deploy em produção apontando para o app principal.
- [X] T023 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete
