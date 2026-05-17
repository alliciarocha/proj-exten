# 📜 Changelog (Histórico de Versões)

Todas as modificações e evoluções notáveis no projeto **Todo List** são documentadas nesta página, seguindo as diretrizes do *Semantic Versioning* (SemVer).

---

## [1.2.0] — 2026-05-17

### ✨ Adicionado
- **Documentação MkDocs Completa**: Estruturação de 14 arquivos profissionais contemplando guias de arquitetura, SDD, testes, CI/CD e setup.
- **Suporte a Edição via PUT**: Novo endpoint REST `/api/tasks/<id>` (PUT) integrado com janela modal no frontend para edição ao vivo de tarefas.
- **Scripts NPM de Bônus**: Configuração do `package.json` provendo atalhos rápidos `npm run docs` e `npm run docs:build`.

### 🎨 Modificado
- **Refinamento Visual do Header**: A borda da foto de perfil do usuário na barra de navegação foi removida e a imagem padronizada de acordo com as especificações visuais do Figma.
- **Melhorias de Contraste e Responsividade**: Otimização das regras CSS Media Queries para dispositivos móveis (`max-width: 768px`).

---

## [1.1.0] — 2026-05-10

### ✨ Adicionado
- **Sistema de Lembretes**: Integração do campo `datetime-local` no frontend com o backend Flask, permitindo persistir o atributo `reminder` na dataclass `Task`.
- **Estatísticas Dinâmicas**: Implementação de *properties* na classe `TaskStore` (`count_done` e `count_pending`) retornadas em tempo real na listagem da API.

### 🐛 Corrigido
- Tratamento de exceções e retorno de erro `400 Bad Request` ao tentar cadastrar tarefas com título vazio ou contendo apenas espaços em branco.

---

## [1.0.0] — 2026-05-01

### 🚀 Lançamento Inicial
- **Arquitetura Base**: Implementação do padrão MVC com Flask Blueprint em `/api/tasks`.
- **Persistência em Memória**: Criação do `TaskStore` Singleton para gerenciamento de estado sem dependências de banco de dados.
- **Interface Soft UI**: Entrega da estrutura HTML5 semântica e do design system em Vanilla CSS.
