# 🧪 Estratégia e Guia de Testes

Garantir a integridade da arquitetura MVC e o funcionamento impecável da API REST exige uma abordagem de testes rigorosa e automatizada.

---

## 📐 Níveis de Teste

A estratégia do **Todo List** divide-se em 3 categorias primárias:
1. **Testes Unitários (Model)**: Validação isolada da dataclass `Task` e das regras de negócio do Singleton `TaskStore`.
2. **Testes de Integração (Controller)**: Testes de endpoints HTTP via cliente de teste simulado (*test client*) do Flask.
3. **Testes Fim a Fim (E2E)**: Simulação de fluxos reais do usuário no navegador interagindo com o DOM e a API.

---

## 🐍 Implementando Testes Unitários em Python (`unittest` / `pytest`)

O Flask e o Python oferecem ferramentas robustas para testar o backend. Veja um exemplo de suíte de testes unitários para o Model e Controller:

```python
import unittest
from scr.model.task_model import TaskStore, Task
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
        with self.assertRaises(ValueError):
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
```

### Como Executar os Testes
No seu terminal, com o ambiente virtual ativo, execute:
```bash
python -m unittest
```
Ou, se preferir utilizar o `pytest`:
```bash
pip install pytest
pytest
```

---

## 🌐 Testes de Interface e E2E (Simulação Manual ou Cypress)

Para testar o fluxo completo da aplicação (Frontend + Backend):
1. **Cadastro**: Insira dados nos campos de input e clique em **`+`**. Verifique se a requisição de rede (`Network tab` do navegador) retorna status `201 Created` e se o card é adicionado na tela.
2. **Conclusão**: Clique no checkbox circular. Verifique se a requisição PATCH para `/api/tasks/<id>/toggle` retorna `200 OK` e se os contadores na barra lateral atualizam instantaneamente.
3. **Filtros**: Cadastre 2 tarefas concluídas e 1 pendente. Alterne entre as abas e valide se a renderização em tela filtra perfeitamente os elementos.
