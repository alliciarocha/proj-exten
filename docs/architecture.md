# Arquitetura

A aplicacao segue o padrao MVC (Model-View-Controller), estruturada em monorepo.

## Tecnologias

- **Backend:** Python 3 + Flask
- **Frontend:** HTML, CSS e JavaScript vanilla (Soft UI Premium)
- **Persistencia:** Arquivo JSON local (`storage.json`)
- **Documentacao:** MkDocs + Material theme
- **Deploy:** Render (backend) + GitHub Pages (documentacao)

## Estrutura do Projeto

```text
├── main.py                  # Ponto de entrada Flask
├── scr/
│   ├── model/
│   │   ├── task_model.py    # Entidade Task, TaskStore (Singleton/Repository)
│   │   └── storage.json     # Persistencia em arquivo JSON
│   ├── view/
│   │   ├── index.html       # Interface HTML
│   │   ├── style.css        # Estilos (Soft UI Premium)
│   │   └── app.js           # Logica do frontend
│   └── controller/
│       └── task_controller.py  # API REST (Blueprint Flask)
├── docs/                    # Documentacao MkDocs
├── specs/                   # Artefatos Spec-Driven
├── mkdocs.yml
├── requirements.txt
├── render.yaml              # Configuracao de deploy no Render
└── Procfile
```

## Camadas

### Model (`scr/model/task_model.py`)

- Entidade `Task` com dataclass e metadados de auditoria (`created_at`, `updated_at`, `deleted_at`)
- `TaskStore` implementa o padrao Singleton e Repository
- Persistencia em arquivo JSON (`storage.json`)
- Exclusao logica (Soft Delete)
- Validacao e sanitizacao de entrada (limite de caracteres, protecao contra XSS)
- Logs estruturados de transacao
- Excecoes de negocio padronizadas (`ValidationError`, `EntityNotFoundError`)

### View (`scr/view/`)

- Interface HTML/CSS/JS vanilla com design Soft UI Premium
- Comunicacao com o backend via API REST (fetch)
- Filtros de status, edicao inline e lembretes visuais

### Controller (`scr/controller/task_controller.py`)

- Blueprint Flask com prefixo `/api/tasks`
- Endpoints RESTful: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`
- Tratamento global de excecoes com respostas JSON padronizadas
