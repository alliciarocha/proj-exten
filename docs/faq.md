# 🤔 Perguntas Frequentes (FAQ)

Encontre aqui as respostas rápidas para as dúvidas mais comuns sobre arquitetura, uso e manutenção do **Todo List**.

---

## 🏛️ Questões de Arquitetura e Engenharia

### P: Por que o projeto utiliza armazenamento apenas em memória?
**R:** A escolha de manter o armazenamento em memória (através do padrão Singleton `TaskStore`) é intencional e alinhada à constituição SDD para focar na limpeza da arquitetura MVC e na validação das regras de negócio. Isso elimina o atrito de instalação e configuração de servidores de banco de dados externos (como PostgreSQL ou MongoDB) durante o desenvolvimento e avaliação acadêmica.

### P: O que acontece com os dados ao reiniciar o servidor Flask?
**R:** Como os dados são armazenados na memória RAM do processo Python, reiniciar o script `main.py` reseta as tarefas para o estado inicial padrão (contendo as 4 tarefas de demonstração pré-carregadas).

### P: O projeto foi desenvolvido usando SDD?
**R:** **Sim!** Toda a base de código seguiu as diretrizes de **Specification-Driven Development (SDD)**, com regras estritas de implementação e design registradas nos artefatos da pasta `.spec-kit`.

---

## 💻 Uso da Aplicação e Interface

### P: Como posso filtrar as tarefas?
**R:** Logo acima da grade de tarefas, você encontrará botões em formato de pílula (*pills*) rotulados como **Todas**, **Pendentes** e **Concluídas**. Ao clicar em qualquer um deles, a listagem é atualizada instantaneamente.

### P: Como funciona a barra de busca?
**R:** A barra de busca no canto direito dos filtros atua em tempo real. Conforme você digita qualquer caractere ou palavra, o JavaScript filtra instantaneamente os cards exibidos procurando correspondências tanto no título quanto na descrição da tarefa.

### P: Posso agendar lembretes para qualquer data?
**R:** Sim. O campo de lembrete utiliza o seletor nativo do navegador (`<input type="datetime-local">`), garantindo compatibilidade multiplataforma para escolha de dia, mês, ano e horário exato.

---

## 🔧 Personalização e Documentação

### P: Como adicionar uma nova seção ou página na documentação?
**R:** Crie um arquivo Markdown (ex: `minha-pagina.md`) na pasta `docs/` ou em qualquer subdiretório. Em seguida, edite o arquivo `mkdocs.yml` na raiz do projeto e adicione a nova entrada dentro da seção `nav`:
```yaml
nav:
  - Home: index.md
  - Minha Nova Página: minha-pagina.md
```

### P: Como alterar as cores do tema da documentação?
**R:** O projeto utiliza o **Material for MkDocs**. Você pode alterar a paleta de cores primárias e de destaque diretamente no arquivo `mkdocs.yml`:
```yaml
theme:
  palette:
    - scheme: default
      primary: teal       # Nova cor primária
      accent: deep orange # Nova cor de destaque
```
