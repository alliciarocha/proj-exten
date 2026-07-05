# 🚀 Produção

Este projeto já está preparado para ser publicado em ambientes de produção com Gunicorn.

## Configuração de Produção

- O ponto de entrada da aplicação é o arquivo main.py.
- O servidor web é iniciado com Gunicorn via render.yaml ou Procfile.
- A aplicação responde na rota principal e fornece os arquivos estáticos necessários.

## Deploy no Render

1. Conecte o repositório ao Render.
2. Selecione o serviço web com o arquivo render.yaml.
3. O build instalará as dependências a partir de requirements.txt.
4. O start command executará o Gunicorn para servir a aplicação.

## Checklist de Produção

- Dependências instaladas corretamente.
- Variáveis de ambiente definidas quando necessário.
- Health check configurado para a rota principal.
- Documentação publicada automaticamente via GitHub Pages.
