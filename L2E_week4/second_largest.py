'''STEP 1: Define the pure helper function 'step(largest, second_largest, x)'.
        - If x is strictly greater than 'largest':
            - The old 'largest' becomes the new 'second_largest'.
            - 'largest' becomes x.
        - Otherwise, if x is strictly greater than 'second_largest' AND x is not equal to 'largest':
            - 'second_largest' becomes x.
        - Return the updated tuple: (largest, second_largest)

STEP 2: Define the main function 'second_largest(nums)'.
        - Initialize 'largest' and 'second_largest' to float('-inf') (negative infinity).
          (We use negative infinity as a safe baseline so that the function can handle negative numbers perfectly!)
        - Loop through every number 'x' inside the 'nums' list:
            - Update our tracking variables by calling the 'step' function:
              largest, second_largest = step(largest, second_largest, x)
        - Return 'second_largest'

STEP 3: Run the main program.
        - Create your test lists (including lists with duplicates).
        - Call 'second_largest(list)' and print the answer from OUTSIDE.
'''

# --- STEP 1: The Pure Logic Step Helper ---
def step(largest: float, second_largest: float, x: int) -> tuple[float, float]:
    """Pure evaluation function to ranking an element inside a stream."""
    if x > largest:
        # The old king drops down to 2nd place, and x becomes the new king
        second_largest = largest
        largest = x
    elif x > second_largest and x != largest:
        # x is not big enough to beat 1st place, but beats 2nd place (and isn't a duplicate)
        second_largest = x
        
    return largest, second_largest


# --- STEP 2: The Main One-Pass Processing Loop ---
def second_largest(nums: list[int]) -> float:
    """Finds the second largest unique element with a single pass."""
    # We initialize variables to negative infinity to handle any negative integer inputs safely
    largest = float('-inf')
    second_largest = float('-inf')
    
    for x in nums:
        # Update our scoreboard positions by feeding the data into our helper function
        largest, second_largest = step(largest, second_largest, x)
        
    return second_largest


# --- STEP 3: Main Program Execution (Printing strictly outside) ---
test_1 = [10, 5, 8, 20, 15]
test_2 = [4, 9, 2, 9, 7]

result_1 = second_largest(test_1)
result_2 = second_largest(test_2)

print(f"Input: {test_1} → Output: {result_1}")
print(f"Input: {test_2} → Output: {result_2}")


'''bonus question answer'''
from functools import reduce

def second_largest_reduce(nums: list[int]) -> float:
    """Bonus alternative using reduce where the accumulator is our tracking tuple."""
    initial_state = (float('-inf'), float('-inf'))
    
    # reduce takes our step function, loops over nums, and bubbles up the final tuple state
    final_largest, final_second = reduce(
        lambda acc, x: step(acc[0], acc[1], x), 
        nums, 
        initial_state
    )
    
    return final_second
