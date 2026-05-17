# ⚡ Deploy da Aplicação e Documentação na Vercel

A **Vercel** é uma plataforma em nuvem extremamente rápida e robusta, excelente alternativa ao GitHub Pages para hospedar sites estáticos ou aplicações web.

---

## 🚀 Como Fazer o Deploy em 3 Minutos

### 1. Conectar seu Repositório GitHub
1. Acesse [https://vercel.com](https://vercel.com) e faça login com a sua conta do GitHub.
2. No painel de controle (*Dashboard*), clique em **"Add New..."** e selecione **"Project"**.
3. Na lista de repositórios do GitHub, encontre `proj-exten` e clique em **Import**.

---

### 2. Configurar o Projeto

Na tela de configuração do projeto na Vercel, defina os seguintes parâmetros para realizar o build automático da documentação MkDocs:

- **Project Name**: `todo-list-docs` (ou o nome de sua preferência)
- **Framework Preset**: Selecione `Other`
- **Root Directory**: `.` (Raiz)
- **Build and Output Settings**:
  - **Build Command**: `pip install mkdocs mkdocs-material && mkdocs build`
  - **Output Directory**: `site`
  - **Install Command**: `pip install -r requirements.txt` (ou deixe o padrão do comando de build)

---

### 3. Concluir e Publicar

1. Clique no botão **Deploy**.
2. A Vercel provisionará um container seguro, baixará o Python e as bibliotecas necessárias, executará o build e gerará a pasta `site`.
3. Em menos de 60 segundos você receberá uma URL de produção customizada com certificado SSL/TLS (HTTPS) gratuito!

---

## 🔄 Deploy Contínuo (CI/CD)

Uma vez conectado, qualquer novo *commit* e *push* para a branch `main` no GitHub acionará de forma instantânea um novo *build* na Vercel, mantendo sua documentação e site estático sempre atualizados.
