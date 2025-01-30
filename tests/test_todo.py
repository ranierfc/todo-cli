import pytest
from src.todo import ToDoList


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
