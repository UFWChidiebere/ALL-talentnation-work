def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num == largest or num == second_largest:
            '''ignore duplicate numbers/values'''
            continue 

        if num == largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    if second_largest == float("inf"):
        return "No unique second largest number found."

    return second_largest

input1 = [10, 5, 8, 20, 15]
input2 = [4, 9, 2, 9, 7]
print(find_second_largest(input1))
print(find_second_largest(input2))













"""Initialize State: Define largest and second_largest as negative infinity (float('-inf')) to securely handle lists with negative numbers.

Single Pass Evaluation: Loop through each number in the array exactly once.Filter Duplicates: If the current item is equal to largest or second_largest, pass over it.

Cascade Value Shift: If a number is strictly larger than largest, the old largest cascades down to become the second_largest, and the current number becomes the new largest.

Alternative Update: If it isn't larger than largest but is strictly larger than second_largest, update only second_largest."""
