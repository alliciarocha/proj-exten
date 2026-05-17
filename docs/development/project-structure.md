# 📂 Estrutura e Organização do Projeto

O repositório do **Todo List** adota uma arquitetura limpa, monolítica (*mono-repo*) e de fácil navegação, agrupando código-fonte, especificações de design e documentação.

---

## 🌳 Árvore Completa de Diretórios

```
proj-exten/
│
├── main.py                    # Ponto de entrada (Servidor Flask e roteamento estático)
├── mkdocs.yml                 # Configuração mestre da documentação MkDocs e tema Material
├── package.json               # Scripts auxiliares do NPM para automação e atalhos
│
├── .github/
│   └── workflows/
│       ├── deploy.yml         # Pipeline CI/CD mestre para deploy no GitHub Pages
│       └── docs.yml           # Pipeline espelho automatizado de documentação
│
├── .spec-kit/
│   └── specs/
│       └── todo-feature.md    # Constituição e documentação do Specification-Driven Development
│
├── docs/                      # Raiz do site de documentação (Markdown)
│   ├── index.md               # Home da documentação
│   ├── quickstart.md          # Guia de início rápido em 5 minutos
│   ├── changelog.md           # Histórico de versões (SemVer)
│   ├── faq.md                 # Perguntas frequentes resolvidas
│   │
│   ├── documentation/
│   │   ├── architecture.md    # Arquitetura MVC e diagramas de sequência
│   │   ├── api.md             # Referência RESTful de endpoints JSON
│   │   └── specification.md   # Especificação e justificativas SDD
│   │
│   ├── deployment/
│   │   ├── github-pages.md    # Como fazer o deploy automatizado via Actions
│   │   ├── vercel.md          # Como hospedar na Vercel
│   │   └── troubleshooting.md # Solução de problemas de publicação e build
│   │
│   └── development/
│       ├── setup.md           # Guia de instalação e ambiente local
│       ├── project-structure.md # Esta página
│       └── testing.md         # Estratégia de testes unitários e E2E
│
└── scr/                       # Código-fonte da aplicação (MVC)
    ├── model/
    │   └── task_model.py      # Dataclass Task, regras e Singleton TaskStore
    ├── controller/
    │   └── task_controller.py # Blueprint Flask com as rotas /api/tasks
    └── view/
        ├── index.html         # Marcação HTML5 e containers do Figma
        ├── style.css          # Design system, Custom Tokens e animações
        └── app.js             # Lógica Vanilla JS, eventos e requisições HTTP Fetch
```

---

## 🔍 Regras de Alocação de Arquivos

1. **Novos Endpoints ou Lógica de Roteamento**: Devem ser criados exclusivamente como funções dentro do Blueprint em `scr/controller/task_controller.py`.
2. **Novas Regras de Negócio e Dados**: Toda alteração no formato das tarefas ou na persistência deve ocorrer em `scr/model/task_model.py`.
3. **Novos Componentes de Interface**: Adicione a estrutura ao `index.html`, o estilo correspondente ao `style.css` e o comportamento em `app.js`.
