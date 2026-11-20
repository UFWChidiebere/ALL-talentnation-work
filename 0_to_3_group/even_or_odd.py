def is_even(n: int) -> bool:
    # for i in n:
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False
    
        
n1 = 4
n2 = 7

print(is_even(n1))
print(is_even(n2))




'''this is for the way of calling the various function in them'''
# 1. Function to find and return all even numbers
def find_evens(numbers):
    return [num for num in numbers if num % 2 == 0]

# 2. Function to find and return all odd numbers
def find_odds(numbers):
    return [num for num in numbers if num % 2 != 0]

# 3. Master function to call both and check truthy/falsy values
def check_numbers(list_of_numbers):
    evens = find_evens(list_of_numbers)
    odds = find_odds(list_of_numbers)
    
    # Check if evens list is truthy (not empty) or falsy (empty)
    if evens:
        print(f"🟢 Evens found (Truthy): {evens}")
    else:
        print("🔴 No evens found (Falsy)")
        
    # Check if odds list is truthy (not empty) or falsy (empty)
    if odds:
        print(f"🟢 Odds found (Truthy): {odds}")
    else:
        print("🔴 No odds found (Falsy)")
