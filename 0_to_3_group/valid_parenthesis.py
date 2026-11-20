# def is_valid_parentheses(s: str) -> bool:
#     valid = True
#     opening_parentheses = []
#     for char in s:
#         if char == '(' or char == '{' or char == '[':
#             opening_parentheses.append(char)
#         elif char == ')' or char == '}' or char == ']':
#             if len(opening_parentheses) == 0:
#                 valid = False
            
#             opened = opening_parentheses.pop()
#             if 


def is_valid_parentheses(s: str) -> bool:
    stack = []
    opening_parentheses = {"(", "[", "{"}
    closing_parentheses = {")", "]", "}"}
    for parentheses in s:
        if parentheses in opening_parentheses:
            stack.append(parentheses)
        elif parentheses in closing_parentheses:
            if len(stack) == 0:
                return False
            last_opened = stack.pop()

            if (parentheses == ")" and last_opened != "(") or (parentheses == "]" and last_opened != "[") or (parentheses == "}" and last_opened != "{"):
                return False
    return len(stack) == 0

'''now there is a way to make the comparison at the very end of this code shorter. this is by changing the opening_prarentheses and the closing_parentheses to a string instead of set so that they can have index and be ordered unlike set that is unordered and doesn't have index'''

'''this method is the slowest!!!'''

def is_valid_parenthesis(s: str) -> bool:
    stack = []
    opening_parentheses = '({['
    closing_parentheses = ')}]'
    for parentheses in s:
        if parentheses in opening_parentheses:
            stack.append(parentheses)
        elif parentheses in closing_parentheses:
            if len(stack) == 0:
                return False
            last_opened = stack.pop()

            if opening_parentheses.index(last_opened) != closing_parentheses.index(parentheses):
                return False
    return len(stack) == 0



'''this is another method to do the valid parentheses check using the dictionary to check for the the key-value pairs'''

def is_valid_parentheses(s: str) -> bool:
    stack = []
    # Maps each closing bracket to its matching opening bracket
    pairs = {")": "(", "]": "[", "}": "{"}
    
    for parentheses in s:
        if parentheses in pairs.values():   # Checks '(', '[', '{'
            stack.append(parentheses)
        elif parentheses in pairs:          # Checks ')', ']', '}'
            if len(stack) == 0:
                return False
            last_opened = stack.pop()
            
            # Super short comparison!
            if last_opened != pairs[parentheses]:
                return False
                
    return len(stack) == 0



def is_valid_parentheses(s: str) -> bool:
    stack = []
    opening_parentheses = {"(", "[", "{"}
    pairs = {")": "(", "]": "[", "}": "{"}
    
    for parentheses in s:
        if parentheses in opening_parentheses:
            stack.append(parentheses)
        elif parentheses in pairs:
            if len(stack) == 0 or stack.pop() != pairs[parentheses]:
                return False
                
    return len(stack) == 0




             
        
