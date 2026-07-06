# Validation Quickstart: todo-list

Este guia descreve como rodar e testar manualmente a aplicação de forma independente para validar se os cenários definidos na especificação funcionam fim-a-fim.

## Prerequisites

- Python 3.11+
- Pip (para instalação do Flask)

## Setup Commands

```bash
# Na pasta to_do
python -m venv .venv
# Ativar o virtual environment no Windows:
.\.venv\Scripts\activate
# Instalar requisitos:
pip install Flask
```

## Run Command

```bash
python main.py
```

## Validation Scenarios

1. Abra o navegador em `http://localhost:5000`
2. **Cadastro (Add Task)**: Escreva um título e uma descrição no formulário e clique em "Adicionar Tarefa". A tarefa deve aparecer imediatamente na lista e no painel estatístico no topo.
3. **Toggle (Concluir)**: Clique no círculo ao lado de uma tarefa pendente. O status deve mudar visualmente (riscado) e a contagem de "Concluídas" deve aumentar.
4. **Soft-Delete (Exclusão)**: Clique no ícone de lixeira. A tarefa deve desaparecer da tela e o painel de métricas deve diminuir o contador total. 
5. **Verificação de Backend**: Abra o arquivo `storage.json` gerado na pasta. Verifique se a tarefa excluída ainda existe no arquivo, porém com o campo `deleted_at` preenchido.
