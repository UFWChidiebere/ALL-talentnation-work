tasks = []

while True:
    print("\nMenu: add | view | remove | done | quit")
    user_input = input("Enter command: ").lower()

    if user_input == "add":
        task_text = input("Enter task details: ")
        new_task = [task_text, False]
        tasks.append(new_task)
        print("Task added.")

    elif user_input == 'view':
        if len(tasks) == 0:
            print('Your to-do list is empty.')
        else:
            for index in range(0, len(tasks)):
                task = tasks[index]
                status_symbol = " "
                if task[1] == True:
                    status_symbol = 'x'
                print(f'{index + 1}. [{status_symbol}] {task[0]}')

    
    elif user_input == "done" or user_input == "remove":
        if len(tasks) == 0:
            print("No tasks available to modify.")
        else:
            task_num_str = input("Enter task number: ")
            
            
            if not task_num_str.isdigit():
                print('Invalid input. Please enter a valid number.')
            else:
                choice_index = int(task_num_str) - 1
                if choice_index < 0 or choice_index >= len(tasks):
                    print('Task number out of range.')
                else:
                    if user_input == "done":
                        tasks[choice_index][1] = True
                        print("Task marked as done.")
                    else:
                        tasks.pop(choice_index)
                        print("Task removed.")

    elif user_input == "quit":
        print("Goodbye!")
        break 

    else:
        print('Unknown command. Try again.')
