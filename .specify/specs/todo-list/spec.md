# Especificação (Spec) — TODO List

## 1. Visão Geral
O Todo List é um gerenciador de tarefas premium construído com a arquitetura MVC (Model-View-Controller) em Flask. O objetivo é fornecer uma aplicação robusta, com persistência local em JSON, sanitização rigorosa e uma interface visual de altíssima qualidade (Soft UI).

## 2. Arquitetura
- **Backend:** Python 3.10+ com Flask.
- **Frontend:** Vanilla HTML/CSS/JS.
- **Padrão:** MVC (Model, View, Controller) com Separação de Preocupações (SoC).
- **Armazenamento:** Persistência serverless baseada em um arquivo `storage.json`.

## 3. Requisitos Funcionais
1. **Adicionar Tarefa:** Título (obrigatório, max 120 char), Descrição (opcional, max 300 char), Lembrete.
2. **Listar Tarefas:** Visualizar tarefas ativas com filtros por status (pendente/concluída).
3. **Concluir Tarefa:** Alternar o status de conclusão (toggle) com atualização no placar em tempo real.
4. **Excluir Tarefa:** Exclusão lógica (Soft Delete), ocultando a tarefa do usuário mas mantendo-a na base com o metadado `deleted_at`.

## 4. Requisitos Não Funcionais
- **Segurança:** Prevenção contra XSS utilizando `html.escape` em todos os inputs.
- **Confiabilidade:** Idempotência nas transações para evitar duplicação em caso de duplo clique.
- **UI/UX:** Design imersivo (Full-Bleed), elementos Glassmorphism e grid geométrico de 8 pontos (8x8 Rule). Ocultação de barras de rolagem nativas.

## 5. Estrutura de Dados (DTO)
Cada tarefa (Task) segue a seguinte estrutura de dataclass:
- `id`: int
- `title`: str
- `description`: str
- `done`: bool
- `reminder`: datetime (opcional)
- `created_at`: datetime
- `updated_at`: datetime
- `deleted_at`: datetime (opcional)
