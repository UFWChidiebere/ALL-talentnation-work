'''STEP 1: Define the pure recursive function 'flatten(nested)'.
        - Base Case 1: If 'nested' is completely empty, return an empty list [].
        - Take the first item from the list ('first = nested[0]') and the rest of the list ('rest = nested[1:]').
        - Check if 'first' is itself a list:
            - If YES: Recursively flatten 'first' and glue it to the recursively flattened 'rest'.
            - If NO: Wrap 'first' in a tiny list [first] and glue it to the recursively flattened 'rest'.

STEP 2: Define the pure function 'group_by(items, key_fn)'.
        - Create a brand new, empty dictionary called 'grouped_dict'.
        - Loop through each 'item' in the 'items' list:
            - Determine its sorting key by running it through the custom function: 'key = key_fn(item)'.
            - If 'key' is not already a drawer in our dictionary:
                - Create an empty list for that drawer.
            - Append the 'item' into that drawer.
        - Return 'grouped_dict'.

STEP 3: Combine them in the main script.
        - Run 'flatten' on the crazy nested list of words to get a clean, flat list.
        - Pass that flat list to 'group_by' along with a tiny lambda function that grabs the first letter 'w[0]'.
        - Print the output safely from outside.
'''


# --- STEP 1: Pure Recursive Flatten (No for/while loops allowed) ---
def flatten(nested: list) -> list:
    """Recursively flattens any deeply nested list without using loops."""
    # Base Case: If the list is completely empty, we are done tracking this branch
    if not nested:
        return []
        
    # Split the list into the very first item and the remaining items
    first = nested[0]
    rest = nested[1:]
    
    # Recursive Case 1: If the first item is a list itself, break it open recursively
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
        
    # Recursive Case 2: If the first item is a normal element, save it and process the rest
    return [first] + flatten(rest)


# --- STEP 2: Pure Grouping Cabinet ---
def group_by(items: list, key_fn) -> dict:
    """Groups elements into a fresh dictionary using a custom rule function."""
    grouped_dict = {}
    
    for item in items:
        # Calculate the category drawer name using our higher-order parameter rule
        key = key_fn(item)
        
        # If the drawer doesn't exist yet, open it up
        if key not in grouped_dict:
            grouped_dict[key] = []
            
        # Place the item inside its correct drawer
        grouped_dict[key].append(item)
        
    return grouped_dict


# --- STEP 3: Main Combination Pipeline Execution ---
if __name__ == "__main__":
    # 1. Test basic example from prompt
    sample_numbers = [1, [2, [3, [4]], 5]]
    print(f"Flatten Numbers Example: {flatten(sample_numbers)}")
    
    # 2. Setup the combined challenge data
    nested_fruits = [["apple", "avocado"], ["banana"], [["cherry"]]]
    
    # Execution Step A: Flatten the nested word boxes completely
    flat_fruits = flatten(nested_fruits)
    print(f"Step A (Flattened List): {flat_fruits}")
    
    # Execution Step B: Group by the first character of each word using a lambda function shortcut
    # lambda w: w[0] means "given a word string 'w', extract index 0 character"
    grouped_fruits = group_by(flat_fruits, lambda w: w[0])
    
    print(f"Step B (Grouped Result): {grouped_fruits}")



'''answer to the bonus question'''
def group_by_recursive(items: list, key_fn) -> dict:
    """Bonus recursive group_by implementation with zero loops."""
    # Base Case: If there are no items left, return a fresh empty dictionary
    if not items:
        return {}
        
    first = items[0]
    # Recursively get the sorted dictionary of all the REMAINING items first
    result_dict = group_by_recursive(items[1:], key_fn)
    
    # Determine the category key for our current first item
    key = key_fn(first)
    
    # Add our current item into the dictionary that bubbled up from the deeper levels
    if key in result_dict:
        # We create a shallow copy to stay perfectly pure and avoid mutating previous states
        result_dict[key] = [first] + result_dict[key]
    else:
        result_dict[key] = [first]
        
    return result_dict
