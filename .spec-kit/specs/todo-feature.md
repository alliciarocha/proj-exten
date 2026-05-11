# Constituição do Projeto: Todo-List SDD

## Justitificativas de Escolhas

1. **Arquitetura MVC:** Escolhida para garantir a separação de responsabilidades. O Model gerencia os dados em memória, a View a interface (CLI ou Web) e o Controller a lógica.
2. **Armazenamento em Memória:** Justifica-se pela simplicidade do escopo acadêmico, eliminando a complexidade de configuração de bancos de dados externos.
3. **Mono-repo:** Facilita a gestão da especificação e do código em um único lugar, garantindo que a IA tenha contexto total do projeto.

## Regras de Implementação

- Linguagem: Python 3.10+.
- Persistência: Apenas variáveis globais ou singletons em memória (Listas/Dicionários).
- Estilo: Seguir PEP 8.
- Documentação: Deve ser compatível com MkDocs.

## Especificação da Interface (View)

A interface deve ser fiel ao layout do Figma:

1. **Header:**
   - Exibir saudação (ex: "Bom dia, Allicia") e a data atual.
2. **Input de Cadastro:**
   - Um campo de texto arredondado com um botão "+" flutuante ou ao lado.
3. **Lista de Tarefas:**
   - Cada tarefa é um card branco independente.
   - À esquerda: Um checkbox circular.
   - Ao centro: Título da tarefa e, abaixo, o horário do lembrete em fonte menor.
   - À direita: Ícone de lixeira (apenas visível no hover ou fixo discretamente).
4. **Filtros (Categorias):**
   - Botões ovais (pills) para "Todas", "Pendentes" e "Concluídas".
