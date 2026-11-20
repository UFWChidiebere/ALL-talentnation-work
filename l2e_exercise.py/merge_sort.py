def merge_sort(parameter):
    """this is to return the argument that wull be passed in later if it is just one argument"""
    if len(parameter) <= 1:
        return parameter


    """this is to calcluate how the true division is going to be handled"""
    middle = len(parameter) // 2

    """now we use recursion to call on the function to handle left and rght of the items"""

    left = merge_sort(parameter[:middle])
    right = merge_sort(parameter[middle:])

    """now we create an empty list and two empty variables to be able to loop left and right and merge them into the empty list after the sorting is completed"""

    sorted_list = []
    i = 0
    j = 0

    """looping through"""
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j+= 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

list1= merge_sort([5,7,9,10,11,32,56,78,98,100,1000,10000,4000,400,200,20,50,60,91,45,65,21,12,13,14,78,96])

print(list1)
        