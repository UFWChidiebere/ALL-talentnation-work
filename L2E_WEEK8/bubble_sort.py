def bubble_sort(nums: list[int], descending:bool=False) -> tuple[list[int], int, int]:
    arr = [x for x in nums]
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(0, n):
        swapped = False

        for j in range(0, n - i - 1):
            comparisons += 1

            if descending:
                should_swap = (arr[j] < arr[j + 1])
            else:
                should_swap = (arr[j] > arr[j + 1])

            if should_swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if  not swapped:
            break
    return (arr, comparisons, swaps)

if __name__ == "__main__":
    print("--- BUBBLE SORT METRICS ---")
    sorted_list = [1, 2, 3, 4, 5]
    reverse_list = [5, 4, 3, 2, 1]
    
    _, best_comps, _ = bubble_sort(sorted_list)
    _, worst_comps, _ = bubble_sort(reverse_list)
    
    print(f"Already Sorted List Comparisons (Best Case): {best_comps}")
    print(f"Reverse Sorted List Comparisons (Worst Case): {worst_comps}")
    print("-" * 40)

    print("--- TOGGLE FUNCTIONAL TESTS ---")
    test_data = [5, 1, 4, 2, 8]
    
    # 1. Standard Ascending Sort
    normal_sorted, _, _ = bubble_sort(test_data)
    print(f"Normal (Ascending):  {normal_sorted}")
    
    # 2. RUNNING THE BONUS PART (Descending Sort)
    bonus_sorted, _, _ = bubble_sort(test_data, descending=True)
    print(f"Bonus (Descending): {bonus_sorted}")