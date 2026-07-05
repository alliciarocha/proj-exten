# TODO List — SPEC-DRIVEN Development

Este projeto consiste no desenvolvimento de uma aplicação web para gerenciamento de tarefas, utilizando a abordagem **Specification-Driven Development (Spec-Driven Development)** por meio do toolkit **spec-kit**. A aplicação foi estruturada seguindo a arquitetura **Model-View-Controller (MVC)**, organizada em um **monorepositório (monorepo)** e utilizando armazenamento em memória local para persistência dos dados durante a execução.

## Funcionalidades

- Cadastrar tarefas (título, descrição, lembrete)
- Remover tarefas com confirmação (exclusão lógica / soft delete)
- Marcar tarefas como concluídas
- Lembretes e estatísticas atualizadas em tempo real
- Filtrar por status (todas, pendentes, concluídas)

## Arquitetura

- **Padrão:** MVC (Model-View-Controller)
- **Estrutura:** Mono-repo
- **Armazenamento:** Arquivo JSON local (`storage.json`)
- **Backend:** Python + Flask
- **Frontend:** HTML/CSS/JS vanilla (Soft UI Premium)
- **Documentação:** MkDocs + Material theme

## Início Rápido

### Clonar

```bash
git clone https://github.com/alliciarocha/proj-exten.git
cd proj-exten
```

### Instalar

Crie seu ambiente virtual e instale as dependências:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Executar

```bash
python main.py
```

Acesse `http://localhost:5000`.

## Estrutura do Projeto

```text
├── .specify/                # Artefatos SPEC-DRIVEN
│   ├── memory/constitution.md
│   └── specs/todo-list/
│       ├── spec.md
│       ├── plan.md
│       ├── tasks.md
│       └── comand.md
├── scr/                     # Código-fonte MVC
│   ├── model/
│   ├── view/
│   └── controller/
├── docs/                    # Documentação MkDocs
├── main.py                  # Entry point
└── mkdocs.yml
```

## Links

- **Aplicação em Produção:** [https://proj-exten.onrender.com/](https://proj-exten.onrender.com/)
- **Repositório:** [https://github.com/alliciarocha/proj-exten](https://github.com/alliciarocha/proj-exten)
- **Documentação Online:** [https://alliciarocha.github.io/proj-exten/](https://alliciarocha.github.io/proj-exten/)

## Licença

MIT
