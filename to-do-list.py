todo = {}

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        todo[task] = "Pending"
        print("Task added successfully!")

    elif choice == "2":
        if len(todo) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for task, status in todo.items():
                print(f"{task} --> {status}")

    elif choice == "3":
        task = input("Enter task name to mark as completed: ")
        if task in todo:
            todo[task] = "Completed"
            print("Task marked as completed!")
        else:
            print("Task not found.")

    elif choice == "4":
        task = input("Enter task name to delete: ")
        if task in todo:
            del todo[task]
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    elif choice == "5":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice. Please enter 1 to 5.")