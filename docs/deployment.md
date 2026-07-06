# Implantacao

## Aplicacao (Render)

A aplicacao esta configurada para deploy no Render usando o plano gratuito.

**Configuracao (`render.yaml`):**

- Ambiente: Python 3.13
- Build: `pip install -r requirements.txt`
- Start: `gunicorn main:app --workers 2 --timeout 120`
- Health check: `/`

**URL de producao:** [https://proj-exten.onrender.com](https://proj-exten.onrender.com/)

## Links

- **Repositorio:** [https://github.com/alliciarocha/proj-exten](https://github.com/alliciarocha/proj-exten)
- **Aplicacao:** [https://proj-exten.onrender.com](https://proj-exten.onrender.com/)
- **Documentacao:** [https://alliciarocha.github.io/proj-exten/](https://alliciarocha.github.io/proj-exten/)
