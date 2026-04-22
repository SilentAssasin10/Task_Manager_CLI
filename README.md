# Task Tracker CLI (Python)
https://roadmap.sh/projects/task-tracker

A command-line task management application built using Python.
It allows users to create, update, delete, and track tasks directly from the terminal, with persistent storage using a JSON file.

---

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as **todo**, **in-progress**, or **done**
* List all tasks
* Filter tasks by status
* Automatic ID generation
* Timestamp tracking (`createdAt`, `updatedAt`)
* No external libraries used

---

## Project Structure

```
task-tracker/
├── task_cli.py
└── tasks.json   (auto-created on first task)
```

---

## Requirements

* Python 3.x
* Standard library only (no external dependencies)

---

## How It Works

The application follows this flow:

```
CLI Input → Parse Command → Load JSON → Modify Data → Save JSON → Output
```

### Key Modules Used

* `sys` → read command-line arguments
* `json` → store and retrieve tasks
* `os` → check file existence
* `datetime` → generate timestamps

---

## Task Data Format

Each task is stored as a dictionary inside a list:

```json
{
    "id": 1,
    "description": "Study Python",
    "status": "todo",
    "createdAt": "2026-04-22T19:00:00",
    "updatedAt": "2026-04-22T19:00:00"
}
```

---

## Usage

Run commands using:

```
python task_cli.py <command> [arguments]
```

---

## Available Commands

### 1. Add a Task

```
python task_cli.py add "Task description"
```

Example:

```
python task_cli.py add "Study Python"
```

---

### 2. List All Tasks

```
python task_cli.py list
```

---

### 3. List Tasks by Status

```
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

---

### 4. Update a Task

```
python task_cli.py update <id> "New description"
```

Example:

```
python task_cli.py update 1 "Study Python deeply"
```

---

### 5. Delete a Task

```
python task_cli.py delete <id>
```

Example:

```
python task_cli.py delete 1
```

---

### 6. Mark Task as In Progress

```
python task_cli.py mark-in-progress <id>
```

---

### 7. Mark Task as Done

```
python task_cli.py mark-done <id>
```

---

## Core Functions

| Function                       | Purpose                              |
| ------------------------------ | ------------------------------------ |
| `load_tasks()`                 | Reads tasks from JSON file           |
| `save_tasks(tasks)`            | Writes tasks to JSON file            |
| `add_task(description)`        | Adds a new task                      |
| `list_tasks(filter_status)`    | Displays tasks (optionally filtered) |
| `update_task(id, description)` | Updates task description             |
| `delete_task(id)`              | Deletes a task                       |
| `update_status(id, status)`    | Changes task status                  |
| `find_task(tasks, id)`         | Finds a task by ID                   |

---

## Error Handling

* Handles missing JSON file safely
* Prevents crashes on invalid inputs
* Checks for missing arguments
* Validates task existence before update/delete

---

## Future Improvements

* Task priorities (high/medium/low)
* Deadlines and reminders
* Sorting (by date or status)
* Export tasks to CSV
* GUI version

---

## Learning Outcomes

This project demonstrates:

* CLI-based application design
* File handling in Python
* JSON data manipulation
* Program structuring and modular functions
* Error handling and input validation

---

## Author

Arkapravo Roy
