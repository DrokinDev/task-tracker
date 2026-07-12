# Task Tracker CLI

A command-line tool to manage your tasks.

## Setup
Ensure Python 3 is installed.

## Commands

### 1. Add a task
```bash
python3 task_cli.py add "Buy groceries"
```

### 2. Update a task description
```bash
python3 task_cli.py update <ID> "New description"
```

### 3. Delete a task
```bash
python3 task_cli.py delete <ID>
```

### 4. Change task status
```bash
python3 task_cli.py mark-in-progress <ID>
python3 task_cli.py mark-done <ID>
```

### 5. List tasks
List all tasks:
```bash
python3 task_cli.py list
```
List by status (`todo`, `in-progress`, `done`):
```bash
python3 task_cli.py list <status>
```

