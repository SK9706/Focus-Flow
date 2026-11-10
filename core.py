"""Core task management logic."""
import json
from pathlib import Path
from datetime import datetime

DEFAULT_FILE = Path.home() / ".focusflow_tasks.json"

def load_tasks(path=DEFAULT_FILE):
    path = Path(path)
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

def save_tasks(tasks, path=DEFAULT_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(tasks, indent=2), encoding="utf-8")

def add_task(title, path=DEFAULT_FILE):
    title = title.strip()
    if not title:
        raise ValueError("Task title cannot be empty.")
    tasks = load_tasks(path)
    task = {
        "id": max((item["id"] for item in tasks), default=0) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks, path)
    return task

def complete_task(task_id, path=DEFAULT_FILE):
    tasks = load_tasks(path)
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks, path)
            return task
    raise ValueError(f"No task found with ID {task_id}.")

def delete_task(task_id, path=DEFAULT_FILE):
    tasks = load_tasks(path)
    updated = [task for task in tasks if task["id"] != task_id]
    if len(updated) == len(tasks):
        raise ValueError(f"No task found with ID {task_id}.")
    save_tasks(updated, path)

def get_stats(path=DEFAULT_FILE):
    tasks = load_tasks(path)
    completed = sum(task["done"] for task in tasks)
    total = len(tasks)
    return {"total": total, "completed": completed, "pending": total - completed}
