def reverse_string(text):
    return text[::-1]
print(reverse_string("wisdom"))
#this is the fastest and most pythonic way to reverse a string


def reverse_with_loop(text):
    reversed_str = ""

    for char in text:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_with_loop("racecar"))


def reverse_with_method(text):
    char_list = list(text)

    char_list.reverse()

    return "".join(char_list)
print(reverse_with_method('chinaza'))


def reverse_join(text):
    return "".join(reversed(text))
print(reverse_join('daniel'))