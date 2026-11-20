def binary_search(nums, target)-> tuple [int, int]:
    low = 0
    high = len(nums) -1
    result_idx = -1
    comparisons = 0
    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1

        if nums[mid] == target:
            result_idx = mid 
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return (result_idx, comparisons)

# nums = [1, 3, 3, 3, 5, 8], target = 3  → (1, comparisons)
# nums = [1, 3, 5, 8],       target = 4  → (-1, comparisons)
# nums = [],                 target = 7  → (-1, 0)

print(binary_search([1, 3, 3, 3, 5, 8], 3))
print(binary_search([1, 3, 5, 8],  4))
print(binary_search([], 7))


'''this is the solution for the bonus questiom'''
def binary_search_recursive_helper(nums: list[int], target: int, low: int, high: int, current_best: int, comps: int) -> tuple[int, int]:
    if low > high:
        return current_best, comps
    
    mid = (low + high) // 2
    comps += 1
    
    if nums[mid] == target:
        return binary_search_recursive_helper(nums, target, low, mid - 1, mid, comps)
    elif nums[mid] < target:
        return binary_search_recursive_helper(nums, target, mid + 1, high, current_best, comps)
    else:
        return binary_search_recursive_helper(nums, target, low, mid - 1, current_best, comps)

def binary_search_recursive(nums: list[int], target: int) -> tuple[int, int]:
    return binary_search_recursive_helper(nums, target, 0, len(nums) - 1, -1, 0)

print(' ' * 30)
print(binary_search_recursive([1, 3, 3, 3, 5, 8], 3))
print(binary_search_recursive([1, 3, 5, 8],  4))
print(binary_search_recursive([], 7))

