import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if no file is found

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        print("Task added!")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete!")
        return

    list_tasks(tasks)  # Show tasks before deleting
    index = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def mark_complete(tasks):
    if not tasks:
        print("No tasks to mark complete!")
        return

    list_tasks(tasks)
    index = int(input("Enter the number of the task to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        if tasks[index]["completed"]:  # Check if already completed
            print("Task is already completed!")
        else:
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Task marked complete!")
    else:
        print("Invalid task number.")

    list_tasks(tasks)
    index = int(input("Enter the number of the task to mark complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked complete!")
    else:
        print("Invalid task number.")

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list!")
        return

    for i, task in enumerate(tasks):
        prefix = "[x]" if task["completed"] else "[ ]"
        print(f"{i+1}. {prefix} {task['task']}")

if __name__ == "__main__":
    tasks = load_tasks()

    while True:
        print("\nChoose an action:")
        print("1. Add task")
        print("2. Delete task")
        print("3. Mark task complete")
        print("4. List tasks")
        print("5. Exit")

        choice = input("> ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            delete_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice")
