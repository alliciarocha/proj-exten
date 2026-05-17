# ⚙️ Configuração do Ambiente Local (Setup Local)

Guia de configuração avançada para engenheiros de software e colaboradores que desejam modificar a aplicação, a API ou a documentação estática em suas próprias máquinas.

---

## 🛠️ Ferramentas Recomendadas

- **IDE**: Visual Studio Code (VS Code) com as extensões *Python* e *MkDocs*.
- **Controle de Versão**: Git cliente de linha de comando.
- **Navegador**: Google Chrome ou Firefox Developer Edition para inspeção de rede (Network tab) e console JS.

---

## 📦 Setup Passo a Passo

### 1. Clonagem e Configuração do Repositório
```bash
git clone https://github.com/alliciarocha/proj-exten.git
cd proj-exten
```

### 2. Criação do Isolamento Virtual
É vital criar um ambiente virtual (`venv`) para evitar conflitos com pacotes globais do Python:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalação Completa do Ecossistema
Instale todas as dependências necessárias de backend e documentação:
```bash
pip install flask mkdocs mkdocs-material
```

---

## 🖥️ Execução Simulatânea (Backend + Docs)

Ao realizar desenvolvimento ativo, você pode querer testar a aplicação web e visualizar as mudanças da documentação simultaneamente.

### Terminal 1: Servidor Flask (Aplicação Web)
Abra um terminal, ative o ambiente virtual e inicie o backend REST:
```bash
python main.py
```
Acesse `http://localhost:5000` para testar a interface e os endpoints da API.

---

### Terminal 2: Servidor MkDocs (Live Reload da Documentação)
Abra um segundo terminal na mesma pasta e inicie o servidor de documentação com recarregamento instantâneo:
```bash
mkdocs serve
```
Acesse `http://localhost:8000`. Qualquer alteração salva nos arquivos `*.md` dentro de `docs/` será recarregada automaticamente na tela em milissegundos!
