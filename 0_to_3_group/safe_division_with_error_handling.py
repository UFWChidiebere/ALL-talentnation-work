'''EAFP- easier to ask for forgiveness than permission.'''
def safe_divide(a: float, b: float) -> float | str:
    try:
        result = a / b
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    # except ValueError:
    #     print('Error: Please enter a valid number for both the numerator(a) and the denominator(b).')
    except TypeError:
        print('Error: You provided an invalid data type. Both arguments must be numbers.')
    else:
        print(f"Success! The result from the divison is {result}")
        return result
    finally:
        print('Execution complete.')

output1 = safe_divide(10, 2)
print(f"Returned value 1: {output1}\n")

output2 = safe_divide(5, 0)
print(f"Returned value 2: {output2}\n")

print(' ' * 30)
safe_divide(10, 2)
safe_divide(5, 0)

print(' ' * 30)
safe_divide(10, 'o')


'''now in the first code you will see that i commented out a block of code coz to use it, the function parameters ot the place holders must be any then we will now have to convert it inside the code. that is the only way the ValueError block will work'''
def safe_divide(a: any, b: any) -> float | str:
    try:
        # Converting here allows Python to catch a ValueError if conversion fails
        num_a = float(a)
        num_b = float(b)
        result = num_a / num_b
    except ZeroDivisionError:
        return 'Error: Cannot divide by zero.'
    except ValueError:
        # This will now run if you pass something that can't be turned into a number
        return 'Error: Please enter a valid number for both the numerator(a) and the denominator(b).'
    else:
        print(f"Success! The result from the division is {result}")
        return result
    finally:
        print('Execution complete.')

# This works because "10" and "2" can be turned into floats
print(safe_divide("10", "2"))
print("-" * 20)

# This triggers the ValueError block!
print(safe_divide("hello", 2))




'''now let's try and solve the code with conditionals(LBYL- look before you leap)'''

def safe_divide(a: float, b: float) -> float | str:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return 'Error: You provided an invalid data type. Both arguments must be numbers.'

    if b == 0:
        return 'Error: Cannot divide by zero.'

    
    
    result = a / b
    return f'Success! The result from the division is {result}'
        

print(safe_divide(10, 2))       
print(safe_divide(5, 0))        
print(safe_divide("hello", 2))
