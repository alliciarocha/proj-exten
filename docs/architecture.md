# 🏗️ Arquitetura MVC

O projeto segue a arquitetura **Model-View-Controller** para separar responsabilidades.

## Diagrama

```
┌─────────────────────────────────────────────────┐
│                   Browser                       │
│  index.html + style.css + app.js                │
│  (Renderiza cards, envia fetch para API)        │
└──────────────────────┬──────────────────────────┘
                       │ HTTP (JSON)
┌──────────────────────▼──────────────────────────┐
│              Controller (Flask)                  │
│  task_controller.py — Blueprint /api/tasks       │
│  Valida, roteia, serializa                       │
└──────────────────────┬──────────────────────────┘
                       │ Python calls
┌──────────────────────▼──────────────────────────┐
│                Model (Python)                    │
│  task_model.py — Task @dataclass                 │
│  TaskStore singleton (memória)                   │
└─────────────────────────────────────────────────┘
```

## Model

- **`Task`**: dataclass com `id`, `title`, `description`, `done`, `reminder`, `created_at`
- **`TaskStore`**: singleton com lista em memória — sem banco de dados externo

## Controller

- Flask Blueprint `api` em `/api/tasks`
- Endpoints REST: `GET`, `POST`, `DELETE`, `PATCH`
- Validação: título não pode ser vazio (regra de negócio)

## View

- HTML semântico com tags `<main>`, `<aside>`, `<header>`
- CSS com custom properties (design tokens) do Figma
- JavaScript vanilla com `fetch()` para consumir a API
- Renderização dinâmica via DOM manipulation
