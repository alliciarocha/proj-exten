# Feature: Gerenciador de Tarefas

## Requisitos Funcionais

1. **Cadastrar Tarefa:** O sistema deve aceitar um título e uma descrição.
2. **Remover Tarefa:** Deve ser possível excluir uma tarefa via ID ou índice.
3. **Lembretes:** Cada tarefa pode ter um horário/data de lembrete associado.

## Regras de Negócio

- Não permitir tarefas com título vazio.
- O lembrete deve disparar um aviso no console ou interface quando o tempo for atingido.

## Estrutura de Dados (Model)

- `Task { id: int, title: string, done: bool, reminder: datetime }`

## Design System (Referência Figma)

- **Paleta de Cores:**
  - Background: #F9F9F9 (Cinza muito claro)
  - Primary (Botões/Check): #5851DB (Roxo/Azul do design)
  - Text: #2D2D2D (Grafite para leitura)
  - Danger/Delete: #FF4B4B
- **UI/UX:**
  - Bordas: `border-radius: 12px` para cards e inputs.
  - Sombras: `box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05)`.
  - Estética: Minimalista, estilo Soft UI, com bastante respiro (padding).
