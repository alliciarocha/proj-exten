import unittest
from scr.model.task_model import TaskStore, Task, ValidationError
from main import app

class TodoAppTestCase(unittest.TestCase):
    def setUp(self):
        """Configuração inicial antes de cada teste."""
        self.app = app.test_client()
        self.store = TaskStore()
        self.store.clear() # Limpa o singleton para iniciar limpo

    def test_create_task_model(self):
        """Testa a criação de uma tarefa diretamente no Model."""
        task = self.store.add("Comprar pão", "Pão francês quentinho")
        self.assertEqual(task.title, "Comprar pão")
        self.assertEqual(self.store.count_pending, 1)

    def test_create_task_empty_title_raises(self):
        """Garante que título vazio lança exceção."""
        with self.assertRaises(ValidationError):
            self.store.add("")

    def test_api_list_tasks(self):
        """Testa o endpoint GET /api/tasks via HTTP."""
        self.store.add("Tarefa API 1")
        response = self.app.get("/api/tasks")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data["tasks"]), 1)
        self.assertEqual(data["tasks"][0]["title"], "Tarefa API 1")

if __name__ == "__main__":
    unittest.main()
