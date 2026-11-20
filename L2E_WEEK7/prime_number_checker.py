def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i = i + 1
    return True

def solve_prime_challange(N):
    if is_prime(N):
        print(f"{N} is prime.")
    else:
        print(f"{N} is not prime.")

    prime_up_to_n = []
    prime_sum = 0
    current = 2

    while current <= N:
        if is_prime(current):
            prime_up_to_n.append(current)
            prime_sum = prime_sum + current
        current = current + 1

    print(f'Prime up to {N}: {prime_up_to_n}')
    print(f'Sum of primes: {prime_sum}')


solve_prime_challange(10)
print("-" * 20)
solve_prime_challange(7)
   