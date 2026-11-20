# def reverse_string(s: str) -> str:
#     return s[::-1]

# s = "python"
# print(reverse_string(s))

# def reverse_string(s: str) -> str:
#     # for char in s
#     reverse = ""
#     for ch in reversed(s):
#         reverse += ch
#     return reverse
# s = "Data Science"
# print(reverse_string(s))

'''this is done without using the slicing method and the in-built reversed function'''
def reverse_string(s: str) -> str:
    reversed = ''
    for char in s:
        reversed = char + reversed
    return reversed
s = "Data Science"
print(reverse_string(s))