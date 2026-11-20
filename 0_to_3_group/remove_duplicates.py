def remove_duplicates(nums: list) -> list:
    cleaned_list = []
    for element in nums:
        if element in cleaned_list:
            continue
        cleaned_list.append(element)
    return cleaned_list

def remove_duplicates_2(nums: list) -> list:
    no_duplicates = []
    for item in nums:
        if item not in no_duplicates:
            no_duplicates.append(item)
    return no_duplicates


'''the method below is one of the fastest and it use set - though not the fastest'''
def remove_duplicates_fastest(nums: list) -> list:
    return list(set(nums)) #set instantly drops all duplicates at C-speed and the list constructor converts it back to satisfy the function signature. the method is fast just that it will re-arrange the list to be in order(if they are unordered before)

'''if the assignment requires the items to stay in their original order, you can combine a set (for instant 0(1) lookup speed) with a list (for maintaining order)'''
def remove_duplicates_ordered_fast(nums: list) -> list:
    cleaned_list = []
    seen = set()
    for element in nums:
        if element not in seen:
            seen.add(element)
            cleaned_list.append(element)
    return cleaned_list
#this code is the fastest of all the code that is written for this task.

nums = [1, 2, 5, 3, 4, 3, 2]
nums1 = ["apple", "banana", "apple", "cherry"]
print(remove_duplicates(nums))
print(remove_duplicates(nums1))
print('-' * 30)
print(remove_duplicates_2(nums))
print(remove_duplicates_2(nums1))


print('@' * 30)
print(remove_duplicates_fastest(nums))
print('#'* 30)
print(remove_duplicates_ordered_fast(nums))





# if element not in cleaned_list:
# if element in cleaned_list:
#     element.skip()
# else:
#     cleaned_list.append(element)
# return cleaned_list