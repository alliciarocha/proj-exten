# Research & Technical Decisions: todo-list

## Consolidate Findings

Não houve ambiguidades na especificação que exijam marcadores de `NEEDS CLARIFICATION`. As escolhas tecnológicas refletem diretamente a constituição do projeto.

### Decision 1: Flask for Web Backend
- **Decision**: Utilizar Flask.
- **Rationale**: Requisito mandatário da constituição para microframework leve.
- **Alternatives considered**: Express.js (rejeitado pois a base original era Python), FastAPI (rejeitado por adicionar abstrações desnecessárias para o escopo).

### Decision 2: JSON file storage (`storage.json`)
- **Decision**: Persistência via arquivo JSON.
- **Rationale**: Mantém o projeto contido sem necessitar de containers de BD, facilitando a execução e testes locais por professores.
- **Alternatives considered**: SQLite (mais robusto, mas adiciona complexidade e foi vetado pela regra de constituição).

### Decision 3: Soft Delete and Idempotency
- **Decision**: Uso de flags booleanas `deleted_at` nulas (ou string ISO) no JSON e variáveis `isSubmitting` no JS.
- **Rationale**: Preserva histórico (soft-delete) e impede a criação de registros duplicados ao salvar lentidão na rede (isSubmitting).
- **Alternatives considered**: Deleção física e ausência de bloqueio de formulário (Rejeitadas por baixa qualidade de UX/Segurança).
