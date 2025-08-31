tasks = []  

def show_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}") 

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(" New task added successfully!")

def remove_task():
    show_tasks()
    num = int(input("Enter task number to remove: "))
    if 0 < num <= len(tasks):
        removed = tasks.pop(num - 1)
        print(f" Removed: {removed}")
    else:
        print(" Invalid number!")

while True:
    print("\n TO-DO LIST APP")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print(" Goodbye!")
        break
    else:
        print(" Invalid option. Try again.")
