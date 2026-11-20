def sum_list(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total
x = sum_list([1,2,3,4,5])
y = sum_list([-1, 10, -5, 20])
print(x)
print(y)


'''the first thing i did was to create a list variable called total, when i looped through and then print the result, it just returned what was inputed,,,, i then changed it to 0 and then use the += cox i was using the append list method'''

'''another method to do this is to make the num variable that is looping throught the argument/parameter to be initialized to index 0

like total = num[0]
and then the for loop will now start at : for num in num[1:]

also we can use the range function and then loop through the numbers 

for num in range(0, len(num))'''


def sum_list(nums: list[int]) -> int:
    total = 0
    for num in range(len(nums)):
        total += nums[num]
    return total
x = sum_list([1,2,3,4,5])
y = sum_list([-1, 10, -5, 20])
print(x)
print(y)



'''this is for one making the accumulator to index 0 and since it is in 0, we move the argument/parameter to index 1'''
def sum_list(nums: list[int]) -> int:
    acc = nums[0]
    for num in nums[1:]:
        acc += num
    return acc
x = sum_list([1,2,3,4,5])
y = sum_list([-1, 10, -5, 20])
print(x)
print(y)

