# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     for x in range(2, n):
#         if n % x == 0:
#             return False
        
#     return True

# print(is_prime(8))






def is_prime(f):
    if f < 2:
       return False
    
    if f == 2:
        return True
    for i in range(2, f):
        if f % i == 0:
            return False

    return True

print(is_prime(11))    