def is_palindrome(s: str) -> bool:
    not_case_sensitive = s.lower()
    reversed = ''

    non_alpha = ".' ',';:?/!~`@#$%^&*()_+-=[]|"
    for x in non_alpha:
        if x in not_case_sensitive:
            not_case_sensitive = not_case_sensitive.replace(x, "")
    for char in not_case_sensitive:
        reversed = char + reversed
    if reversed == not_case_sensitive:
        return 'Paloindrome'
    else:
        return False

s = "A man, a plan, a canal: Panama."
s1 = "racecar"
print(is_palindrome(s))
print(is_palindrome(s1))



'instead of manually building the special characters, one can use python built in method that is called the isalnum()'
def is_palindrome(s: str) -> bool:
    cleaned = "".join([char.lower() for char in s if char.isalnum()])
    return cleaned == cleaned[::-1]




'''also one can import re and use the sub() and also import string and use the translate(str.maketrans and the string.punctuation)'''


"""there are just different ways/methods to kill a bird..... there's also the tracking method that will have to be checking/comparing the left hand side to the right hand side to see if they are of the same ASCII value"""