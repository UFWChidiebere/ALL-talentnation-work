# def fizzbuzz(n):
#     if n == 0:
#         return []
#     for i in range(1, n):
#         if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#             return "FizzBuzzBazz"
#         elif i % 3 == 0:
#             return "Fizz"
#         elif i % 5 == 0:
#             return "Buzz"
#         elif i % 7 == 0:
#             return "Bazz"
#         else:
#             return i
# fizzbuzz(3)
# print(fizzbuzz(15))
# print(fizzbuzz(21))
# print(fizzbuzz(35))
# print(fizzbuzz(105))
# print(fizzbuzz(4))
# print(fizzbuzz(0))
#this first version of fizzbuzz_plus is not correct because it only returns the first value that meets the condition, instead of returning a list of all values from 1 to n. The correct implementation should append each value to a result list and return that list at the end.

def fizzbuzz_plus(n):
    if n == 0:
        return []
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
            result.append("FizzBuzzBazz")
        if i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 7 == 0:
            result.append("Bazz")
        else:
            result.append(i)
    return result

# print(fizzbuzz_plus(3))
# print('--' * 10)
# print(fizzbuzz_plus(15))
# print('--' * 10)
# print(fizzbuzz_plus(21))
# print('--' * 10)
# print(fizzbuzz_plus(35))
# print('--' * 10)
# print(fizzbuzz_plus(105))
# print('--' * 10)
# print(fizzbuzz_plus(4))
# print('--' * 10)
# print(fizzbuzz_plus(0))

#this version of fizzbuzz_plus is correct because it returns a list of all values from 1 to n, with the appropriate substitutions for multiples of 3, 5, and 7.

def fizzbuzz_plus(n):
    if n == 0:
        return []
    result = []
    for i in range(1, n + 1):
        current_word = ""
        if i % 3 == 0:
            current_word += "Fizz"
        if i % 5 == 0:
            current_word += "Buzz"
        if i % 7 == 0:  
            current_word += "Bazz"
        if current_word == "":
            current_word = str(i)
        result.append(current_word)
    return result   
print(fizzbuzz_plus(3))
print('--' * 10)
print(fizzbuzz_plus(15))
print('--' * 10)
print(fizzbuzz_plus(21))
print('--' * 10)
print(fizzbuzz_plus(35))
print('--' * 10)
print(fizzbuzz_plus(105))
print('--' * 10)
print(fizzbuzz_plus(4))
print('--' * 10)
print(fizzbuzz_plus(0))

#this is the correct implementation of fizzbuzz_plus, which returns a list of all values from 1 to n, with the appropriate substitutions for multiples of 3, 5, and 7.
