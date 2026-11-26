
def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

my_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = removeDuplicates(my_nums)

print(f"Returned unique length (k): {k}") 

print(f"The unique items at the front of the list: {my_nums[:k]}")


def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write_index = []
    for num in nums:
        if num in write_index:
            continue
        write_index.append(num)
    return (write_index)
nums = [1,1,2]
print(removeDuplicates(nums))

'''this is the way to make a function that removes duplicates from a list of integers. The function takes a list of integers as input and returns the length of the list after removing duplicates. It uses a write index to keep track of the position where the next unique element should be written. The function iterates through the list, comparing each element with the previous one, and only writes unique elements to the front of the list. Finally, it returns the length of the unique elements.'''



