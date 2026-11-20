def count_vowels(s: str) -> int:
    vowels = "AEIOUaeiou"
    count = ''
    for vowel in s:
    # for vowel in s.lower():
        if vowel in vowels:
        # if vowel in 'aeiou':
            count += vowel
    return len(count)

'''instead of hardcoding the vowels, we can add the .lower() to the parameter that is inside the function so that it automatically covert the argument passed to lower to match the vowel we hard coded

like..... for vowel in s.lower()'''
    

s = "Hello World"
print(count_vowels(s))


def count_vowels(s: str) -> int:
    v = 'AEIOUaeiou'
    t = 0
    for vowel in s:
        if vowel in v:
            t += 1
    return t

s = "PYTHON programming"  
print(count_vowels(s))