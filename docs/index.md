# ToDo List

Aplicacao web para gerenciamento de tarefas, desenvolvida com a abordagem Specification-Driven Development (SDD) utilizando o toolkit spec-kit. A aplicacao segue a arquitetura Model-View-Controller (MVC), organizada em monorepo, com persistencia em arquivo JSON local.

## Funcionalidades

- Cadastrar tarefas com titulo, descricao e lembrete opcional
- Remover tarefas com confirmacao (exclusao logica / soft delete)
- Marcar tarefas como concluidas
- Editar tarefas existentes
- Filtrar por status (todas, pendentes, concluidas)
- Lembretes e estatisticas atualizadas em tempo real
- Sanitizacao de entrada contra XSS (OWASP)
- Logs estruturados de transacao (observabilidade)
