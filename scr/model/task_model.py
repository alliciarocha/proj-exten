"""
Model: Gerenciador de Tarefas (Todo List)

Implementa os padrões avançados de arquitetura e boas práticas da indústria:
- DTOs via @dataclass
- Exclusão Lógica (Soft Delete)
- Metadados de Auditoria (created_at, updated_at, deleted_at)
- Estratégia Serverless (Persistência em arquivo JSON)
- Exceções Padronizadas de Negócio
- Sanitização contra XSS e limitação de tamanho (OWASP)
- Observabilidade via Logs Estruturados de Transação
"""

from __future__ import annotations

import html
import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

# Configuração de Observabilidade (Logging Estruturado)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] (%(name)s) %(message)s")
logger = logging.getLogger("TaskModel")


class EntityNotFoundError(Exception):
    """Exceção levantada quando uma entidade solicitada não existe."""
    pass


class ValidationError(Exception):
    """Exceção levantada para falhas de validação nos dados de entrada."""
    pass


@dataclass
class Task:
    """Representa uma tarefa individual com metadados de auditoria e DTO."""

    id: int
    title: str
    description: str = ""
    done: bool = False
    reminder: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        """Serializa a entidade para JSON-friendly DTO."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "reminder": self.reminder.isoformat() if self.reminder else None,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Task:
        """Deserializa um DTO JSON para a entidade Task."""
        reminder = None
        if data.get("reminder"):
            try:
                reminder = datetime.fromisoformat(data["reminder"])
            except (ValueError, TypeError):
                reminder = None

        created_at = datetime.now()
        if data.get("created_at"):
            try:
                created_at = datetime.fromisoformat(data["created_at"])
            except (ValueError, TypeError):
                pass

        updated_at = datetime.now()
        if data.get("updated_at"):
            try:
                updated_at = datetime.fromisoformat(data["updated_at"])
            except (ValueError, TypeError):
                pass

        deleted_at = None
        if data.get("deleted_at"):
            try:
                deleted_at = datetime.fromisoformat(data["deleted_at"])
            except (ValueError, TypeError):
                pass

        return cls(
            id=int(data["id"]),
            title=data["title"],
            description=data.get("description", ""),
            done=bool(data.get("done", False)),
            reminder=reminder,
            created_at=created_at,
            updated_at=updated_at,
            deleted_at=deleted_at,
        )


class TaskStore:
    """
    Singleton & Repository Interface — gerencia persistência JSON, exclusão lógica,
    sanitização e logs transacionais.
    """

    _instance: Optional[TaskStore] = None
    _tasks: list[Task]
    _next_id: int
    _storage_path: str = os.path.join(os.path.dirname(__file__), "storage.json")

    def __new__(cls) -> TaskStore:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._tasks = []
            cls._instance._next_id = 1
            cls._instance._load()
            logger.info("TaskStore Singleton inicializado com sucesso.")
        return cls._instance

    def _load(self) -> None:
        """Carrega tarefas do arquivo JSON estático de persistência."""
        if os.path.exists(self._storage_path):
            try:
                with open(self._storage_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self._tasks = [Task.from_dict(item) for item in data.get("tasks", [])]
                    self._next_id = data.get("next_id", 1)
                logger.info(f"Persistência carregada: {len(self._tasks)} tarefas ativas.")
                return
            except (json.JSONDecodeError, IOError, KeyError) as e:
                logger.warning(f"Falha ao ler storage.json ({e}). Recriando persistência padrão.")

        # Se não existir ou falhar, inicializa com dados padrão e salva
        self._tasks = []
        self._next_id = 1
        self.add("Estudar Python", "Revisar laços de repetição (Loop).", "2026-05-09T22:59:00")
        self.add("Finalizar UI do Figma", "Ajustar os últimos espaçamentos da barra lateral.")
        self.add("Comprar mantimentos", "Ir ao mercado comprar frutas e verduras.")
        self.add("Responder e-mails", "Limpar a caixa de entrada antes do final do dia.")

    def _save(self) -> None:
        """Salva o estado atual no arquivo JSON de persistência."""
        data = {
            "next_id": self._next_id,
            "tasks": [t.to_dict() for t in self._tasks]
        }
        try:
            with open(self._storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except IOError as e:
            logger.error(f"Erro ao salvar em {self._storage_path}: {e}")

    # ---------- CRUD & Repository Logic ----------

    def add(
        self,
        title: str,
        description: str = "",
        reminder: Optional[str] = None,
    ) -> Task:
        """Adiciona nova tarefa com validação estrita e sanitização."""
        if not title or not title.strip():
            raise ValidationError("O título da tarefa não pode ser vazio.")

        # Sanitização Anti-XSS e limitação de tamanho (OWASP)
        clean_title = html.escape(title.strip())[:120]
        clean_desc = html.escape(description.strip())[:300]

        if not clean_title:
            raise ValidationError("O título da tarefa não pode ser vazio após sanitização.")

        parsed_reminder = None
        if reminder:
            try:
                parsed_reminder = datetime.fromisoformat(reminder)
            except (ValueError, TypeError):
                parsed_reminder = None

        now = datetime.now()
        task = Task(
            id=self._next_id,
            title=clean_title,
            description=clean_desc,
            reminder=parsed_reminder,
            created_at=now,
            updated_at=now,
        )
        self._tasks.append(task)
        self._next_id += 1
        self._save()

        logger.info(f"Transação [ADD]: Tarefa {task.id} ('{task.title[:15]}...') cadastrada.")
        return task

    def remove(self, task_id: int) -> bool:
        """Realiza exclusão lógica (Soft Delete) e log transacional."""
        for task in self._tasks:
            if task.id == task_id and task.deleted_at is None:
                task.deleted_at = datetime.now()
                task.updated_at = datetime.now()
                self._save()
                logger.info(f"Transação [SOFT_DELETE]: Tarefa {task.id} excluída logicamente.")
                return True
        raise EntityNotFoundError(f"Tarefa com ID {task_id} não encontrada ou já excluída.")

    def toggle(self, task_id: int) -> Task:
        """Alterna o status de conclusão da tarefa."""
        for task in self._tasks:
            if task.id == task_id and task.deleted_at is None:
                task.done = not task.done
                task.updated_at = datetime.now()
                self._save()
                logger.info(f"Transação [TOGGLE]: Tarefa {task.id} -> Concluída: {task.done}.")
                return task
        raise EntityNotFoundError(f"Tarefa com ID {task_id} não encontrada.")

    def edit(
        self,
        task_id: int,
        title: str,
        description: str = "",
        reminder: Optional[str] = None,
    ) -> Task:
        """Atualiza metadados da tarefa de forma auditável e segura."""
        if not title or not title.strip():
            raise ValidationError("O título da tarefa não pode ser vazio.")

        clean_title = html.escape(title.strip())[:120]
        clean_desc = html.escape(description.strip())[:300]

        if not clean_title:
            raise ValidationError("O título da tarefa não pode ser vazio após sanitização.")

        parsed_reminder = None
        if reminder:
            try:
                parsed_reminder = datetime.fromisoformat(reminder)
            except (ValueError, TypeError):
                parsed_reminder = None

        for task in self._tasks:
            if task.id == task_id and task.deleted_at is None:
                task.title = clean_title
                task.description = clean_desc
                task.reminder = parsed_reminder
                task.updated_at = datetime.now()
                self._save()
                logger.info(f"Transação [EDIT]: Tarefa {task.id} atualizada com sucesso.")
                return task
        raise EntityNotFoundError(f"Tarefa com ID {task_id} não encontrada.")

    def get_all(self) -> list[Task]:
        """Retorna todas as tarefas ativas (não excluídas logicamente)."""
        return [t for t in self._tasks if t.deleted_at is None]

    def get_by_filter(self, filter_type: str = "all") -> list[Task]:
        """Filtra tarefas ativas pelo status."""
        active = self.get_all()
        if filter_type == "pending":
            return [t for t in active if not t.done]
        elif filter_type == "done":
            return [t for t in active if t.done]
        return active

    @property
    def count_done(self) -> int:
        """Quantidade de tarefas ativas concluídas."""
        return sum(1 for t in self.get_all() if t.done)

    @property
    def count_pending(self) -> int:
        """Quantidade de tarefas ativas pendentes."""
        return sum(1 for t in self.get_all() if not t.done)

    def clear(self) -> None:
        """Limpa as tarefas (útil para testes)."""
        self._tasks.clear()
        self._next_id = 1
        self._save()
        logger.info("Transação [CLEAR]: Repositório resetado.")
