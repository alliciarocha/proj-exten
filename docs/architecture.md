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
├── .specify/                # Configurações do Spec Kit
│   └── memory/constitution.md
├── specs/                   # Artefatos SPEC-DRIVEN
│   └── 001-todo-list/
│       ├── spec.md
│       ├── plan.md
│       ├── research.md
│       ├── data-model.md
│       ├── quickstart.md
│       └── tasks.md
├── scr/                     # Código-fonte MVC
│   ├── model/
│   ├── view/
│   └── controller/
├── docs/                    # Documentação MkDocs
├── main.py                  # Entry point
└── mkdocs.yml
```

