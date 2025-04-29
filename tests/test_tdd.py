import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import tasks

@pytest.fixture
def sample_tasks():
  return [
    {"id": 1, "due_date": "2025-05-10"},
    {"id": 2, "due_date": "2025-05-15"},
    {"id": 3, "due_date": "2025-04-20"}
  ]

# Sort Tasks by Due Date
# Input: List of Tasks
# Ouput: List of Tasks sorted by Date; earliest first
def test_sort_tasks_by_due_date(sample_tasks):
  # test list with tasks
  sorted_task = [
    {"id": 3, "due_date": "2025-04-20"},
    {"id": 1, "due_date": "2025-05-10"},
    {"id": 2, "due_date": "2025-05-15"}
  ]

  result = tasks.sort_tasks_by_due_date(sample_tasks)
  assert result == sorted_task

  # test list without tasks
  result = tasks.sort_tasks_by_due_date([])
  assert result == []


# Duplicate a Task by ID
# Input: List of Tasks, ID of Task to Duplicate
# Output: List of Tasks
def test_duplicate_task(sample_tasks):
  # test id in list
  duplicated_task = [
    {"id": 1, "due_date": "2025-05-10"},
    {"id": 2, "due_date": "2025-05-15"},
    {"id": 3, "due_date": "2025-04-20"},
    {"id": 4, "due_date": "2025-05-10"}
  ]

  result = tasks.duplicate_task(sample_tasks, id=1)
  assert result == duplicated_task

  # test id not in list
  result = tasks.duplicate_task(sample_tasks, id=0)
  assert result == sample_tasks


# Reminder for Task due on day
# Input: List of Tasks, Date to Filter By
# Output: List of IDs of Task due on day
def test_reminder(sample_tasks):
  # test date in list
  assert tasks.reminder(sample_tasks, date="2025-04-20") == [3]

  # test date not in list
  assert tasks.reminder(sample_tasks, date="2024-01-01") == []
