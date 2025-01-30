import json
import os
from datetime import datetime
from enum import Enum


class Priority(Enum):
    HIGH = "alta"
    MEDIUM = "media"
    LOW = "baixa"


class ToDoList:
    def __init__(self, file_path: str = "todos.json"):
        self.__file_path = file_path
        self.__tasks = self.__load_tasks()

    @property
    def file_path(self) -> str:
        return self.__file_path

    @property
    def tasks(self) -> list:
        return self.__tasks

    def __load_tasks(self) -> list:
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                tasks = json.load(f)
                # Garantir retrocompatibilidade para tarefas antigas sem prioridade
                for task in tasks:
                    if "priority" not in task:
                        task["priority"] = Priority.LOW.value
                return tasks
        return []

    def __save_tasks(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task: str, priority: Priority = Priority.LOW) -> None:
        self.tasks.append(
            {
                "task": task,
                "priority": priority.value,
                "completed": False,
                "created_at": datetime.now().isoformat(),
                "completed_at": None,
            }
        )
        self.__save_tasks()

    def list_tasks(self, filter_status: str = "all") -> list:
        return [
            task
            for task in self.tasks
            if (filter_status == "completed" and task["completed"])
            or (filter_status == "pending" and not task["completed"])
            or filter_status == "all"
        ]

    def remove_task(self, index: int) -> bool:
        try:
            del self.tasks[index]
            self.__save_tasks()
            return True
        except IndexError:
            return False

    def mark_as_completed(self, index: int) -> bool:
        try:
            self.tasks[index]["completed"] = True
            self.tasks[index]["completed_at"] = datetime.now().isoformat()
            self.__save_tasks()
            return True
        except IndexError:
            return False
