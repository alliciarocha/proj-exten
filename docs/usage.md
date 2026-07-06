# Uso

## Requisitos

- Python 3.11 ou superior
- pip

## Instalacao

Clone o repositorio e instale as dependencias:

```bash
git clone https://github.com/alliciarocha/proj-exten.git
cd proj-exten
```

Crie um ambiente virtual e ative:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

## Executar

```bash
python main.py
```

Acesse `http://localhost:5000` no navegador.

## Como usar

1. Na tela principal, preencha o titulo e a descricao da tarefa.
2. Opcionalmente, defina uma data e hora para o lembrete.
3. Clique em adicionar para cadastrar a tarefa.
4. Use os filtros (todas, pendentes, concluidas) para navegar pelas tarefas.
5. Clique no checkbox para marcar uma tarefa como concluida.
6. Use o botao de editar para alterar titulo, descricao ou lembrete.
7. Use o botao de remover para excluir uma tarefa (exclusao logica).

## API REST

A aplicacao expoe os seguintes endpoints:

| Metodo  | Rota                      | Descricao                        |
|---------|---------------------------|----------------------------------|
| GET     | `/api/tasks`              | Lista tarefas (filtro opcional)  |
| POST    | `/api/tasks`              | Cria nova tarefa                 |
| PUT     | `/api/tasks/<id>`         | Edita tarefa existente           |
| DELETE  | `/api/tasks/<id>`         | Remove tarefa (soft delete)      |
| PATCH   | `/api/tasks/<id>/toggle`  | Alterna status de conclusao      |

### Filtros

Use o parametro `filter` na rota GET:

- `/api/tasks?filter=all` — todas as tarefas
- `/api/tasks?filter=pending` — apenas pendentes
- `/api/tasks?filter=done` — apenas concluidas
