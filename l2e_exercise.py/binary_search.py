def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
print(binary_search([1,3,4,5,6,7,10,14,50,76,56,32,53,13,46,78,], 78))


"""Function BinarySearch(array, target):
    1. Set 'low' to 0 (the start of the array)
    2. Set 'high' to the last index of the array (length of array - 1)

    3. While 'low' is less than or equal to 'high':
        
        a. Calculate the middle index: 
           mid = (low + high) divided by 2 (round down to whole number)

        b. If the item at array[mid] is equal to target:
           Return mid (We found it!)

        c. Else if the item at array[mid] is less than target:
           Move the 'low' wall to mid + 1 (Look in the right half)

        d. Else (the item at array[mid] must be greater than target):
           Move the 'high' wall to mid - 1 (Look in the left half)

    4. If the loop ends and we haven't returned anything:
       Return -1 (The target is not in the array)
the above is the psuedocode for the code above"""