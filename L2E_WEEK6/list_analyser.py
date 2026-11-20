number = [12, 5, 27, 8, 14, 27, 3]

smallest_val = number[0]
smallest_index = 0
largest_val = number[0]
largest_index = 0
total_sum = 0
count = 0

for index in range(0, len(number)):
    current_num = number[index]

    total_sum += current_num
    count += 1

    if current_num < smallest_val:
        smallest_val = current_num
        smallest_index = index

    if current_num > largest_val:
        largest_val = current_num
        largest_index = index

average = total_sum / count
above_average_count = 0

for current_num in number:
    if current_num > average:
        above_average_count += 1

print(f"Smallest: {smallest_val} (at index {smallest_index})")
print(f"Largest: {largest_val} (at index {largest_index})")
print(f"Total: {total_sum}")
print(f"Average: {average:.2f}") 
print(f"Numbers above average: {above_average_count}")






