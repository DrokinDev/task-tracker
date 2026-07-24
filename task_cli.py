import json
import sys
from datetime import datetime
from pathlib import Path


def add(tasks, task_description):
    if task_description is not None:
        task = createTask(len(tasks),task_description)
        tasks.append(task)
        print(f'Task added sucessfully (ID:{task["id"]})')
    else:
        print("Incorrect argument")

def update(tasks,task_id, task_description):
    try:
        task_id = int(task_id)
    except (ValueError,TypeError):
        print("Incorrect argument")
        return

    if (0 > task_id) or (task_id >= len(tasks)):
        print("Id out of bounds")
        return

    if (task_description is None) or (task_id is None):
        print("Incorrect argument")
    else:
        task_id = int(task_id)
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = task_description
                task["updatedAt"] = str(datetime.now())
                print(f'Task updated sucessfully (ID:{task["id"]})')
                return


def delete(tasks,task_id):
    try:
        task_id = int(task_id)
    except (ValueError,TypeError):
        print("Incorrect argument")
        return

    if (0 > task_id) or (task_id >= len(tasks)):
        print("Id out of bounds")
        return

    for task in tasks[task_id + 1:]:
        task["id"] -=1

    del tasks[task_id]
    print(f'Task deleted sucessfully (ID:{task_id})')

def mark_in_progress(tasks,task_id):
    try:
        task_id = int(task_id)
    except (ValueError,TypeError):
        print("Incorrect argument")
        return

    if (0 > task_id) or (task_id >= len(tasks)):
        print("Id out of bounds")
        return

    if task_id is None:
        print("Incorrect argument")
    else:
        task_id = int(task_id)
        tasks[task_id]["status"] = "in-progress"
        tasks[task_id]["updatedAt"] = str(datetime.now())
        print(f'Task marked sucessfully (ID:{task_id})')

def mark_done(tasks,task_id):
    try:
        task_id = int(task_id)
    except (ValueError,TypeError):
        print("Incorrect argument")
        return

    if (0 > task_id) or (task_id >= len(tasks)):
        print("Id out of bounds")
        return

    if task_id is None:
        print("Incorrect argument")
    else:
        task_id = int(task_id)
        tasks[task_id]["status"] = "done"
        tasks[task_id]["updatedAt"] = str(datetime.now())
        print(f'Task marked sucessfully (ID:{task_id})')

def list_tasks(tasks,filter=None):
    if filter is None:
        for task in tasks:
            print(f'ID: {task["id"]} Description: {task["description"]} Status: {task["status"]} Created: {task["createdAt"]} Last Update: {task["updatedAt"]}')
    elif filter in ["done","todo","in-progress"]:
        for task in tasks:
            if task["status"] == filter:
                print(f'ID: {task["id"]} Description: {task["description"]} Status: {task["status"]} Created: {task["createdAt"]} Last Update: {task["updatedAt"]}')
    else:
        print("Wrong filter")

def createTask(task_id, description):
    time = str(datetime.now())
    return {
        "id":task_id,
        "description": description,
        "status": "todo",
        "createdAt": time,
        "updatedAt": time
    }

def main():

    #Edge case or case
    if not Path("tasks.json").exists():
        with open("tasks.json", "w") as f:
            json.dump([] ,f)

    with open("tasks.json", "r") as f:
            tasks = json.load(f)

    value = sys.argv[2] if len(sys.argv) > 2 else None

    if len(sys.argv) > 1:
        match sys.argv[1]:
            case "add":
                add(tasks, value)
            case "update":
                value2 = sys.argv[3] if len(sys.argv) > 3 else None
                update(tasks,value,value2)
            case "delete":
                delete(tasks,value)
            case "mark-in-progress":
                mark_in_progress(tasks,value)
            case "mark-done":
                mark_done(tasks, value)
            case "list":
                list_tasks(tasks, value)


    with open("tasks.json","w") as f:
        json.dump(tasks,f)

if __name__ == "__main__":
    main()
