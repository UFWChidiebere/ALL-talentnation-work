numbers = [12, 5, 27, 8, 14]
# numbers = [50, 1, 4, 100, 1000, 0]

smallest = numbers[0]
largest = numbers[0]
total = 0

for num in numbers:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num
    
    total += num

average = total / len(numbers)
print(average)

print(f'The Smallest Number is:  {smallest}')
print(f'The Largest Nuumber is:  {largest}')
print(f'The Total Is:  {total}')
print(f'The Average Is:  {average}')