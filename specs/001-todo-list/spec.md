# Feature Specification: todo-list

**Feature Branch**: `[todo-list]`

**Created**: 2026-07-06

**Status**: Draft

**Input**: User description: "Quero as mesmas funcionalidades e interfaces: CRUD de tarefas, exclusão lógica (soft-delete), e alteração de status (toggle de conclusão), com interface amigável"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Cadastro de Novas Tarefas (Priority: P1)

Como um usuário, quero poder adicionar novas tarefas com título, descrição e um lembrete (opcional) para que eu possa organizar meus compromissos.

**Why this priority**: O cadastro é o coração do aplicativo. Sem poder adicionar tarefas, o aplicativo não tem utilidade primária.

**Independent Test**: Pode ser testado independentemente preenchendo o formulário de cadastro e verificando se a tarefa aparece na listagem e na base de dados.

**Acceptance Scenarios**:

1. **Given** que estou na página inicial, **When** eu preencho o título e a descrição e clico em salvar, **Then** a tarefa é adicionada à lista e os campos do formulário são limpos.
2. **Given** que tento salvar sem preencher o título, **When** clico em salvar, **Then** recebo um aviso de campo obrigatório e a tarefa não é salva.

---

### User Story 2 - Controle de Conclusão (Priority: P1)

Como um usuário, quero marcar tarefas como concluídas ou pendentes rapidamente para acompanhar meu progresso atual.

**Why this priority**: É essencial para acompanhar o ciclo de vida das atividades gerenciadas.

**Independent Test**: Pode ser testado clicando no ícone de status de uma tarefa e verificando se a mudança é visualmente refletida e persistida.

**Acceptance Scenarios**:

1. **Given** uma tarefa pendente na lista, **When** eu clico no ícone de "check", **Then** a tarefa ganha um estilo de concluída e a estatística de conclusão é atualizada.
2. **Given** uma tarefa concluída, **When** eu clico no ícone novamente, **Then** ela retorna ao estado de pendente.

---

### User Story 3 - Exclusão Segura (Priority: P2)

Como um usuário, quero poder excluir tarefas que não me interessam mais, mas de forma segura, mantendo integridade histórica no sistema (exclusão lógica).

**Why this priority**: Limpeza da interface para melhorar o foco, com garantia de não perder dados permanentemente por acidente sistêmico.

**Independent Test**: Pode ser testado deletando um item e verificando se ele desaparece da interface, porém permanece no banco de dados com uma flag indicadora.

**Acceptance Scenarios**:

1. **Given** uma tarefa na lista, **When** eu clico no botão de lixeira e confirmo, **Then** a tarefa é removida da visualização e a contagem total diminui.

### Edge Cases

- What happens when a descrição fornecida exceder 300 caracteres? (O limite deve ser barrado pela interface para evitar estouro).
- How does system handle envio duplo acidental? (A interface deve bloquear cliques repetidos via flag "isSubmitting").

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: O sistema DEVE permitir a criação de tarefas contendo: título (obrigatório), descrição e lembrete (opcional).
- **FR-002**: O sistema DEVE alternar o status de uma tarefa entre concluída e pendente instantaneamente na interface.
- **FR-003**: O sistema DEVE remover a tarefa da visualização do usuário ao ser deletada, mas marcando o registro como excluído logicamente no backend.
- **FR-004**: O sistema DEVE sanitizar as entradas do usuário, escapando tags HTML (prevenção contra XSS).
- **FR-005**: O sistema DEVE recalcular o painel de métricas sempre que uma tarefa for adicionada, concluída ou excluída.

### Key Entities *(include if feature involves data)*

- **Task**: Representa um compromisso. Atributos chave: ID único, Título, Descrição, Data de Lembrete, Status (Concluída ou não), Data de Criação, e flag de Exclusão Lógica.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Usuários conseguem cadastrar uma nova tarefa em menos de 3 segundos de interação.
- **SC-002**: Alterações de estado (concluir/deletar) refletem visualmente na interface instantaneamente (sem recarregar a página inteira).
- **SC-003**: 100% das inserções de scripts maliciosos (XSS) no título e descrição são neutralizadas antes da exibição.

## Assumptions

- O aplicativo será usado principalmente em desktops ou navegadores modernos, portanto a compatibilidade de layouts foca nas resoluções padrões atuais.
- A persistência inicial em arquivo JSON é suficiente para o escopo e volume de dados esperado.
