# Data Model & Interface Contracts: todo-list

## Entities

### `Task`
A entidade primária do sistema.

**Attributes**:
- `id` (int): Identificador único, numérico e incremental.
- `title` (string): Título da tarefa (max 120 chars, sanitizado).
- `description` (string): Descrição detalhada da tarefa (max 300 chars, sanitizado).
- `reminder` (datetime string | null): Horário de lembrete (formato ISO 8601).
- `done` (boolean): Estado da tarefa (true = concluída, false = pendente).
- `created_at` (datetime string): Timestamp de criação.
- `deleted_at` (datetime string | null): Marcador de exclusão lógica. Se diferente de nulo, a tarefa não deve ser exibida.

**State Transitions**:
- `done`: `false` <-> `true` (Toggle via UI).
- `deleted_at`: `null` -> `datetime` (Exclusão irremovível).

## Contracts

As rotas da API expostas para o Frontend em Vanilla JS são baseadas em JSON e chamadas AJAX (Fetch API).

### `GET /api/tasks`
Retorna todas as tarefas não deletadas (deleted_at == null).

### `POST /api/tasks`
Cria uma nova tarefa.
- **Payload**: `{ "title": "...", "description": "...", "reminder": "..." }`
- **Returns**: `{ "status": "success", "task": { ... } }`

### `PUT /api/tasks/<id>/toggle`
Alterna a flag `done` da tarefa especificada.
- **Returns**: `{ "status": "success", "done": true/false }`

### `DELETE /api/tasks/<id>`
Altera o campo `deleted_at` da tarefa, efetuando o soft delete.
- **Returns**: `{ "status": "success" }`
