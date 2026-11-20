def find_factorial(n):
    if n == 0:
        return 1
    return n * find_factorial(n - 1)

print(find_factorial(8))


'''to do same thing with a for loop and without a function: getting the user input and then doing the factorial'''

# 1. Get the number from the user and convert it to an integer
user_input = input("Enter a number to find its factorial: ")
num = int(user_input)

# 2. Initialize a tracker variable at 1 (since multiplying by 0 would ruin the math)
factorial = 1

# 3. Check for negative numbers, zero, or calculate the factorial
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # Loop from 1 up to the user's number (inclusive)
    for i in range(1, num + 1):
        factorial = factorial * i
        
    # 4. Output the final calculation
    print(f"The factorial of {num} is {factorial}")





# 1. Get user input and convert to integer
user_input = input("Enter a number to find its factorial: ")
num = int(user_input)

# Keep a copy of the original number for the final print statement
original_num = num

# 2. Initialize the result tracker at 1
factorial = 1

# 3. Check edge cases and execute the loop
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # The loop runs as long as num is greater than 1
    while num > 1:
        factorial = factorial * num  # Multiply current value
        num -= 1                     # Decrease number by 1 to move toward the exit condition
        
    # 4. Output the final calculation
    print(f"The factorial of {original_num} is {factorial}")

