input_list = [10, 20, 10, 30, 20]
seen_items = []
duplicate_items = []

for item in input_list:
    item_already_seen = False
    for seen in seen_items:
        if item == seen:
            item_already_seen = True
            break

    if item_already_seen == True:
        already_in_duplicates = False
        for dup in duplicate_items:
            if item == dup:
                already_in_duplicates = True
                break

        if already_in_duplicates == False:
            duplicate_items.append(item)
    else:
        seen_items.append(item)

print(duplicate_items)




'''this is for the optional stretch'''
input_list = [10, 20, 10, 30, 20]

# Dictionary to track counts of ALL items from the input list
item_counts = {}

for item in input_list:
    # Check if the item is already a key in our dictionary
    if item in item_counts:
        item_counts[item] += 1  # Increment its count by 1
    else:
        item_counts[item] = 1   # Initialize its count at 1

# Dictionary to store ONLY the items that appeared more than once
duplicate_dictionary = {}

for item in input_list:
    # If the item appeared more than once and isn't in our duplicate dictionary yet
    if item_counts[item] > 1 and item not in duplicate_dictionary:
        duplicate_dictionary[item] = item_counts[item]

print(duplicate_dictionary)
