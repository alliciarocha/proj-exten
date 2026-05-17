# Constituição do Projeto: Todo-List SDD (State-of-the-Art Core)

## Princípios Arquiteturais e de Engenharia (OWASP, SOLID & 12-Factor)

1. **Arquitetura MVC & Roteamento:** Separação estrita com base no *Single Responsibility Principle (SRP)*. O Controller gerencia requisições HTTP e erros globais; o Model gerencia regras e persistência abstrata (*Dependency Inversion*).
2. **Transferência de Dados Tipada (DTOs):** Uso de `@dataclass` com serialização e desserialização de atributos e datas no formato ISO 8601.
3. **Segurança por Padrão (OWASP):** Sanitização ativa anti-XSS via `html.escape` e limitação de comprimento de strings (máximo 120 caracteres para títulos e 300 para descrições).
4. **Idempotência & Anti-Concorrência:** O frontend e o backend implementam bloqueio ativo de botões e transações durante envios (`isSubmitting`) para mitigar duplicação acidental por duplo clique.
5. **Observabilidade (Logging Estruturado):** Cada mutação e transação no sistema (criação, edição, exclusão e toggle) emite eventos de log padronizados contendo data/hora, identificador da entidade e desfecho da transação.
6. **Exclusão Lógica (Soft Delete) & Auditoria:** Controle completo do ciclo de vida dos registros (`created_at`, `updated_at`, `deleted_at`). A deleção marca a entidade como arquivada, preservando a trilha de auditoria.

## Regras de Implementação

- Linguagem: Python 3.10+ com tipagem estática obrigatória.
- Persistência: Singleton `TaskStore` sincronizado com o arquivo `storage.json`.
- Qualidade: Exigência de cobertura mínima de testes automatizados de 85% para regras de negócio.
- Estilo: Conformidade estrita com PEP 8.
- Documentação: Padronizada em Markdown (MkDocs e Material Theme).

## Especificação da Interface (View)

A interface segue o design system Soft UI com paleta azul premium (tons frios e modernos):

1. **Header:** Exibir saudação personalizada e data atual na barra lateral.
2. **Cadastro e Edição:** Formulários protegidos contra duplo clique para Título, Descrição e Lembrete (`datetime-local`).
3. **Lista de Tarefas:** Cards autônomos com checkbox circular, título riscado ao concluir, botões de ação com animação de remoção.
4. **Filtros e Busca:** Abas de filtragem e barra de busca instantânea no lado do cliente.
