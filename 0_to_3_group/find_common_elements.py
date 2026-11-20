def find_common_elements(list1: list, list2: list) -> list:
    same_elements = []
    for elements in list1:
        if elements in list2 and elements not in same_elements:
            same_elements.append(elements)

    return same_elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = ["a", "b", "c"]
list4 = ["x", "y", "z"]
print(find_common_elements(list1, list2))
print("-" * 20)
print(find_common_elements(list3, list4))



'''this was the logic i had initially but it is a total nonsense'''
def find_common_elements(list1: list, list2: list) -> list:
    same_elements = []
    for i in list1 and list2:
        if i in list1 == i in list2 and i not in same_elements:
            same_elements.append(i)
    return same_elements

'''this is the one that can be done using the list and set method'''
def find_common_elements(list1: list, list2: list) -> list:
    # Converting to sets finds duplicates instantly and efficiently
    return list(set(list1).intersection(set(list2)))
#the method above is fast but there's a method that is more faster..... that is the one below



def find_common_elements_super_fast(list1: list, list2: list) -> list:
    #turn only the second list into a set for 0(1) lighting lookups
    set2 = set(list2)

    #loop through list1 and look up directly inside the set2's hash tables
    return [item for item in list1 if item in set2]



#now the above code is for when we know which of the list is the smallest. what if we do not know the smallest list before hand?. then we use the code below that have conditionals checkking for the length of the two list.

def find_common_elements_smartest(list1: list, list2: list) -> list:
    # Check which list is smaller
    if len(list1) < len(list2):
        # If list1 is smaller, turn it into a set
        small_set = set(list1)
        return [item for item in list2 if item in small_set]
    else:
        # If list2 is smaller (or they are equal), turn it into a set
        small_set = set(list2)
        return [item for item in list1 if item in small_set]


'''You might worry that checking len(list1) takes a long time if the list has a million items.
Fortunately, in Python, checking the length of a list is instant—\(O(1)\) constant time. Python keeps track of a list's size in a hidden counter variable behind the scenes. It doesn't count the items one by one; it just reads that counter instantly.
Would you like to move on to the next programming question on your sheet, or is there another concept here you'd like to explore?
'''
