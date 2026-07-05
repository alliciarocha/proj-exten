# Documentação de Comandos (comand.md)

Este documento centraliza todos os comandos necessários para instalar dependências, configurar o ambiente e executar a aplicação, servindo como referência rápida (cheatsheet) para os desenvolvedores da equipe.

## 1. Ambiente Virtual (Python)
Para não poluir o sistema global com bibliotecas, o projeto isola suas dependências em um ambiente virtual.

**Criar o ambiente virtual (venv):**
```bash
# No Windows
python -m venv venv

# No Linux / macOS
python3 -m venv venv
```

**Ativar o ambiente virtual:**
```bash
# No Windows
.\venv\Scripts\activate

# No Linux / macOS
source venv/bin/activate
```

## 2. Instalação de Dependências
Com o ambiente ativado, você deve instalar as bibliotecas (Flask, etc) listadas no arquivo `requirements.txt`.

**Comando de instalação:**
```bash
pip install -r requirements.txt
```

*(Caso adicione uma nova biblioteca no futuro, você pode atualizar o arquivo usando: `pip freeze > requirements.txt`)*

## 3. Execução do Servidor (Aplicação)
Inicia o backend Flask em modo de desenvolvimento, que automaticamente serve a API e os arquivos estáticos de frontend na porta `5000`.

**Comando de inicialização:**
```bash
python main.py
```
*Acesse no navegador: `http://localhost:5000`*

## 4. Manipulação de Repositório (Git)
Comandos essenciais para o versionamento do projeto.

**Adicionar arquivos e fazer commit:**
```bash
git add .
git commit -m "Descricao objetiva do que foi alterado"
```

**Enviar para o repositório remoto (GitHub):**
```bash
git push origin main
```
