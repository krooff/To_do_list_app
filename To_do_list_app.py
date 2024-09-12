tasks = []

def display_menu():

    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task():
    task_title = input("\nEnter the title of the task: ").strip()
    if task_title:
        tasks.append({"title": task_title, "status": "Incomplete"})
        print(f"Task '{task_title}' added to the list.")
    else:
        print("Task title cannot be empty.")

def view_tasks():
    """View the list of tasks with their statuses."""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']}")

def mark_task_complete():
    """Mark a specific task as complete."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as complete: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["status"] = "Complete"
                print(f"Task '{tasks[task_number - 1]['title']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")