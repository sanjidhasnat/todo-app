from todo import TodoManager

manager = TodoManager()

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as done/undone")
    print("4. Delete task")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        name = input("Task name: ")
        manager.add_task(name)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        manager.view_tasks()
        idx = int(input("Enter task number: ")) -1 
        manager.mark_done(idx)

    elif choice == "4":
        manager.view_tasks()
        idx = int(input("Enter task number: "))-1
        manager.delete_tasks(idx)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again!")           
