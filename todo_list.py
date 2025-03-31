tasks = []
while True:
    print("\n to-do list")
    print("1. view tasks")
    print("2. add tasks ")
    print("3. remove tasks")
    print("4. Exit")
    choice = input("enter the number :")

    if choice == "1":
        if not tasks:
            print("no task yet !")
        else:
            print("your tasks") 
            for i,tasks in enumerate(tasks,1):
                print(f"{i}. {task}")

    elif choice == "2":
        task= input("enter your task:").strip()
        priority= input("enter your task priority:").strip()  
        tasks.append(task)

    elif choice == "3":
        if not tasks:
            print("no tasks to remove!")
        else:
            print("your tasks : ")
            for i ,task in enumerate(tasks,1):
                print(f"{i}. {task}")
            try:    
                task_number = int(input("enter the task number to remove:"))
                removed_task = tasks.pop(task_number -1)
                print(f"task {removed_task} removed ")
            except (IndexError,ValueError):
                print("Invalid number! Please enter a valid task number")

    elif choice == "4":
        print("thank you for using the To-Do List!")
        break

    else:
        print("invalid number ! please enter number between 1-4")