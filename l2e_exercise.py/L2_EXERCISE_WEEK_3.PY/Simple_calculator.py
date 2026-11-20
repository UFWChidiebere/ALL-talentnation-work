def simple_calculator():

    total = 0.0
    history = [total]
    print("Continous Calculator Started. Type 'undo' to revert or 'exit' to stop.")
    print(f"Current Total: {total}")

    while True:
        user_input = input("Enter operator and number (e.g., +5) or 'undo': ").strip()

        if user_input.casefold() == 'exit':
            break

        if user_input.casefold() == 'undo':
            if len(history) > 1:
                history.pop() #remove current state
                total = history[-1] #revert to previous
                print(f"Undo successful: Reverted to: {total}")
            else:
                print("Nothing to undo.")
            continue

        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid input format. Use: [operator] [number]")
            continue

        operator, num_str = parts[0], parts[1]
        try:
            num = float(num_str)
        except ValueError:
            print("Error: Invalid number.")
            continue

        if operator == '+':
            total += num
        elif operator == '-':
            total -= num
        elif operator == '*':
            total *= num
        elif operator == '/':
            if num == 0:
                print("Error: Division by zero is not allowed.")
                continue
            total /= num
        else:
            print("Invalid operator: Use +, -, *, or /")
            continue

        history.append(total)
        print(f"REsult: {total}")

simple_calculator()














"""Initialize State: Create a variable total starting at 0.0. Create a history list history = [total] to act as a stack for the undo feature.

Infinite Loop: Use while True to keep the calculator running continuously.

Parse Input: Prompt for a command. If the user enters "undo", check if history has more than one state. If yes, pop the current state and set total to the previous state.

Validation: Split or validate the user input to extract the operator and the number. Ensure the number can cast safely to a float.

Compute & Guard Operations: Use structured if/elif blocks instead of eval(). Explicitly check if the operator is / and the number is 0 to catch Division by Zero without crashing.

Save State: Append the new total to history after every successful calculation."""
        