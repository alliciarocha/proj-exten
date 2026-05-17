# Todo List — Gerenciador de Tarefas Premium

[![Documentação MkDocs](https://img.shields.io/badge/📖_Documentação-MkDocs-2563EB?style=for-the-badge)](https://alliciarocha.github.io/proj-exten/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask MVC](https://img.shields.io/badge/Arquitetura-MVC-0D9488?style=for-the-badge)](https://alliciarocha.github.io/proj-exten/)

Um gerenciador de tarefas moderno, elegante e robusto, construído sob o padrão arquitetural **MVC (Model-View-Controller)** e os princípios do **Specification-Driven Development (SDD)**. A interface foi rigorosamente desenhada com a estética **Soft UI Premium**, elementos em *glassmorphism* e conformidade com o sistema de grid de 8 pontos (8x8 rule).

🔗 **[Acesse a Documentação Oficial Completa](https://alliciarocha.github.io/proj-exten/)**

---

## ✨ Principais Funcionalidades & Destaques

- **Interface Imersiva Full-Bleed:** Janela de visualização expansiva em tela cheia com paleta azul premium (`Cool Blues`) e total imersão visual sem barras de rolagem nativas.
- **Minicalendário & Placar em Tempo Real:** Acompanhamento interativo do calendário mensal e contadores automáticos de tarefas concluídas e pendentes.
- **Idempotência & Proteção Anti-Duplo Clique:** Travas ativas (`isSubmitting`) no frontend e no backend para evitar duplicação acidental de registros.
- **Exclusão Lógica (Soft Delete):** Metadados de auditoria completos (`created_at`, `updated_at`, `deleted_at`). A exclusão oculta o registro sem apagar o histórico físico.
- **Segurança Robusta (OWASP):** Higienização de entradas (XSS sanitization via `html.escape`) e validação rigorosa de DTOs tipados em Python (`@dataclass`).

---

## 🚀 Como Executar Localmente

### 1. Pré-requisitos
- Python 3.10 ou superior.

### 2. Passo a Passo

```bash
# Clone o repositório
git clone https://github.com/alliciarocha/proj-exten.git
cd proj-exten

# Execute a aplicação Flask (o backend e o servidor estático serão iniciados)
python main.py
```

O servidor estará disponível no seu navegador em: **`http://127.0.0.1:5000`**

---

## 📚 Documentação e Especificação Arquitetural

Toda a arquitetura de código, endpoints da API REST, decisões de design system e justificativas de engenharia estão minuciosamente registradas em nosso portal gerado via MkDocs:

👉 **[Portal de Documentação — Gerenciador de Tarefas](https://alliciarocha.github.io/proj-exten/)**

---
*Desenvolvido com foco na excelência visual, manutenibilidade de longo prazo e melhores práticas de engenharia de software.*
