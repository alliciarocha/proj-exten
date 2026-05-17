# 📋 Especificação SDD e Constituição Arquitetural

Este documento descreve a constituição e as diretrizes de engenharia de software avançadas que guiam o desenvolvimento do **Todo List**, ratificadas nos artefatos do `.spec-kit/constitution.md`.

---

## 🏛️ Princípios Arquiteturais, Boas Práticas e Justificativas (SOLID, OWASP & 12-Factor)

A arquitetura do sistema foi projetada para garantir resiliência, manutenibilidade e alta fidelidade visual. A seguir, detalham-se as práticas fundamentais e as justificativas técnicas para sua adoção:

### 1. Arquitetura MVC & SRP (Single Responsibility Principle)
- **Prática:** Divisão estrita de responsabilidades entre Model, View e Controller.
- **Justificativa:** Isolar as regras de negócio e persistência (`Model`) da camada de apresentação (`View`) e do roteamento HTTP (`Controller`) permite testar cada componente isoladamente, facilitando a manutenção e futuras expansões sem risco de efeitos colaterais indesejados.

### 2. Transferência de Dados Tipada (DTOs)
- **Prática:** Uso de `@dataclass` no Python para encapsulamento e validação de estruturas de dados.
- **Justificativa:** Garante tipagem estática rigorosa e serialização/desserialização previsível (`to_dict()` e `from_dict()`). Isso previne erros de tipagem em tempo de execução e padroniza a formatação de datas em ISO 8601 para consumo confiável pelo frontend Javascript.

### 3. Segurança por Padrão (OWASP & Sanitização XSS)
- **Prática:** Sanitização completa via `html.escape` de todas as strings recebidas e limitação de comprimento em nível de API (título até 120 caracteres, descrição até 300 caracteres).
- **Justificativa:** Protege o sistema e o navegador do usuário contra ataques de injeção de scripts maliciosos (Cross-Site Scripting) e previne que entradas excessivamente longas desconfigurem ou quebrem o layout da interface.

### 4. Idempotência de Transação (Proteção Anti Duplo Clique)
- **Prática:** Implementação de travas de estado assíncronas (`isSubmitting`) tanto na interface de usuário quanto na camada de controle.
- **Justificativa:** Em redes com latência ou diante de cliques múltiplos rápidos por parte do usuário, a trava impede que múltiplas requisições idênticas sejam processadas simultaneamente, garantindo que uma tarefa não seja criada ou alterada mais de uma vez por acidente.

### 5. Exclusão Lógica (Soft Delete) & Auditoria de Ciclo de Vida
- **Prática:** Ocultação de registros através de metadados de exclusão (`deleted_at`) em vez de deleção física direta no banco de dados.
- **Justificativa:** Em sistemas corporativos e de alta confiabilidade, a deleção física destrói o histórico transacional. A exclusão lógica preserva a integridade referencial, permite auditoria completa do ciclo de vida das tarefas e viabiliza futuras funcionalidades de lixeira ou restauração de dados.

### 6. Observabilidade e Logs Estruturados
- **Prática:** Registro padronizado de cada evento de mutação de estado no backend com identificadores unívocos e timestamps.
- **Justificativa:** Fornece rastreabilidade operacional imediata para depuração de erros e monitoramento de performance em ambiente de produção sem a necessidade de inspecionar a base de dados diretamente.

---

## 🛠️ Padrões de Implementação

- **Linguagem:** Python 3.10+
- **Padrão de Código:** Conformidade estrita com a **PEP 8** e tipagem estática via anotações de tipo.
- **Qualidade de Código:** Meta de cobertura mínima de testes automatizados de 85% para a camada de Model e Controller.
- **Documentação:** Estruturada em Markdown compatível com a suíte MkDocs e Material Theme.

---

## 🎨 Especificação da Interface e Design System (View)

A interface do usuário adota o estilo visual **Soft UI Premium** em layout expansivo de tela cheia (*full-bleed*) estruturado em duas colunas (barra lateral fixa na esquerda com `416px` e área de tarefas expansiva na direita), sob o **sistema de grid de 8 pontos (8x8 rule)** com paleta azul curada e elementos em *glassmorphism*.

### 1. Sistema de Grid (8x8 Rule) e Ergonomia
- **Prática:** Padronização rigorosa de margens, preenchimentos, fontes e dimensões de componentes em múltiplos exatos de 8px (`16px`, `24px`, `32px`, `48px`). Ocultação de barras de rolagem nativas do sistema operacional.
- **Justificativa:** O grid de 8 pontos estabelece um ritmo visual impecável e previsível em qualquer resolução de tela, garantindo alinhamento perfeito. A ocultação das barras de rolagem nativas elimina ruídos visuais cinzas indesejados, mantendo a imersão estética e a sensação premium de um aplicativo desktop dedicado.

### 2. Cabeçalho Principal (Header)
- Saudação personalizada ao usuário em destaque e exibição da data atual formatada na barra lateral.

### 3. Cadastro e Edição de Tarefas
- Campos de texto estilizados e protegidos por travas assíncronas para inserção de **Título**, **Detalhes (Descrição)** e **Lembrete (Data e Hora)**.
- Botão primário com gradiente vibrante e ícone de `+` para confirmação rápida da inclusão.
- Janela modal interativa para edição em tempo real de metadados.

### 4. Gerenciamento e Lista de Tarefas (Cards)
- **Cards Independentes:** Cada tarefa é um componente visual autônomo com indicador de seleção e realce dinâmico no estado *hover*.
- **Conclusão (Checkbox Circular):** Permite alternar instantaneamente o status da tarefa com aplicação automática de estilo riscado.
- **Ações:** Botões de edição e exclusão (com animação suave de saída) e exibição do horário de lembrete agendado.

### 5. Filtros e Pesquisa
- Filtros rápidos em formato *pill* (*Todas*, *Pendentes* e *Concluídas*) que filtram dinamicamente as tarefas ativas na tela em tempo real.
- Barra de busca com filtragem instantânea conforme a digitação do usuário.
