# Grab a piece of paper or type it out here, and trace the steps the program takes by finding the low index, the high index, and the calculated middle index (mid = (low + high) // 2) for each loop until you land on the number.Hint: Keep in mind that // drops any decimals (e.g., 3.5 becomes 3).What are the values of low, high, and mid during the very first round of the loop? Try tracking the first split!

def binary_tracking(arr, target):
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