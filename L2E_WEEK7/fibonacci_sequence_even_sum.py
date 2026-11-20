def solve_fibonacci_challenge(N):
    if N <= 0:
        return
    sequence = []
    a = 0
    b = 1
    even_sum = 0

    count = 0
    while count < N:
        sequence.append(a)  
        if a % 2 == 0:       
            even_sum += a

        '''this is where the swap state happens'''
        next_val = a + b
        a = b
        b = next_val
        count += 1

    reversed_str = ''
    i = len(sequence) - 1
    while i >= 0:
        if i == 0:
            reversed_str += str(sequence[i])
        else:
            reversed_str += str(sequence[i]) + ', '
        i = i - 1
        
    print(f"Sequence: {sequence}")
    print(f'Even Sum: {even_sum}')
    print(f'Reversed: {reversed_str}')


solve_fibonacci_challenge(8)
