# ⚡ Deploy da Aplicação na Vercel

A **Vercel** é uma plataforma em nuvem extremamente rápida e robusta, excelente para hospedar a nossa aplicação Flask.

---

## 🚀 Como Fazer o Deploy

### 1. Preparar o Repositório
A Vercel precisa de um arquivo `vercel.json` na raiz do repositório para entender como executar a aplicação Flask. O arquivo deve ter o seguinte conteúdo:

```json
{
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

E garanta que as dependências (Flask) estão no `requirements.txt`.

### 2. Conectar seu Repositório GitHub
1. Acesse [https://vercel.com](https://vercel.com) e faça login com a sua conta do GitHub.
2. No painel de controle (*Dashboard*), clique em **"Add New..."** e selecione **"Project"**.
3. Na lista de repositórios do GitHub, encontre `proj-exten` e clique em **Import**.

---

### 3. Configurar o Projeto

Na tela de configuração do projeto na Vercel, você não precisa fazer configurações avançadas, pois o arquivo `vercel.json` orientará o build automático da aplicação backend em Python.

- **Project Name**: `todo-list-app` (ou o nome de sua preferência)
- **Framework Preset**: Selecione `Other`
- **Root Directory**: `.` (Raiz)

### 4. Concluir e Publicar

1. Clique no botão **Deploy**.
2. A Vercel provisionará um container com Python, instalará o que está no `requirements.txt`, executará a aplicação via `main.py` e disponibilizará o servidor.
3. Você receberá uma URL de produção customizada com certificado SSL/TLS (HTTPS) gratuito!

---

## 🔄 Deploy Contínuo (CI/CD)

Qualquer novo *commit* e *push* para a branch `main` no GitHub acionará de forma instantânea um novo *build* na Vercel, mantendo sua aplicação sempre atualizada.
