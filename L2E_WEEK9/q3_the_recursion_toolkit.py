#Base Case: n==0 : this is the basecase
#Reduction: n // 10 - strips off the rightmost digit, processing one digit per call
def digit_sum(n: int) -> int:
    if n == 0: 
        return 0
    return (n % 10) + digit_sum(n // 10)

#Base Case: text == ''
#Reduction: text[1:] slices away the first letter, making the string shorter
def reverse_text(text: str) -> str:
    if text == '':
        return ''
    return reverse_text(text[1:]) + text[0]

#Base Case: text == ''
#Reduction: text[1:] shift past the checked  first letter to process the rest
def count_char(text: str, ch: str) -> str:
    if text == '':
        return 0
    c_match = 1 if text[0] == ch else 0 # ternary operator
    # match = int(text[0] ==ch) # boolean typecasting
    # match = (text[0] == ch) * 1 # direct math (implicit version)

    # c_match = 0
    # if text[0] == ch:
        # c_match = 1
    # elif text[0] != ch:
        # c_match = 0
    return c_match + count_char(text[1:], ch)


#Base Case: exp == 0
#Reduction: exp - 1. Drops the exponent value by 1 towards 0
def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    return base * power(base, exp -1)


# Bonus
# For exp = 1000, power() makes 1,001 calls, whereas power_fast() halves exp
# each time and makes only about 11 calls.
def power_fast(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power_fast(base, exp // 2)
        return half * half
    return base * power_fast(base, exp - 1)




print(digit_sum(1234) )                 # 10
print(digit_sum(0) )                    # 0
print(reverse_text("abc"))              # "cba"
print(reverse_text("") )                # ""
print(count_char("banana", "a"))        # 3
print(power(2, 10) )                    # 1024
print(power(5, 0)  )                    # 1
