def reverse_text(text):
    r_t = ''
    for char in text:
        r_t = char + r_t
    return r_t
print(reverse_text('wisdom'))