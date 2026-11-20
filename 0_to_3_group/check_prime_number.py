# def is_prime(n: int) -> bool:
#     if n < 2:
#         return "Prime numbers starts from 2 (which is the is the first and the lowest prime number and the only even number in list of prime numbers) and anything lesser cannot be a prime number"

#     if n == 2:
#         return True

#     if n > 2 and n % 1 == n and n % n == 1:
#         return True
#     else:
#         return False 
    #this is the logic i wrote initially and it was totally wrong. i had to meet Lawrence to help me through and he came up with differnt things that can work
'''for the code above, this is the version that AI said should have been my code.....below'''
def is_prime_my_style(n: int):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True




def is_prime(n: int) -> bool:
    if n < 2:
        return "Prime numbers starts from 2 (which is the is the first and the lowest prime number and the only even number in list of prime numbers) and anything lesser cannot be a prime number"
    
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

n = 14
print(is_prime(n))

 
'''this code is fast(reduce time complexity by half) and it help skip even numbers so that it is only odd numbers that are prime numbers'''



'''this is another code that doesn't skip even numbers so it checks for even and odd numbers that are prime numbers'''
def is_prime(n: int) -> bool:
    if n < 2:
        return "Prime numbers starts from 2 (which is the is the first and the lowest prime number and the only even number in list of prime numbers) and anything lesser cannot be a prime number"
    
    if n == 2:
        return True
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 15
n1 = 11
n2 = 49
n4 = 8
print(is_prime(n))
print(is_prime(n1))
print(is_prime(n2))
print(is_prime(n4))



'''6k +/- 1'''
def is_prime_6k(n: int) -> bool:
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


n = 15
n1 = 11
print(is_prime_6k(n))
print(is_prime_6k(n1))
# print(is_prime(n2))
# print(is_prime(n4))
