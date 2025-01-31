import argparse
from datetime import datetime
from todo import ToDoList, Priority


def main():
    todo = ToDoList()
    parser = argparse.ArgumentParser(description="To-Do List CLI")
    parser.add_argument("--add", help="Adicionar uma tarefa")
    parser.add_argument("--remove", type=int, help="Remover uma tarefa pelo índice")
    parser.add_argument("--list", action="store_true", help="Listar todas as tarefas")
    parser.add_argument(
        "--filter",
        choices=["all", "completed", "pending"],
        default="all",
        help="Filtrar tarefas por status",
    )
    parser.add_argument(
        "--complete", type=int, help="Marcar tarefa como concluída pelo índice"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Mostrar detalhes completos das tarefas"
    )
    parser.add_argument(
        "--created-before",
        help="Filtrar tarefas criadas antes de uma data (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--completed-after",
        help="Filtrar tarefas concluídas após uma data (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--priority",
        choices=["alta", "media", "baixa"],
        default="baixa",
        help="Definir prioridade de tarefa (alta/media/baixa)",
    )
    parser.add_argument(
        "--filter-priority",
        choices=["alta", "media", "baixa"],
        help="Filtrar tarefas por prioridade",
    )
    args = parser.parse_args()

    if args.add:
        priority = Priority(args.priority)
        todo.add_task(args.add, priority)
        print(f"Tarefa adicionada: ({priority.value}): {args.add}")

    if args.remove is not None:
        success = todo.remove_task(args.remove)
        print("✅ Tarefa removida!" if success else "❌ Índice inválido!")

    if args.list:
        tasks = todo.list_tasks(args.filter)

        if args.filter_priority:
            tasks = [t for t in tasks if t["priority"] == args.filter_priority]

        if args.created_before:
            tasks = [
                t
                for t in tasks
                if datetime.fromisoformat(t["created_at"])
                < datetime.strptime(args.created_before, "%Y-%m-%d")
            ]

        if args.completed_after:
            tasks = [
                t
                for t in tasks
                if t["completed"]
                and datetime.fromisoformat(t["completed_at"])
                > datetime.strptime(args.completed_after, "%Y-%m-%d")
            ]

        real_indexes = [idx for idx, task in enumerate(todo.tasks) if task in tasks]
        if tasks:
            for display_idx, (real_indexes, task) in enumerate(
                zip(real_indexes, tasks)
            ):
                status = "X" if task["completed"] else " "
                priority = f"[{task['priority'].upper()}]" if "priority" in task else ""
                created = datetime.fromisoformat(task["created_at"]).strftime(
                    "%d/%m/%Y %H:%M"
                )
                completed = (
                    datetime.fromisoformat(task["completed_at"]).strftime(
                        "%d/%m/%Y %H:%M"
                    )
                    if task["completed_at"]
                    else "N/A"
                )

                if args.verbose:
                    print(
                        f"Índice Real: {real_indexes} | Tarefa {display_idx}: {priority} [{status}] {task['task']}"
                    )
                    print(f"\tCriada em: {created}")
                    print(f"\tConcluída em: {completed}\n")
                else:
                    print(f"{real_indexes}. {priority} [{status}] {task['task']}")
        else:
            print("Nenhuma tarefa encontrada!")

    if args.complete is not None:
        success = todo.mark_as_completed(args.complete)
        print("✅ Tarefa concluída!" if success else "❌ Índice inválido!")


if __name__ == "__main__":
    main()
