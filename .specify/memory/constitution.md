# Feature: Gerenciador de Tarefas — Constituição de Software

## 1. Requisitos Funcionais

1. **Cadastrar Tarefa:** O sistema aceita entrada tipada e higienizada para título, descrição e horário de lembrete.
2. **Remover Tarefa:** Exclusão lógica (Soft Delete) via ID, preservando a integridade de histórico e auditoria.
3. **Lembretes e Status:** Alternância instantânea de conclusão (toggle) com recálculo automático em tempo real no placar de estatísticas e destaque visual no minicalendário interativo.

## 2. Regras de Negócio e Práticas de Engenharia

- **Validação e Limitação:** Proibição de títulos vazios e restrição de comprimento (título até 120 caracteres, descrição até 300 caracteres) para prevenir estouro de layout e exaustão de armazenamento.
- **Idempotência Transacional:** Mecanismo de bloqueio ativo (`isSubmitting`) no frontend e backend para impedir duplo envio e duplicação acidental de registros.
- **Sanitização de Segurança (OWASP):** Sanitização obrigatória via escape de strings HTML contra injeção de scripts (XSS).

## 3. Estrutura de Dados (Model & DTO)

- `Task { id: int, title: string, description: string, done: bool, reminder: datetime, created_at: datetime, updated_at: datetime, deleted_at: datetime }`

## 4. Design System & UI Architecture (Soft UI Premium)

- **Layout Imersivo Full-Bleed:** Ocupação total da janela de visualização (`100vw`/`100vh`) dividida em barra lateral fixa na esquerda (`416px`) e painel expansivo de tarefas na direita.
- **Sistema de Grid de 8 Pontos (8x8 Rule):** Rigoroso alinhamento geométrico onde margens, preenchimentos e tamanhos são múltiplos exatos de 8px (ex: `16px`, `24px`, `32px`, `48px`).
- **Paleta Curada (Cool Blues):**
  - Fundo da Página: Gradiente imersivo `#F0F7FF` a `#E0F2FE`
  - Ação Primária / Destaques: Azul Royal Premium (`#2563EB`) e Bright Blue (`#3B82F6`)
  - Superfícies: Branco puro com suporte a *glassmorphism* (`backdrop-filter: blur(24px)`)
- **Ergonomia:** Ocultação de barras de rolagem nativas para manter a imersão de design de aplicativo nativo.
