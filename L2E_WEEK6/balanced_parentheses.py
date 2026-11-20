# input_string = "[(a + b) * {c - d}]"
input_string = input('Enter a string with brackets to check: ')
stack = []
is_balanced = True

for character in input_string:
    if character in ['(', '[', '{']:
        stack.append(character)
    elif character in [')', ']', '}']:
        if len(stack) == 0:
            is_balanced = False
            break

        last_opened = stack.pop()

        if character == ')' and last_opened != '(':
            is_balanced = False
            break
        if character == ']' and last_opened != '[':
            is_balanced = False
            break
        if character == '}' and last_opened != '{':
            is_balanced = False
            break

if len(stack) != 0:
    is_balanced = False
if is_balanced == True:
    print("Balanced")
else:
    print('Not balanced')

