tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. add")
    print("2. view")
    print("3. remove")
    print("4. quit")
    
    choice = input("Enter your choice: ").strip().lower()
    
    if choice == "add":
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print(f"'{new_task}' added successfully.")
        
    elif choice == "view":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
                
    elif choice == "remove":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            # Show list first so they know what to remove
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
                
            try:
                task_num = int(input("Enter the task number to remove: "))
                # Convert 1-based user input to 0-based index
                index_to_remove = task_num - 1
                
                if 0 <= index_to_remove < len(tasks):
                    removed = tasks.pop(index_to_remove)
                    print(f"Removed task: '{removed}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid integer number.")
                
    elif choice == "quit":
        print("Goodbye!")
        break
        
    else:
        print("Invalid option. Please type add, view, remove, or quit.")