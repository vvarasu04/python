tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()

while True:
    print("Options: 1.Add 2.Remove 3.Show 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == '2':
        show_tasks()
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")



