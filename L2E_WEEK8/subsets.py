def subsets(items):
    if not items:
        return [[]]
    
    first = items[0]
    remainder = items[1:]
    
    # Recursive step: get all subsets of elements behind the first index
    sub_combinations = subsets(remainder)
    
    # Mathematical bifurcation: subset with 'first' element included, or excluded
    with_first = [[first] + sub for sub in sub_combinations]
    
    # Return fresh unified lists
    return sub_combinations + with_first


def permutations(items):
    if len(items) == 0:
        return [[]]
        
    all_permutations = []
    for i in range(len(items)):
        current = items[i]
        # Keep original sequence pristine by splicing elements around the index
        remaining_elements = items[:i] + items[i+1:]
        
        for p in permutations(remaining_elements):
            all_permutations.append([current] + p)
            
    return all_permutations


# --- Bonus Implementation ---
def subsets_with_sum(items, target):
    # Generates a pure snapshot list using power set calculations 
    all_sets = subsets(items)
    return [sub for sub in all_sets if sum(sub) == target]


# Validation Engine tracking N growth patterns 
print("--- N Verification Analysis ---")
for n in range(9):
    test_list = list(range(1, n + 1))
    sub_count = len(subsets(test_list))
    perm_count = len(permutations(test_list))
    print(f"N={n} | Subsets: {sub_count} (2^{n}={2**n}) | Permutations: {perm_count} ({n}!)")

print("\n--- Bonus Test Cases ---")
print("Subsets adding up to 5 in [1, 2, 3, 4]:", subsets_with_sum([1, 2, 3, 4], 5))
