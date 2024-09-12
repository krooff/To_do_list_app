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

def delete_task():
    """Delete a task from the to-do list."""
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task['title']}' has been deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

def main():
    """Main function to run the to-do list application."""
    while True:
        display_menu()
        try:
            choice = input("\nChoose an option (1-5): ").strip()
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                mark_task_complete()
            elif choice == '4':
                delete_task()
            elif choice == '5':
                print("\nThank you for using the To-Do List App. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("\nReturning to the menu...")

if __name__ == "__main__":
    main()