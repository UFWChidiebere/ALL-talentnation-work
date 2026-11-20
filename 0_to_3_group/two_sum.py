'''this code is the fastest '''
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:

            return f'INDICES: {[seen[complement], index]} VALUES: {[complement, value]}'
            return [seen[complement], index]
            return [complement, value] # this line of code is to return the value itself instead of the index in which the values were found.
        seen[value] = index
    return []

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([3, 2, 4], 6))       # Output:

print('*' * 10)
'''this is the method that is simplier, however, it is very slow due to the fact that a nested for loop is being used however, it does not take up memory'''
def two_sum_2_loops(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range( i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j] #this is the line that makes the returning of the index possible. 
                return [nums[i], nums[j]] #if i want the code to return the values that make up the sum of the target and not the index, i will have to use this block of code.
    return []
print(two_sum_2_loops([2, 7, 11, 15], 9)) 
print(two_sum_2_loops([3, 2, 4], 6))   



'''i want to try and use the set method to try returning the values in the list instead of the index'''
def two_sums(nums: list[int], target: int) -> list[int]:
    seen = set()
    for values in nums:
        complement = target - values
        if complement in seen:
            return [complement, values]
        seen.add(values)

    return []
print(two_sums([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sums([3, 2, 4], 6))       # Output:



'''this is me trying tp use one loop one for loop instead'''

#after much delibration with Lawrence, found out that it is not worth it so didn't end up doing it.