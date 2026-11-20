def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9"

def is_palindrome(text: str) -> bool:
    left = 0
    right = len(text) - 1

    while left < right:
        if not is_letter(text[left]):
            left += 1
            continue

        if not is_letter(text[right]):
            right -= 1
            continue

        char_l = text[left]
        char_r = text[right]

        '''Why the code checks for Capital Letters ('A' <= char_l <= 'Z')
In computer memory, every character has a secret number code (called an ASCII value).
• Capital letters run from 65 (A) to 90 (Z)
• Small letters run from 97 (a) to 122 (z)
Notice that the difference between a capital letter and its small version is exactly 32 (for example, 65 ('A') + 32 = 97 ('a')).'''
        if "A" <= char_l <= "Z":
            char_l = chr(ord(char_l) + 32)
        if "A" <= char_r <= "Z":  
            char_r = chr(ord(char_r) + 32)

        if char_l != char_r:
            return False
        
        left += 1
        right -= 1
    return True
test_1 = "was it a car or a cat i saw?"
test_2 = "Hello, World!"        

print(f"Input: {test_1} -> Output: {'Palindrome' if is_palindrome(test_1) else 'Not a palindrome'}")
print(f"Input: {test_2} -> Output: {'Palindrome' if is_palindrome(test_2) else 'Not a palindrome'}")




# --- BONUS QUESTION FOR 1 ---
def is_palindrome_recursive(text: str, left: int, right: int) -> bool:
    '''Recursive palindrome check without loops'''
    if left >= right:
        return True

    # Fixed: Now recursively calls itself (is_palindrome_recursive)
    if not is_letter(text[left]):
        return is_palindrome_recursive(text, left + 1, right)

    if not is_letter(text[right]):
        return is_palindrome_recursive(text, left, right - 1)
    
    char_l = chr(ord(text[left]) + 32) if 'A' <= text[left] <= 'Z' else text[left]
    char_r = chr(ord(text[right]) + 32) if 'A' <= text[right] <= 'Z' else text[right]

    if char_l != char_r:
        return False
        
    return is_palindrome_recursive(text, left + 1, right - 1)


# List of test entries: (string_to_test, expected_boolean_output, description)
recursive_tests = [
    ("Was it a car or a cat I saw?", True, "Standard sentence with spaces & mixed casing"),
    ("Hello, World!", False, "Standard non-palindrome text"),
    ("A man, a plan, a canal: Panama.", True, "Heavy punctuation and mixed casing"),
    ("No 'x' in Nixon", True, "Contains single quotes and spaces"),
    ("12321", True, "Pure numbers"),
    ("123421", False, "Non-palindrome numbers"),
    ("Never odd or even.", True, "Ends with a period"),
    ("", True, "Empty string (technically reads the same both ways)"),
    ("A", True, "Single character string")
]

print("--- Running Recursive Palindrome Tests ---")
for text, expected, description in recursive_tests:
    # We initialize the recursive pointers at 0 and the final index of the string
    result = is_palindrome_recursive(text, 0, len(text) - 1)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    
    print(f"{status} | Input: '{text}'")
    print(f"       Description: {description}")
    print(f"       Expected: {expected} | Got: {result}\n")

