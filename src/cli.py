import argparse
from todo import ToDoList


def main():
    todo = ToDoList()
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument("--add", help="Adicionar uma tarefa")
    args = parser.parse_args()

    if args.add:
        todo.add_task(args.add)
        print(f"Tarefa adicionada: {args.add}")


if __name__ == "__main__":
    main()
