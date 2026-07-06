<!--
Sync Impact Report:
- Version change: Initial → 1.0.0
- Modified principles: N/A (Initial Setup)
- Added sections: Performance and UX Standards, Code Organization
- Removed sections: N/A
- Templates requiring updates: 
  - to_do/.specify/templates/plan-template.md (⚠ pending)
  - to_do/.specify/templates/spec-template.md (⚠ pending)
  - to_do/.specify/templates/tasks-template.md (⚠ pending)
- Follow-up TODOs: N/A
-->

# Gerenciador de Tarefas (Todo List) Constitution

## Core Principles

### I. Estrita Arquitetura MVC
O padrão Model-View-Controller DEVE ser usado para separar rigorosamente a lógica de negócios (Model), a interface do usuário (View) e o roteamento (Controller). A separação garante código limpo, manutenível e escalável, e nenhuma exceção deve ser aberta que quebre essa organização lógica.

### II. Simplicidade e Localidade (Flask + JSON)
A aplicação DEVE utilizar Flask como microframework e persistência local através de arquivo JSON (`storage.json`). NÃO devem ser adicionados servidores de banco de dados externos (como PostgreSQL ou MySQL). O foco é manter a leveza do repositório, facilitando testes e deploy.

### III. UI Imersiva e Higienização de Dados (Security-First)
O frontend DEVE seguir as diretrizes de Soft UI Premium, utilizando um sistema de grid de 8x8 pixels para alinhamentos (ex: 8px, 16px, 24px) e paleta harmoniosa. Além disso, a segurança NÃO é opcional: toda entrada do usuário DEVE ser sanitizada rigorosamente (escapando HTML para evitar injeção de XSS) e tamanhos de título/descrição devem ser limitados para evitar estouros de layout.

### IV. Idempotência e Tratamento Transacional
A interface DEVE prevenir envios duplos implementando estados visuais e lógicos de bloqueio (`isSubmitting`) tanto no frontend quanto no backend. A remoção de itens do banco DEVE sempre ser exclusão lógica (soft delete).

### V. Spec-Driven Development Obrigatório
Toda e qualquer nova funcionalidade DEVE ser projetada e especificada através do toolkit Spec-Kit antes de qualquer linha de código ser escrita. Programação desestruturada (vibe coding) é inaceitável, e todo commit deve ser passível de rastreabilidade até sua especificação geradora.

## Performance and UX Standards

Todas as transições visuais (inclusão, alteração de status e exclusão) DEVEM refletir instantaneamente na tela, recalculando métricas de estatística em tempo real e alterando calendários sem a necessidade de refresh completo da página. A UI DEVE esconder barras de rolagem desnecessárias para garantir aparência nativa.

## Code Organization

O código-fonte DEVE estar integralmente isolado nas subpastas apropriadas (por exemplo, dentro do pacote `scr/` do app), não poluindo a raiz do projeto de especificações (que contém configurações como `render.yaml` e arquivos gerados pelo Spec Kit).

## Governance

A Constituição atua como documento fundacional para toda a engenharia deste projeto e tem precedência final sobre qualquer convenção técnica ou framework de terceiros.
As alterações nesta Constituição DEVEM justificar claramente o raciocínio técnico e exigir aprovação unânime. Todo Pull Request ou revisão de código DEVE verificar se a implementação está em conformidade com as regras aqui descritas.

**Version**: 1.0.0 | **Ratified**: 2026-07-06 | **Last Amended**: 2026-07-06
