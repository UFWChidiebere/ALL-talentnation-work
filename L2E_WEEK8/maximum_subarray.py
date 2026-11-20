def max_subarray_brute(nums: list[int]) -> tuple[int, tuple[int, int]]:
    if not nums:
        return 0, (-1, -1)

    max_sum = nums[0]
    start_idx, end_idx = 0, 0
    n = len(nums)

    for i in range(n):
        current_running = 0
        for j in range(i, n):
            current_running += nums[j]
            if current_running > max_sum:
                max_sum = current_running
                start_idx, end_idx = i, j
    return f'SUM: {max_sum}, INDICES: {(start_idx, end_idx)}'


'''this is the fast method to solving this problem which is called the KADANE'S ALGORITHM- which involve parsing the list exactly once'''

def max_subarray_fast(nums: list[int]) -> tuple[int, tuple[int, int]]:
    if not nums:
        return 0, (-1, -1)
    max_so_far = nums[0]
    current_max = nums[0]
    start, end, temp_start = 0, 0, 0

    for i in range(1, len(nums)):
        if nums[i] > current_max + nums[i]:
            current_max = nums[i]
            temp_start = i
        else:
            current_max += nums[i]

        if current_max>max_so_far:
            max_so_far = current_max
            start = temp_start
            end = i
    return F'SUM: {max_so_far}, INDICES: {(start, end)}'




print(max_subarray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_brute([5]))                             
print(max_subarray_brute([-3, -1, -2]))     

print(' ' * 10)
print(max_subarray_fast([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_fast([5]))                             
print(max_subarray_fast([-3, -1, -2]))    
