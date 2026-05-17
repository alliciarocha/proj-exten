"""
Controller: Gerenciador de Tarefas (Todo List)

Blueprint Flask com endpoints REST para CRUD de tarefas.
Implementa tratamento de exceções global e respostas JSON limpas.
"""

from flask import Blueprint, jsonify, request

from scr.model.task_model import EntityNotFoundError, TaskStore, ValidationError

api = Blueprint("api", __name__, url_prefix="/api/tasks")

store = TaskStore()


# ---------- Global Exception Handlers ----------

@api.errorhandler(ValidationError)
def handle_validation_error(e):
    return jsonify({"error": str(e)}), 400


@api.errorhandler(EntityNotFoundError)
def handle_entity_not_found_error(e):
    return jsonify({"error": str(e)}), 404


@api.errorhandler(Exception)
def handle_general_error(e):
    # Protege detalhes internos em produção, retornando mensagem padronizada
    if isinstance(e, (ValidationError, EntityNotFoundError)):
        raise e
    return jsonify({"error": "Ocorreu um erro interno no servidor."}), 500


# ---------- Endpoints RESTful ----------

@api.route("", methods=["GET"])
def list_tasks():
    """
    GET /api/tasks?filter=all|pending|done
    Retorna tarefas ativas (filtrando soft deleted).
    """
    filter_type = request.args.get("filter", "all")
    tasks = store.get_by_filter(filter_type)
    return jsonify({
        "tasks": [t.to_dict() for t in tasks],
        "count_done": store.count_done,
        "count_pending": store.count_pending,
    })


@api.route("", methods=["POST"])
def create_task():
    """
    POST /api/tasks
    Cria nova tarefa com validação estrita.
    """
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    description = data.get("description", "")
    reminder = data.get("reminder")

    task = store.add(title, description, reminder)
    return jsonify(task.to_dict()), 201


@api.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    DELETE /api/tasks/<id>
    Executa exclusão lógica (Soft Delete).
    """
    store.remove(task_id)
    return "", 204


@api.route("/<int:task_id>/toggle", methods=["PATCH"])
def toggle_task(task_id):
    """
    PATCH /api/tasks/<id>/toggle
    Alterna status de conclusão.
    """
    task = store.toggle(task_id)
    return jsonify(task.to_dict())


@api.route("/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    """
    PUT /api/tasks/<id>
    Atualiza dados de uma tarefa existente.
    """
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    description = data.get("description", "")
    reminder = data.get("reminder")

    task = store.edit(task_id, title, description, reminder)
    return jsonify(task.to_dict())
