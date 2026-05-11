"""
Main — Gerenciador de Tarefas (Todo List)

Ponto de entrada da aplicação Flask.
Serve a interface estática e registra o blueprint da API REST.
"""

import os

from flask import Flask, send_from_directory

from scr.controller.task_controller import api

app = Flask(__name__, static_folder=None)

# Caminho absoluto para a pasta de arquivos da View
VIEW_DIR = os.path.join(os.path.dirname(__file__), "scr", "view")


@app.route("/")
def index():
    """Serve a página principal (index.html)."""
    return send_from_directory(VIEW_DIR, "index.html")


@app.route("/static/<path:filename>")
def serve_static(filename):
    """Serve arquivos estáticos (CSS, JS) da pasta view."""
    return send_from_directory(VIEW_DIR, filename)


# Registra o blueprint da API
app.register_blueprint(api)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
