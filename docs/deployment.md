# Implantacao

## Aplicacao (Render)

A aplicacao esta configurada para deploy no Render usando o plano gratuito.

**Configuracao (`render.yaml`):**

- Ambiente: Python 3.13
- Build: `pip install -r requirements.txt`
- Start: `gunicorn main:app --workers 2 --timeout 120`
- Health check: `/`

**URL de producao:** [https://proj-exten.onrender.com](https://proj-exten.onrender.com/)

## Documentacao (GitHub Pages)

A documentacao MkDocs e publicada automaticamente via GitHub Actions.

O workflow `.github/workflows/docs.yml` e acionado a cada push na branch `main`:

1. Instala Python 3.11 e as dependencias (`mkdocs`, `mkdocs-material`)
2. Executa `mkdocs build` para gerar o site estatico
3. Faz upload e deploy no GitHub Pages

**URL da documentacao:** [https://alliciarocha.github.io/proj-exten/](https://alliciarocha.github.io/proj-exten/)

## Links

- **Repositorio:** [https://github.com/alliciarocha/proj-exten](https://github.com/alliciarocha/proj-exten)
- **Aplicacao:** [https://proj-exten.onrender.com](https://proj-exten.onrender.com/)
- **Documentacao:** [https://alliciarocha.github.io/proj-exten/](https://alliciarocha.github.io/proj-exten/)
