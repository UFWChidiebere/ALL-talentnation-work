def find_second_largest(numbers):
    largest = None
    second_largest = None
    
    for num in numbers:
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num
            
    return second_largest


# 1. Define a list of numbers
my_numbers = [10, 5, 8, 20, 15]

# 2. Call the function and print the result
result = find_second_largest(my_numbers)
print(f"The second largest number is: {result}")


print(find_second_largest([4, 9, 2, 9, 7]))      # Output: 7 (ignores the duplicate 9)
print(find_second_largest([-10, -5, -2, -20]))   # Output: -5 (works perfectly with negative numbers!)




"""Alternative Method: Unique Element Set Conversion (No sort)If you convert the list to a unique structure first, you can scrub duplicates out instantly. Then, you can explicitly pop the structural global maximum out of the tracking list to reveal the runner-up."""

def alternative_second_largest(numbers):
    # Unique values filter manually without using built-in set()
    unique_nums = []
    for n in numbers:
        if n not in unique_nums:
            unique_nums.append(n)
            
    # Remove first absolute largest item
    first_max = unique_nums[0]
    for n in unique_nums:
        if n > first_max:
            first_max = n
    unique_nums.remove(first_max)
    
    # The remaining maximum value inside this array is our second largest
    second_max = unique_nums[0]
    for n in unique_nums:
        if n > second_max:
            second_max = n
            
    return second_max

# 1. Define your list of numbers
sample_numbers = [4, 9, 2, 9, 7]

# 2. Call the function and print the returned value
result = alternative_second_largest(sample_numbers)
print(f"The second largest unique number is: {result}")




"""A Quick Warning on this Alternative MethodWhile you call them the same way, look closely at this line in the alternative code:

first_max = unique_nums[0]

if you accidently pass an empty list [] into alternative_second_largest(), unique_nums[0] will crash your program with an IndexError: list index out of range.Your original implementation (find_second_largest) using None initialization is much safer because it gracefully handles empty lists without crashing!Are you ready to move on to Object-Oriented Programming (OOP) concepts, or would you like to see how to call the Word Frequency or Two Sum functions first?"""

