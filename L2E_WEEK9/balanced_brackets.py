def is_balanced(text:str) -> bool:
    stack = []
    brackets_map = {")": "(", "]": "[", "}": "{"}
    # openers = { "(", "[", "{"}
    openers = set(brackets_map.values())

    for char in text:
        if char in openers:
            stack.append(char)
        elif char in brackets_map:
            if not stack or stack[-1] != brackets_map[char]:
                return False
            stack.pop()
            
    return len(stack) == 0



# Bonus
def max_depth(text: str) -> int:
    current_depth = 0
    deepest = 0
    openers = "([{"
    closers = ")]}"

    for char in text:
        if char in openers:
            current_depth += 1
            if current_depth > deepest:
                deepest = current_depth
        elif char in closers:
            current_depth -= 1

    return deepest


print(is_balanced("(a + b) * [c - d]"))  # True
print(is_balanced("{[()]}")   )           # True
print(is_balanced("([)]")    )            # False
print(is_balanced("((")  )                # False
print(is_balanced("}{")   )               # False
print(is_balanced(""))  
print('============')
print(is_balanced('{123] *[}'))