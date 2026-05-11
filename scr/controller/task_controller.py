"""
Controller: Gerenciador de Tarefas (Todo List)

Blueprint Flask com endpoints REST para CRUD de tarefas.
Comunica-se com o TaskStore (Model) e retorna JSON.
"""

from flask import Blueprint, jsonify, request

from scr.model.task_model import TaskStore

api = Blueprint("api", __name__, url_prefix="/api/tasks")

store = TaskStore()


@api.route("", methods=["GET"])
def list_tasks():
    """
    GET /api/tasks?filter=all|pending|done

    Retorna lista de tarefas filtrada.
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
    Body JSON: { title, description?, reminder? }

    Cria uma nova tarefa.
    """
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    description = data.get("description", "")
    reminder = data.get("reminder")

    if not title:
        return jsonify({"error": "O título da tarefa não pode ser vazio."}), 400

    try:
        task = store.add(title, description, reminder)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(task.to_dict()), 201


@api.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    DELETE /api/tasks/<id>

    Remove uma tarefa pelo ID.
    """
    removed = store.remove(task_id)
    if not removed:
        return jsonify({"error": "Tarefa não encontrada."}), 404
    return "", 204


@api.route("/<int:task_id>/toggle", methods=["PATCH"])
def toggle_task(task_id):
    """
    PATCH /api/tasks/<id>/toggle

    Alterna o status done/undone de uma tarefa.
    """
    task = store.toggle(task_id)
    if task is None:
        return jsonify({"error": "Tarefa não encontrada."}), 404
    return jsonify(task.to_dict())

@api.route("/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    """
    PUT /api/tasks/<id>
    Body JSON: { title, description?, reminder? }

    Atualiza título, descrição e lembrete de uma tarefa.
    """
    data = request.get_json(silent=True) or {}
    title = data.get("title", "").strip()
    description = data.get("description", "")
    reminder = data.get("reminder")

    if not title:
        return jsonify({"error": "O título da tarefa não pode ser vazio."}), 400

    try:
        task = store.edit(task_id, title, description, reminder)
        if task is None:
            return jsonify({"error": "Tarefa não encontrada."}), 404
        return jsonify(task.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
