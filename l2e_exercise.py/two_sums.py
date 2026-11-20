def two_sum_indices(numbers, target):
    # Outer pointer moves through the list
    for i in range(len(numbers)):
        # Inner pointer scans exclusively ahead of the current index
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None

print(two_sum_indices([1,2,3,4], 3))



"""Alternative Method: Tracking Visited Elements with a Hash Table (O(N) Speed)
Instead of searching through a nested loop over and over again (O(N^2)), we can loop through the list just once (O(N)).
For every number, we calculate its "complement" (what value we need to reach the target). We look up if that complement is already stored inside a memory lookup dictionary. Since lookups in hash tables take constant time, this is incredibly fast!"""

def alternative_two_sum(numbers, target):
    seen_elements = {}  # Format: {value: index}
    
    for current_index, current_num in enumerate(numbers):
        complement = target - current_num
        
        # Check if the needed complement number has been stored previously
        if complement in seen_elements:
            return [seen_elements[complement], current_index]
            
        # Store current number position inside hash table registry
        seen_elements[current_num] = current_index
        
    return None
