# Plan — TODO List

Plano de ação utilizado para o desenvolvimento da TODO List, focado em entregas incrementais.

## Fase 1: Setup e Fundações
- Inicialização do repositório.
- Definição da arquitetura MVC (Model-View-Controller).
- Configuração do ambiente virtual Python e instalação do Flask.

## Fase 2: Construção do Backend (Model)
- Criação das Dataclasses para representar as Tarefas (DTOs).
- Implementação do Singleton `TaskStore` responsável pela manipulação dos dados.
- Implementação de persistência em arquivo estático (`storage.json`).
- Adição de validações rigorosas e exclusão lógica (Soft Delete).

## Fase 3: Camada de API (Controller)
- Construção do Blueprint da API REST no Flask.
- Exposição das rotas GET (listar), POST (criar), PATCH (concluir/toggle) e DELETE (remover).
- Tratamento de exceções e mapeamento para respostas HTTP amigáveis (ex: 400 Bad Request, 404 Not Found).

## Fase 4: Interface de Usuário (View)
- Desenvolvimento do Frontend (`index.html`) utilizando Vanilla JS e CSS.
- Aplicação do Design System Soft UI Premium (Glassmorphism, cores fluídas, Grid 8x8).
- Integração dinâmica utilizando a Fetch API para consumir os endpoints REST.
- Trava de proteção (idempotência) de duplo clique.

## Fase 5: Qualidade, Deploy e Documentação
- Escrita de testes unitários automatizados para o Model e Controller.
- Configuração de CI/CD para deploy Serverless na Vercel (`vercel.json`).
- Criação e manutenção da documentação do projeto via MkDocs.
