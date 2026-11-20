def is_palindrome(sentence):
    left = 0
    right = len(sentence) - 1
    
    while left < right:
        while left < right and not sentence[left].isalnum():
            left += 1
        while left < right and not sentence[right].isalnum():
            right -= 1

        if sentence[left].casefold() != sentence[right].casefold():
            print("Output: Not a palindrome")
            return False

        left += 1
        right -= 1

    print("Output: Palindrome")
    return True

is_palindrome("was it a car or a cat i saw?")
is_palindrome("Hello, World!")

















"""Pointers Setup: Initialize left = 0 and right = len(sentence)-1

Two-Pointer Convergence: Run a loop while left < right.

Skip Bad Characters: Inside the loop, run sub-loops to check if the character at left or right is alphanumeric. If not, increment left or decrement right dynamically without processing them.

Case-Insensitive Match: Convert both characters to lowercase manually using .lower() and check if they match. If they don't, return False immediately.

Advance: Move both pointers inward (left += 1, right -= 1)."""