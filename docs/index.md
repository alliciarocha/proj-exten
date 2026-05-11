# 📝 Todo List — Gerenciador de Tarefas

Aplicação web para gerenciamento de tarefas seguindo a arquitetura **MVC** com Python e Flask.

## Funcionalidades

- ✅ **Cadastrar Tarefa** — título e descrição
- 🗑️ **Remover Tarefa** — exclusão com animação
- ✔️ **Marcar como Concluída** — toggle visual com checkbox
- 🔍 **Filtros** — Todas, Pendentes, Concluídas + busca por nome
- 📅 **Calendário** — mini calendário interativo na sidebar
- 📊 **Estatísticas** — contagem de tarefas concluídas/pendentes

## Como Executar

```bash
# Instalar dependências
pip install flask

# Rodar a aplicação
python main.py
```

Acesse [http://localhost:5000](http://localhost:5000) no navegador.

## Estrutura do Projeto

```
proj exte/
├── main.py                    # Entrada Flask
├── mkdocs.yml                 # Config documentação
├── docs/                      # Páginas MkDocs
├── scr/
│   ├── model/
│   │   └── task_model.py      # Task dataclass + TaskStore
│   ├── controller/
│   │   └── task_controller.py # REST API Blueprint
│   └── view/
│       ├── index.html         # Interface HTML
│       ├── style.css          # Design system CSS
│       └── app.js             # Lógica frontend
└── .spec-kit/                 # Especificações SDD
```

## API REST

| Método   | Endpoint                 | Descrição              |
|----------|--------------------------|------------------------|
| `GET`    | `/api/tasks?filter=all`  | Listar tarefas         |
| `POST`   | `/api/tasks`             | Criar tarefa           |
| `DELETE` | `/api/tasks/<id>`        | Remover tarefa         |
| `PATCH`  | `/api/tasks/<id>/toggle` | Alternar concluída     |
