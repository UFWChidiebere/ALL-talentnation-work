def insertion_sort(nums: list) -> tuple:
    comparisons = 0
    shifts = 0
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if nums[j] > key:
                nums[j+1] = nums[j]
                shifts+=1
                j=j-1
            else:
                break
        nums[j+1] = key
    return (comparisons, shifts)

print(insertion_sort([5, 2, 4, 1])) #-> sorted [1, 2, 4, 5], returns (6, 5)
print(insertion_sort([1, 2, 3, 4]))  #-> already sorted, returns (3, 0)
print(insertion_sort([4, 3, 2, 1]))  #-> reversed, returns (6, 6)
print(insertion_sort([]))           #-> returns (0, 0)



print('============================================')
# --- Demonstrating operational costs outside the function ---
sorted_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_10    = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_20 = list(range(1, 21))
rev_20    = list(range(20, 0, -1))

print(f"Sorted 10 elements: {insertion_sort(sorted_10)}") # Outputs: (9, 0)
print(f"Reversed 10 elements: {insertion_sort(rev_10)}")   # Outputs: (45, 45)
print(f"Sorted 20 elements: {insertion_sort(sorted_20)}") # Outputs: (19, 0)
print(f"Reversed 20 elements: {insertion_sort(rev_20)}")   # Outputs: (190, 190)
