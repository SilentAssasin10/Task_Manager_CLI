import sys
import os
from datetime import datetime
import json

FILE_NAME = 'tasks.json'

# Load tasks

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except:
        return []

# Save tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)


# Add tasks

def add_tasks(description):
    tasks = load_tasks()
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]['id'] + 1

    now = datetime.now().isoformat()

    new_tasks = {
        "id": new_id,
        "description": description,
        "state": "todo",
        "added": now,
        "modified": now
    }

    tasks.append(new_tasks)
    save_tasks(tasks)
    print(f"Task added with {new_id} Task ID")

# Find task 
def find_tasks(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return

# Update command

def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_tasks(tasks, task_id)

    if task:
        task['description'] = new_description
        task['modified'] = datetime.now().isoformat()

    save_tasks(tasks)
    print(f"Task with {task_id} successfully modified")

# Delete task
def delete(task_id):
    tasks = load_tasks()
    new_tasks = []

    task = find_tasks(tasks, task_id)

    if not task:
        print(f"Task {task_id} not found!")

    for i in tasks:
        if i["id"] == task_id:
            continue
        new_tasks.append(i)

    tasks = new_tasks
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully")

# Status update to mark-in-progress & mark-done

def status_update(task_id, status):
    tasks = load_tasks()
    task = find_tasks(tasks, task_id)
    if task:
        task["state"] = status
        task["modified"] = datetime.now().isoformat()
    else:
        print(f"Task {task_id} not found")

    save_tasks(tasks)
    print(f"Task {task_id} status changed successfully")


# List tasks

def list_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("No tasks available right now!")
    else:
        for Task in tasks:
            print(f'{Task["id"]} | {Task["description"]} | {Task["state"]}')


# Main CLI Logic

def main():
    if len(sys.argv) < 2:
        print("No command found!")
        return 
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("No description found!")
            sys.exit()
            return
        
        description = sys.argv[2]
        add_tasks(description)

    elif command == "list":
        list_tasks()

    elif command == "update":
        if len(sys.argv) < 4:
            print("Description is not available!")

        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Task number not given")
        
        delete(int(sys.argv[2]))
    
    elif command == "mark-in-progress":
        status_update(int(sys.argv[2]), "in-progress")

    elif command == "mark-done":
        status_update(int(sys.argv[2]), "done")

    else:
        print("Unknown command!")
        sys.exit()
        return

if __name__ == "__main__":
    main()