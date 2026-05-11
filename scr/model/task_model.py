"""
Model: Gerenciador de Tarefas (Todo List)

Define a estrutura de dados Task e o armazenamento em memória (TaskStore).
Segue PEP 8 e a regra de persistência apenas em memória (constitution.md).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    """Representa uma tarefa individual."""

    id: int
    title: str
    description: str = ""
    done: bool = False
    reminder: Optional[datetime] = None
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        """Serializa a tarefa para JSON-friendly dict."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "reminder": (
                self.reminder.isoformat() if self.reminder else None
            ),
            "created_at": self.created_at.isoformat(),
        }


class TaskStore:
    """
    Singleton — armazena tarefas em memória (lista Python).

    Métodos públicos:
        add, remove, toggle, get_all, get_by_filter
    """

    _instance: Optional[TaskStore] = None
    _tasks: list[Task]
    _next_id: int

    def __new__(cls) -> TaskStore:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._tasks = []
            cls._instance._next_id = 1
            
            # Adicionando 4 tarefas iniciais
            cls._instance.add("Estudar Python", "Revisar laços de repetição (Loop).", "2026-05-09T22:59:00")
            cls._instance.add("Finalizar UI do Figma", "Ajustar os últimos espaçamentos da barra lateral.")
            cls._instance.add("Comprar mantimentos", "Ir ao mercado comprar frutas e verduras.")
            cls._instance.add("Responder e-mails", "Limpar a caixa de entrada antes do final do dia.")
            
        return cls._instance

    # ---------- CRUD ----------

    def add(
        self,
        title: str,
        description: str = "",
        reminder: Optional[str] = None,
    ) -> Task:
        """
        Cria e armazena uma nova tarefa.

        Args:
            title: Título da tarefa (obrigatório, não pode ser vazio).
            description: Descrição opcional.
            reminder: Data/hora do lembrete em formato ISO 8601 (opcional).

        Returns:
            A tarefa criada.

        Raises:
            ValueError: Se o título estiver vazio.
        """
        if not title or not title.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")

        parsed_reminder = None
        if reminder:
            try:
                parsed_reminder = datetime.fromisoformat(reminder)
            except (ValueError, TypeError):
                parsed_reminder = None

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip(),
            reminder=parsed_reminder,
        )
        self._tasks.append(task)
        self._next_id += 1
        return task

    def remove(self, task_id: int) -> bool:
        """
        Remove uma tarefa pelo ID.

        Returns:
            True se removida, False se não encontrada.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                return True
        return False

    def toggle(self, task_id: int) -> Optional[Task]:
        """
        Alterna o status done/undone de uma tarefa.

        Returns:
            A tarefa atualizada ou None se não encontrada.
        """
        for task in self._tasks:
            if task.id == task_id:
                task.done = not task.done
                return task
        return None

    def edit(self, task_id: int, title: str, description: str = "", reminder: Optional[str] = None) -> Optional[Task]:
        """
        Atualiza o título, descrição e lembrete de uma tarefa existente.
        """
        if not title or not title.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")
        
        parsed_reminder = None
        if reminder:
            try:
                parsed_reminder = datetime.fromisoformat(reminder)
            except (ValueError, TypeError):
                parsed_reminder = None
        
        for task in self._tasks:
            if task.id == task_id:
                task.title = title.strip()
                task.description = description.strip()
                task.reminder = parsed_reminder
                return task
        return None

    def get_all(self) -> list[Task]:
        """Retorna todas as tarefas (ordenadas por criação)."""
        return list(self._tasks)

    def get_by_filter(self, filter_type: str = "all") -> list[Task]:
        """
        Filtra tarefas pelo status.

        Args:
            filter_type: 'all', 'pending' ou 'done'.

        Returns:
            Lista filtrada de tarefas.
        """
        if filter_type == "pending":
            return [t for t in self._tasks if not t.done]
        elif filter_type == "done":
            return [t for t in self._tasks if t.done]
        return self.get_all()

    @property
    def count_done(self) -> int:
        """Quantidade de tarefas concluídas."""
        return sum(1 for t in self._tasks if t.done)

    @property
    def count_pending(self) -> int:
        """Quantidade de tarefas pendentes."""
        return sum(1 for t in self._tasks if not t.done)

    def clear(self) -> None:
        """Remove todas as tarefas (útil para testes)."""
        self._tasks.clear()
        self._next_id = 1
