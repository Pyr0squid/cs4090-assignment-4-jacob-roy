import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import tasks


@pytest.fixture
def sample_tasks():
  return [
    {"id": 1, "priority": "High", "category":"School", "completed": True, "title": "Buy groceries", "description": "Milk, Eggs, Bread", "due_date": "2025-04-10"},
    {"id": 2, "priority": "Medium", "category": "Work", "completed": False, "title": "Workout", "description": "Leg day at the gym", "due_date": "2025-04-10"},
    {"id": 3, "priority": "High", "category": "Work", "completed": False, "title": "Read", "description": "Finish that fantasy novel", "due_date": "2025-05-10"}
  ]


@pytest.mark.parametrize("task_list, expected_id", [
  ([], 1),
  ([{"id": 1}, {"id": 2}], 3),
  ([{"id": 5}, {"id": 10}], 11)
])
def test_generate_unique_id(task_list, expected_id):
  assert tasks.generate_unique_id(task_list) == expected_id
  

@pytest.mark.parametrize("priority, expected_count", [
  ("High", 2),
  ("Medium", 1),
  ("Low", 0)
])
def test_filter_tasks_by_priority(sample_tasks, priority, expected_count):
  result = tasks.filter_tasks_by_priority(sample_tasks, priority)
  assert len(result) == expected_count
  assert all(task["priority"] == priority for task in result)


@pytest.mark.parametrize("query, expected_ids", [
  ("gym", [2]),
  ("novel", [3]),
  ("milk", [1]),
  ("xyz", [])
])
def test_search_tasks(sample_tasks, query, expected_ids):
  result = tasks.search_tasks(sample_tasks, query)
  result_ids = [task["id"] for task in result]
  assert result_ids == expected_ids
