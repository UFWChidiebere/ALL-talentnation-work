def is_palindrome(text):
    text = text.lower().strip().replace(" ", "")
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return " Not a palindrome"
        left += 1
        right -= 1
    return "Palindrome"

print(is_palindrome(" m A d A m"))




"""Alternative Method: Constructing the String Backwards (Loop Only)Because the prompt forbids using [::-1] or .reverse(), this alternative builds a completely separate reversed string by reading the original characters backwards, index by index."""
def alternative_palindrome(text):
    text = text.lower().strip()
    reversed_text = ""


    #iterate backwards using negative indices
    for i in range(1, len(text) + 1):
        reversed_text += text[-i]

    if text == reversed_text:
        return "Palindrome"
    return "Not a palindrome"




"""this is Nifemi's code however i have used AI to optimize it"""
def palindrome_halves(word):
    low_word = word.lower().strip()
    length = len(low_word)
    mid = length // 2
    
    # Left half goes up to the middle index
    left_half = low_word[:mid]
    
    # Right half starts at the middle (or past the middle character if the length is odd)
    if length % 2 == 0:
        right_half = low_word[mid:]
    else:
        right_half = low_word[mid + 1:]
        
    # Reverse the right half using a small manual loop (since [::-1] is banned)
    reversed_right = ""
    for char in right_half:
        reversed_right = char + reversed_right
        
    # If the left half matches the reversed right half, it's a palindrome!
    if left_half == reversed_right:
        return f"{word} is a palindrome"
    else:
        return f"{word} is not a palindrome"

# Test executions
print(palindrome_halves("deed"))     # Output: deed is a palindrome
print(palindrome_halves("racecar"))  # Output: racecar is a palindrome
print(palindrome_halves("python"))   # Output: python is not a palindrome


