"""Command-line interface for FocusFlow."""
import argparse
from .core import add_task, complete_task, delete_task, get_stats, load_tasks

def main():
    parser = argparse.ArgumentParser(
        prog="focusflow",
        description="A lightweight task planner for study and personal projects."
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="Add a new task")
    add.add_argument("title", help='Task title, e.g. "Revise Python functions"')

    commands.add_parser("list", help="Show all tasks")

    done = commands.add_parser("done", help="Mark a task as completed")
    done.add_argument("id", type=int)

    remove = commands.add_parser("delete", help="Delete a task")
    remove.add_argument("id", type=int)

    commands.add_parser("stats", help="Show task progress")
    args = parser.parse_args()

    try:
        if args.command == "add":
            task = add_task(args.title)
            print(f'Added task #{task["id"]}: {task["title"]}')
        elif args.command == "list":
            tasks = load_tasks()
            if not tasks:
                print("No tasks yet. Add one with: python focusflow.py add \"Your task\"")
            for task in tasks:
                mark = "x" if task["done"] else " "
                print(f'[{mark}] #{task["id"]} {task["title"]}')
        elif args.command == "done":
            task = complete_task(args.id)
            print(f'Marked as completed: {task["title"]}')
        elif args.command == "delete":
            delete_task(args.id)
            print(f"Deleted task #{args.id}.")
        elif args.command == "stats":
            stats = get_stats()
            print(f'Total: {stats["total"]} | Completed: {stats["completed"]} | Pending: {stats["pending"]}')
    except ValueError as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()
