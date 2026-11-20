def factorial(n: int) -> int:
    if n < 0:
        return 'Can"t find Factorial of negative numbers'
    if n == 0 or n == 1:
        return 1
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(5))
'''this is the logic i am able to impliment with the help of AI- to complete it'''

'''this is the recursive case code  for the same task'''
def factorial_recursive(n):
    #the base case that will help to stop the recursive call
    if n == 0 and n == 1:
        return 1

    return n * factorial_recursive(n - 1)


'''this is the for-loop solution'''
def factorial_loop(n):
    result = 1
    # Loops from 1 up to n
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_loop(5))  # Output: 120
