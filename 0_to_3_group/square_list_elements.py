def square_elements(nums: list[int]) -> list[int]:
    # return list(map(lambda num: num ** 2, nums))

    return [x ** 2 for x in nums]

nums = [1, 2, 3, 4]
nums1 = [-2, 0, 5]
print(square_elements(nums))
print(square_elements(nums1))


'''this above is how to solve the problem using map amd liat comprehension as requested by the task'''

'''the code below is me trying to solve the code using a for loop'''
def square_elements_loops(nums: list[int]) -> list[int]:
    # if len(nums) == 0:
    #     return []   #this part i was trying to create a base case but i was made to understand that it is not needed cox the for loop already handles the empty list
    squared = []
    for num in nums:
        result = num ** 2 
        squared.append(result)
    return squared 
print('-' * 10)
nums = [1, 2, 3, 4]
nums1 = [-2, 0, 5]
print(square_elements_loops(nums))
print(square_elements_loops(nums1))



'''now  let me try to use a while loop to trying to solve the problem'''

def squared_elements_while(nums: list[int]) -> list[int]:
    squared = []
    i = 0
    while i < len(nums):
        num = nums[i]
        squared.append(num ** 2)
        i += 1
    return squared






    # if len(nums) == 0:
    #     return []
    # squared = []
    # while len(nums) >=1:
    #     for num in nums:
    #         result = num ** 2
    #         squared.append(result)
    # return squared
nums = [1, 2, 3, 4]
nums1 = [-2, 0, 5]
print('=' * 10)
print(squared_elements_while(nums))
print(squared_elements_while(nums1))


'''now let me try and use recursion to solve the task'''

def squared_elements_recursion(nums: list[int]) -> list[int]:
    #this is the base case of the recursive call
    if not nums:
        return []
    return [nums[0] ** 2] + squared_elements_recursion(nums[1:])
nums = [1, 2, 3, 4]
nums1 = [-2, 0, 5]
print('*' * 10)
print(squared_elements_recursion(nums))
print(squared_elements_recursion(nums1))



'''Ai assisted recursion'''
def squared_elements_recursion(nums: list[int], index: int = 0) -> list[int]:
    # Base case: stop when the index reaches the end of the list
    if index == len(nums):
        return []
    
    # Square the current item and move the index forward by 1
    return [nums[index] ** 2] + squared_elements_recursion(nums, index + 1)

nums = [1, 2, 3, 4]
nums1 = [-2, 0, 5]
print('*' * 10)
print(squared_elements_recursion(nums))
print(squared_elements_recursion(nums1))



'''(Note: Keep in mind that Python has a default recursion limit of 1,000 calls, so for massive lists, your earlier for loop or a map() approach will always be safer than recursion.)'''
    