def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib_list = [0, 1, ]
    while len(fib_list) < n:
        next_sum = fib_list[-1] + fib_list[-2]
        fib_list.append(next_sum)
    return fib_list   
n = 10
print(fibonacci(n))

'''the above code is to get the fibonacci of the number entered. like if the number is 10, there should be a total of 10 fib numbers in the list that is going to be outputed'''


#now what if i want the fib number that will be generated to stop at the last two sum that will be equal to the number that is inputed?. this is the code for such a program
def fib_stop_at_last_two_sum(n: int) -> list[int]:
    if n < 0:
        return []
    if n == 0:
        return [0]

    sequence = [0, 1]
    while True:
        next_sum = sequence[-1] + sequence[-2]
        if next_sum > n:
            break
        sequence.append(next_sum)
    return sequence

n = 10
print('*' * 10)
print(fib_stop_at_last_two_sum(n))