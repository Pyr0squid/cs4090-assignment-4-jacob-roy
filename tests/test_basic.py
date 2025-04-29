import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import tasks
import tempfile
import json


def test_load_tasks():
  # Test File exist
  task_list = [
    {"id": 1, "priority": "High", "category":"School", "completed": True, "title": "Buy groceries", "description": "Milk, Eggs, Bread", "due_date": "2025-04-10"},
    {"id": 2, "priority": "Medium", "category": "Work", "completed": False, "title": "Workout", "description": "Leg day at the gym", "due_date": "2025-04-10"},
    {"id": 3, "priority": "High", "category": "Work", "completed": False, "title": "Read", "description": "Finish that fantasy novel", "due_date": "2025-05-10"}
  ]
  
  with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
    json.dump(task_list, tmp)
    tmp_path = tmp.name

  assert tasks.load_tasks(tmp_path) == task_list
  os.remove(tmp_path)

  # Test File doesn't exist
  assert tasks.load_tasks("test.json") == []

  # Test Corrupted File
  with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
    tmp.write("{bad json}")
    tmp_path = tmp.name

  assert tasks.load_tasks(tmp_path) == []
  os.remove(tmp_path)


def test_filter_tasks_by_category():
  task_lists = [
    {"id": 1, "category":"School"},
    {"id": 2, "category": "Work"},
    {"id": 3, "category": "Work"}
  ]

  work_category = tasks.filter_tasks_by_category(task_lists, "Work")
  assert len(work_category) == 2
  assert all(task["category"] == "Work" for task in work_category)


def test_filter_tasks_by_completion():
  task_lists = [
    {"id": 1, "completed": True},
    {"id": 2, "completed": False},
    {"id": 3, "completed": False}
  ]

  completed = tasks.filter_tasks_by_completion(task_lists)
  assert len(completed) == 1
  assert all(task["completed"] == True for task in completed)

  not_completed = tasks.filter_tasks_by_completion(task_lists, False)
  assert len(not_completed) == 2
  assert all(task["completed"] == False for task in not_completed)


def test_get_overdue_tasks():
  task_list = [
    {"id": 1, "completed": True, "due_date": "2025-04-10"},
    {"id": 2, "completed": False, "due_date": "2025-04-10"},
    {"id": 3, "completed": False, "due_date": "2025-05-10"}
  ]
  result = tasks.get_overdue_tasks(task_list)
  assert len(result) == 1
  assert result[0]["completed"] == False

