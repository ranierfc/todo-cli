class ToDoList:
    def __init__(self):
        self.__tasks = []
    
    @property
    def tasks(self) -> list:
        return self.__tasks
    
    def add_task(self, task: str) -> None:
        self.__tasks.append({"task": task, "completed": False})
        