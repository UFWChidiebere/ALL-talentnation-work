values = [14, 7, 22, 9, 7, 31]
target = 31

found_index = -1

for i in range(len(values)):
    if values[i] == target:
        found_index = i
        break

    if found_index != -1:
        print(f'Target found at index {found_index}')
    else:
        print('Target not found')
