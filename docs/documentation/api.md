# 🔌 Referência Completa da API REST

A API do **Todo List** segue os princípios RESTful, retornando respostas no formato JSON e utilizando códigos de status HTTP semânticos para indicar o resultado das operações.

---

## 🌐 Endpoints Disponíveis

```
URL Base: http://localhost:5000/api/tasks
```

| Método | Endpoint | Parâmetros / Query | Corpo (JSON) | Retorno Sucesso |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/tasks` | `?filter=all\|pending\|done` | *Nenhum* | `200 OK` |
| **POST** | `/api/tasks` | *Nenhum* | `{title*, description, reminder}` | `201 Created` |
| **PUT** | `/api/tasks/<id>` | *Nenhum* | `{title*, description, reminder}` | `200 OK` |
| **PATCH**| `/api/tasks/<id>/toggle`| *Nenhum* | *Nenhum* | `200 OK` |
| **DELETE**|`/api/tasks/<id>` | *Nenhum* | *Nenhum* | `204 No Content`|

---

## 📖 Detalhamento dos Métodos

### 1. Listar Tarefas (`GET /api/tasks`)

Retorna a lista de tarefas cadastrada no sistema, filtrada de acordo com o parâmetro opcional, além da contagem em tempo real.

#### Query Parameters
- `filter` (opcional): `"all"` (padrão), `"pending"` ou `"done"`.

#### Exemplo de Resposta (200 OK)
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Estudar Python",
      "description": "Revisar laços de repetição (Loop).",
      "done": false,
      "reminder": "2026-05-09T22:59:00",
      "created_at": "2026-05-17T12:00:00.000000"
    }
  ],
  "count_done": 0,
  "count_pending": 1
}
```

---

### 2. Criar Tarefa (`POST /api/tasks`)

Cria uma nova tarefa no armazenamento em memória.

#### Corpo da Requisição (JSON)
```json
{
  "title": "Comprar café",
  "description": "Grãos moídos na hora",
  "reminder": "2026-05-20T15:30:00"
}
```
*Observação: `title` é obrigatório. `description` e `reminder` são opcionais.*

#### Exemplo de Resposta (201 Created)
```json
{
  "id": 5,
  "title": "Comprar café",
  "description": "Grãos moídos na hora",
  "done": false,
  "reminder": "2026-05-20T15:30:00",
  "created_at": "2026-05-17T12:35:00.123456"
}
```

#### Respostas de Erro Comuns
- **`400 Bad Request`**: Quando o título está ausente ou vazio.
```json
{
  "error": "O título da tarefa não pode ser vazio."
}
```

---

### 3. Editar Tarefa (`PUT /api/tasks/<id>`)

Atualiza integralmente as informações de título, descrição e lembrete de uma tarefa específica.

#### Corpo da Requisição (JSON)
```json
{
  "title": "Comprar café descafeinado",
  "description": "Pacote de 500g",
  "reminder": "2026-05-21T10:00:00"
}
```

#### Exemplo de Resposta (200 OK)
Retorna o objeto da tarefa com os dados atualizados.
- **`404 Not Found`**: Se o ID da tarefa não existir.

---

### 4. Alternar Status de Conclusão (`PATCH /api/tasks/<id>/toggle`)

Inverte o estado do atributo `done` (*true* para *false* ou vice-versa).

#### Exemplo de Resposta (200 OK)
```json
{
  "id": 1,
  "title": "Estudar Python",
  "description": "Revisar laços de repetição (Loop).",
  "done": true,
  "reminder": "2026-05-09T22:59:00",
  "created_at": "2026-05-17T12:00:00.000000"
}
```

---

### 5. Excluir Tarefa (`DELETE /api/tasks/<id>`)

Remove a tarefa permanentemente da memória.

#### Resposta de Sucesso
- **`204 No Content`** (corpo da resposta vazio).
- **`404 Not Found`**: Se a tarefa solicitada não for encontrada.
