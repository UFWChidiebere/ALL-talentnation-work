# def find_min_max(nums: list[int]) -> tuple[int, int]:
#     maximum = nums[0]
#     minimum = nums[0]
#     for num in nums:
#         if num < minimum:
#             minimum = num
#         if num > maximum:
#             maximum = num
#     print((maximum, minimum))

#     total = 0
#     for num in nums:
#         total += num
#     print(f'The total of the whole list after finding the maximum and minimum is: {total}')
        
    

# n1 = [3, 1, 9, 4, 2, 7]
# n2 = [ 4, 5, 6, 10, 11,19]
# find_min_max(n1)
# find_min_max(n2)
















# def find(nums):
#     largest_num = max(nums)
#     smallest_num = min(nums)
    
        
#     return (largest_num, smallest_num)
# n = [3, 1, 9, 4, 2, 7]
# print(find(n))


'''adewale"s logic'''

def max(nums):
    if not nums:
        return None
    
    max_numbers = float("-inf")
    for num in nums:
        if num > max_numbers:
            max_numbers = num
    return max_numbers


def min(nums):
    if not nums:
        return None
    
    min_numbers = float("inf")
    for num in nums:
        if num < min_numbers:
            min_numbers = num
    return min_numbers


def find_min_max(nums: list[int]) -> tuple[int, int]:
    return (max(nums), min(nums))



n = [3, 1, 9, 4, 2, 7]
print(max(n))

n = [3, 1, 9, 4, 2, 7]
print(min(n))




'''this is for initializing the variable to None '''

def max(nums):
    max_numbers = None
    for num in nums:
        # If it's the first run, or if the current num is larger
        if max_numbers is None or num > max_numbers:
            max_numbers = num
    return max_numbers

n = [3, 1, 9, 4, 2, 7]
print(max(n))  # Output: 9
