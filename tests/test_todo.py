import pytest
from src.todo import ToDoList, Priority


@pytest.fixture
def todo(tmp_path):
    file_path = tmp_path / "test_todos.json"
    return ToDoList(file_path)


def test_mark_as_completed(todo: ToDoList):
    todo.add_task("Tarefa para concluir")
    assert todo.mark_as_completed(0) is True
    assert todo.tasks[0]["completed"] is True


def test_list_tasks(todo: ToDoList):
    todo.add_task("Tarefa 1")
    todo.add_task("Tarefa 2")
    todo.mark_as_completed(0)

    # Testar filtro 'completed'
    completed_tasks = todo.list_tasks(filter_status="completed")
    assert len(completed_tasks) == 1
    assert completed_tasks[0]["task"] == "Tarefa 1"

    # Testar filtro 'pending'
    pending_tasks = todo.list_tasks(filter_status="pending")
    assert len(pending_tasks) == 1
    assert pending_tasks[0]["task"] == "Tarefa 2"


def test_task_creation_date(todo):
    todo.add_task("Tarefa com data")
    assert "created_at" in todo.tasks[0]
    assert isinstance(todo.tasks[0]["created_at"], str)


def test_task_completion_date(todo):
    todo.add_task("Tarefa para concluir")
    todo.mark_as_completed(0)
    assert "completed_at" in todo.tasks[0]
    assert isinstance(todo.tasks[0]["completed_at"], str)


def test_task_priority(todo):
    todo.add_task("Tarefa sem prioridade")
    assert todo.tasks[0]["priority"] == Priority.LOW.value

    todo.add_task("Tarefa urgente", Priority.HIGH)
    assert todo.tasks[1]["priority"] == Priority.HIGH.value


def test_filter_by_priority(todo):
    todo.add_task("Tarefa 1", Priority.HIGH)
    todo.add_task("Tarefa 2", Priority.MEDIUM)

    high_priority_tasks = todo.list_tasks()
    high_priority_tasks = [
        t for t in high_priority_tasks if t["priority"] == Priority.HIGH.value
    ]

    assert len(high_priority_tasks) == 1
    assert high_priority_tasks[0]["task"] == "Tarefa 1"


def test_remove_task_with_filters(todo):
    todo.add_task("Tarefa Alta", Priority.HIGH)
    todo.add_task("Tarefa Baixa", Priority.LOW)

    filtered_tasks = [
        task for task in todo.tasks if task["priority"] == Priority.LOW.value
    ]
    real_indices = [
        idx for idx, task in enumerate(todo.tasks) if task in filtered_tasks
    ]

    assert todo.remove_task(real_indices[0]) is True
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["priority"] == Priority.HIGH.value
