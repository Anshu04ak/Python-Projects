tasks = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. Mark a task as done")
    print("3. Remove a task")
    print("4. View all tasks")
    print("5. Exit")
    choice = input("Enter your Choice: ")

    if choice == '1':
        print()
        no_of_task=int(input("How many task you want to add : "))
        for i in range(no_of_task):
            task = input("Add your Task: ")
            tasks.append([task, False])  
            print(f"Task: '{task}' added.")

    elif choice == '2':
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1][1] = True  
            print(f"Task '{tasks[task_num - 1][0]}' marked as done.")
        else:
            print("Invalid task number.")

    elif choice == '3':
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks = [task for idx, task in enumerate(tasks) if idx != task_num - 1]
            print(f"Task number {task_num} removed.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task[1] else "Not Done"
            print(f"{idx}. {task[0]} - {status}")
            
    elif choice == '5':
        print("Exiting the to-do list manager.")
        break
    
    else:
        print("Invalid choice, please try again.")