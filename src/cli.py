import argparse
from todo import ToDoList


def main():
    todo = ToDoList()
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument("--add", help="Adicionar uma tarefa")
    parser.add_argument("--remove", type=int, help="Remover uma tarefa pelo índice")
    parser.add_argument("--list", action="store_true", help="Listar todas as tarefas")
    args = parser.parse_args()

    if args.add:
        todo.add_task(args.add)
        print(f"Tarefa adicionada: {args.add}")

    if args.remove is not None:
        success = todo.remove_task(args.remove)
        print("✅ Tarefa removida!" if success else "❌ Índice inválido!")

    if args.list:
        tasks = todo.tasks
        if tasks:
            for idx, task in enumerate(tasks):
                status = "✔️" if task["completed"] else " "
                print(f"{idx}. [{status}] {task['task']}")
        else:
            print("Nenhuma tarefa encontrada!")


if __name__ == "__main__":
    main()
