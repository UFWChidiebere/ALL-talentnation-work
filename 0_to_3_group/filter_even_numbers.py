def filter_even_numbers(nums: list[int]) -> list[int]:
    even_num = []
    for num in nums:
        if num % 2 == 0:
            even_num.append(num)
    return even_num
nums = [1, 2, 3, 4, 5, 6]
nums2 = [1, 3, 5, 7]
print(filter_even_numbers(nums))
print('*'* 20)
print(filter_even_numbers(nums2))


'''the above code is correct logically however, it doesn't meet the task requirement.... which is to use filter'''

'''this is the code that meet up the requirement for the task'''
def filter_even_numbers(nums: list[int]) -> list[int]:
    return list(filter(lambda num: num % 2 == 0, nums))
'''to use lambda, this is the antamoy of it
    lambda(the key word for anonymous function) followed by the argument, a colon, and then the expression.
    
    lambda argument: expressiion'''
    


nums = [1, 2, 3, 4, 5, 6]
nums2 = [1, 3, 5, 7]
print(filter_even_numbers(nums))   # Output: [2, 4, 6]
print(filter_even_numbers(nums2))  # Output: []





#this same task can be done using a list comprehension which is the most pythonic way and it is the fastest way among the three
def filter_even_numbers(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]
