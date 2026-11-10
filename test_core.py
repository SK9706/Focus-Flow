import json
import pytest
from focusflow.core import add_task, complete_task, delete_task, get_stats, load_tasks

def test_add_and_load_task(tmp_path):
    db = tmp_path / "tasks.json"
    task = add_task("Learn Python", db)
    assert task["id"] == 1
    assert load_tasks(db)[0]["title"] == "Learn Python"

def test_complete_task(tmp_path):
    db = tmp_path / "tasks.json"
    add_task("Build a project", db)
    assert complete_task(1, db)["done"] is True

def test_delete_task(tmp_path):
    db = tmp_path / "tasks.json"
    add_task("Temporary task", db)
    delete_task(1, db)
    assert load_tasks(db) == []

def test_stats(tmp_path):
    db = tmp_path / "tasks.json"
    add_task("One", db)
    add_task("Two", db)
    complete_task(1, db)
    assert get_stats(db) == {"total": 2, "completed": 1, "pending": 1}

def test_empty_title_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        add_task("   ", tmp_path / "tasks.json")
