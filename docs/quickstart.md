# 🚀 Início Rápido (Quickstart)

Em apenas 5 minutos você terá o ambiente de desenvolvimento configurado e a aplicação rodando localmente na sua máquina.

---

## 📋 Pré-requisitos

Certifique-se de ter instalado em seu sistema:
- **Python 3.10** ou superior
- **Git** para clonar o repositório
- (Opcional) **Node.js / npm** caso queira utilizar os comandos de script bônus

---

## ⚙️ Instalação Passo a Passo

### 1. Clonar o Repositório
Abra seu terminal ou prompt de comando e execute:
```bash
git clone https://github.com/alliciarocha/proj-exten.git
cd proj-exten
```

### 2. Criar e Ativar Ambiente Virtual (Recomendado)
Para manter as dependências isoladas:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
Instale o Flask e o gerador de documentação:
```bash
pip install flask mkdocs mkdocs-material
```

### 4. Iniciar o Servidor de Desenvolvimento
```bash
python main.py
```

O servidor será iniciado na porta 5000. Abra o seu navegador favorito e acesse:
```
http://localhost:5000
```

---

## 🎯 Seus Primeiros Passos na Aplicação

### Criando sua Primeira Tarefa
1. Na barra superior do painel principal, localize os campos **"Título da tarefa"** e **"Detalhes da tarefa"**.
2. Digite um título (ex: *"Revisar documentação"*) e adicione uma descrição curta.
3. Se desejar, clique no ícone de calendário para definir uma data e hora para o lembrete.
4. Clique no botão de **`+`** com gradiente laranja. A tarefa aparecerá instantaneamente como um card na sua grade!

### Concluindo e Removendo Tarefas
- **Concluir**: Clique no círculo (checkbox) à esquerda do título do card. O título será riscado e o contador de concluídas na barra lateral será incrementado na hora.
- **Editar**: Posicione o mouse sobre o card e clique no ícone de lápis para abrir o modal de edição em tempo real.
- **Excluir**: Posicione o mouse sobre o card e clique no ícone de lixeira. O card desaparecerá com uma animação suave.
