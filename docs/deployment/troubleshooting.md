# 🔧 Resolução de Problemas (Troubleshooting de Deploy)

Se você encontrou algum contratempo ao publicar a documentação ou executar a aplicação, consulte esta lista de sintomas e soluções rápidas.

---

## 🛑 Erros no GitHub Actions e Pages

### 1. O site retorna erro 404 (Not Found)
- **Causa Comum**: A configuração em *Settings -> Pages* não está apontada para a fonte correta.
- **Solução**: Certifique-se de que a origem (*Source*) em *Settings -> Pages* esteja definida como **GitHub Actions**.

### 2. O Workflow no GitHub Actions falha com erro de permissão
- **Sintoma**: No log da aba Actions, a etapa `Setup Pages` ou `Deploy to GitHub Pages` exibe uma mensagem de falha de token.
- **Solução**: Verifique se o arquivo `.github/workflows/docs.yml` possui o bloco de permissões explícitas:
```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```

### 3. As imagens ou o CSS não carregam na URL pública
- **Causa Comum**: Caminhos relativos mal formatados ou a propriedade `site_url` incorreta.
- **Solução**: No arquivo `mkdocs.yml`, certifique-se de que o `site_url` está exatamente igual ao seu domínio do GitHub Pages, terminando com barra (`/`).

---

## 🖥️ Erros no Ambiente de Desenvolvimento Local

### 1. `ModuleNotFoundError: No module named 'mkdocs'`
- **Causa**: As bibliotecas do MkDocs e do tema Material não foram instaladas no ambiente Python ativo.
- **Solução**: No terminal, execute:
```bash
pip install mkdocs mkdocs-material
```

### 2. O servidor Flask acusa porta 5000 em uso
- **Sintoma**: `OSError: [Errno 98] Address already in use` ou similar.
- **Solução**: Outro processo ou execução anterior do `main.py` ainda está ativa em segundo plano. Feche os terminais antigos ou encerre o processo do Python no Gerenciador de Tarefas do sistema operacional.
