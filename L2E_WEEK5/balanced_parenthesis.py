text = '(a+b) * (c-d)'
counter = 0 
is_balanced = True

for char in text:
    if char == '()':
        counter += 1
    elif char == ')':
        counter -= 1

    if counter < 0:
        is_balanced = False
        break
if is_balanced and counter == 0:
    print('Balanced')
else:
    print('Not Balanced')
    