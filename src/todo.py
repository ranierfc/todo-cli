import json
import os


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
                return json.load(f)
        return []

    def __save_tasks(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task: str) -> None:
        self.tasks.append({"task": task, "completed": False})
        self.__save_tasks()

    def remove_task(self, index: int) -> bool:
        try:
            del self.tasks[index]
            self.__save_tasks()
            return True
        except IndexError:
            return False
