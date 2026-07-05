# Justificativas do Projeto (Escopo e Arquitetura)

Este documento centraliza as escolhas de engenharia de software e metodologias utilizadas no desenvolvimento deste gerenciador de tarefas acadêmico.

---

## 1. Adoção do Padrão MVC (Model-View-Controller)
O padrão MVC foi adotado para garantir a separação de responsabilidades (Separation of Concerns). 
- **Model:** Lida exclusivamente com as regras de negócio e manipulação do armazenamento.
- **View:** Isola a interface do usuário (HTML/JS/CSS), mantendo a lógica visual independente.
- **Controller:** Faz o meio de campo, roteando as requisições HTTP e entregando dados.
Isso garante que o código seja altamente manutenível, testável e escalável, preparando o projeto para evoluções futuras sem gerar dívida técnica.

## 2. Abordagem Spec-Driven Development (SDD)
A utilização da metodologia Spec-Driven Development (via toolkit `.specify/` na raiz do projeto) justifica-se pela necessidade de garantir o rigor da Engenharia de Software desde a concepção. 
O planejamento formal, a criação da Constituição do Projeto e a definição do escopo prévio evitam a prática de "vibe coding" (programação desestruturada). Isso traz previsibilidade, rastreabilidade e melhor garantia de qualidade para as funcionalidades entregues.

## 3. Uso do Python + Microframework Flask
A escolha da linguagem Python em conjunto com o Flask atende ao objetivo de construir uma API REST leve e de altíssima performance. 
Diferente de frameworks completos (como Django), o Flask não impõe uma estrutura engessada, mantendo o monorepositório limpo, de fácil compreensão para a banca avaliadora e focado puramente nos endpoints necessários.

## 4. Armazenamento em Arquivo Local (JSON)
Optou-se por utilizar persistência de dados em arquivo local (`storage.json`) em vez de um banco de dados relacional complexo (como PostgreSQL ou MySQL). 
**Motivos:**
- Elimina a necessidade de instalação de servidores externos para quem clonar o repositório.
- Reduz consideravelmente a barreira de entrada e os "atritos" durante a correção pelo professor.
- Mantém o escopo da aplicação alinhado e suficiente para os objetivos propostos na disciplina.

## 5. Arquitetura de Interface e UX
Foi adotado um Design System customizado (Soft UI Premium) sem a utilização de frameworks pesados de CSS (como Bootstrap ou Tailwind).
O uso de CSS Vanilla com uma paleta de cores curada, grid system múltiplo de 8px e componentes fluidos reforça o domínio da base tecnológica do desenvolvimento frontend e proporciona uma experiência imersiva para o usuário.
