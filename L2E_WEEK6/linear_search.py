values = [14, 7, 22, 9, 7, 31, 7, 5]
target = 22
matching_indices = []

for index in range(0, len(values)):
    if values[index] == target:
        matching_indices.append(index)

match_count = len(matching_indices)
if match_count == 0:
    print('Target not found')
else:
    first_occurence = matching_indices[0]
    last_occurence = matching_indices[match_count - 1]


print(f"Target: {target} → Found at indices: {matching_indices} | Count: {match_count} | First: {first_occurence} | Last: {last_occurence}")
