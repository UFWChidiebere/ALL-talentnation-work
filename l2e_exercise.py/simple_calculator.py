def simple_calculator(first_num, second_num, operator):
    """this code is for when input is not required and a function is being used """
    if operator == "*":
        print(first_num * second_num)
    elif operator == "+":
        print(first_num + second_num)
    elif operator == "-":
        print(first_num - second_num)
    elif operator == "/":
        if second_num == 0:
            print("Cannot divide by zero")
        else:
            # This only runs if second_num is NOT 0
            print(first_num / second_num) 
    else:
        print("invalid operator")

simple_calculator(15, 0, "/")



"""the code below is for when there's function and input is required and try and error is used to optimize the code"""
def simple_calculator():
    first_input = input("Input: ").strip()
    operator = input("Operator: ").strip()
    second_input = input("Input: ").strip()

    try:
        num1 = float(first_input)
        num2 = float(second_input)
    except ValueError:
        print("Output: Invalid numeric input")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Output: Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Output: Invalid operator")
        return

    if result.is_integer():
        result = int(result)

    print(f"Result: {result}")

simple_calculator()



"""alternative method: Dictionary Dispatch(No if-elif)
though this method violate the instructions in the task, however......."""
import operator

def alternative_calculator():
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    try:
        num1 = float(input("Input 1: "))
        op = input("Operator: ").strip()
        num2 = float(input("Input 2: "))

        if op not in ops:
            print("Output: Invalid operator")
            return
        if op == "/" and num2 == 0:
            print("Output: Cannot divide by zero")
            return

        result = ops[op] (num1, num2)
        print(f"Result: {int(result) if result.is_integer() else result}")
    except ValueError:
        print("Output: Invalid numeric input")

