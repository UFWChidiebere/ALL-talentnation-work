def start(nums):
    if not nums:
        return None, None, None  # Return None for empty list

    smallest = min(nums)
    largest = max(nums)
    average = sum(nums) / len(nums)

    return smallest, largest, average
#this function takes a list of numbers as input and returns the smallest number, largest number, and average of the numbers in the list. If the input list is empty, it returns None for all three values. this is the normal way to do it but due to the constraints of the assignment, we will not use the built-in min, max, and sum functions. Instead, we will implement our own logic to find the smallest, largest, and average values.

def stats(nums):
    if not nums:
        return None, None, None

    smallest = nums[0]
    largest = nums[0]
    total = 0   

    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num

    average = round(total / len(nums), 2)
    return f'smallest: {smallest}, largest: {largest}, average: {average}'

    # return f"smallest: {smallest}, largest: {largest}, average: {average:.4f}" # was using this line to check the difference between the two methods of rounding the average. The first method rounds to 2 decimal places, while the second method rounds to 4 decimal places. The first method is more appropriate for this assignment, as it is more concise and easier to read.
print(stats([4, 9, 2, 7]) )  
print(stats([5]))          
print(stats([0]))      
#this is the correct implementation of the stats function, which calculates the smallest, largest, and average values from a list of numbers without using built-in functions. It handles empty lists by returning None for all three values.
