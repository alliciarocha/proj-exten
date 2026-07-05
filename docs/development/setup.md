# ⚙️ Configuração do Ambiente Local (Setup Local)

Guia de configuração avançada para engenheiros de software e colaboradores que desejam modificar a aplicação ou a API em suas próprias máquinas.

---

## 🛠️ Ferramentas Recomendadas

- **IDE**: Visual Studio Code (VS Code) com a extensão *Python*.
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
Instale todas as dependências necessárias do backend:
```bash
pip install flask
```

---

## 🖥️ Execução Local

### Terminal 1: Servidor Flask (Aplicação Web)
Abra um terminal, ative o ambiente virtual e inicie o backend REST:
```bash
python main.py
```
Acesse `http://localhost:5000` para testar a interface e os endpoints da API.
