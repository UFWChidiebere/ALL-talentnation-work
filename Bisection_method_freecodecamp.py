def square_root_bisection(number, tolerance=1e-7, max_iterations=100):
    if  number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number 

    low = 0
    if number < 1:
        high = 1
    else:
        high = number

    for iteration in range(max_iterations):
        mid = (low + high) / 2

        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
        if mid * mid > number:
            high = mid
        else:
            low = mid
    print(f"Failed to converge within {max_iterations} iterations")
    return None




"""this is the psuedocode for the task above


STEP 1: Define a function named 'square_root_bisection' with three parameters:
        - number
        - tolerance (give it a default value, e.g., 1e-7)
        - max_iterations (give it a default value, e.g., 100)

STEP 2: Handle immediate edge cases and errors:
        - IF number < 0:
            Raise ValueError with message: "Square root of negative number is not defined in real numbers"
        - IF number == 0 OR number == 1:
            Print "The square root of [number] is [number]"
            Return number

STEP 3: Set up boundaries for the search interval:
        - Set low boundary = 0
        - IF number < 1:
            Set high boundary = 1  (Because square root of 0.25 is 0.5, which is greater than 0.25)
        - ELSE:
            Set high boundary = number

STEP 4: Run a loop tracking the current iteration count up to max_iterations:
        - Compute the middle point: mid = (low + high) / 2
        
        - Check if the size of our interval (high - low) is within the acceptable tolerance:
            IF (high - low) <= tolerance:
                Print "The square root of [number] is approximately [mid]"
                Return mid
                
        - Adjust the search boundaries for the next guess:
            IF mid * mid > number:
                high = mid  (Our guess was too high)
            ELSE:
                low = mid   (Our guess was too low)

STEP 5: If the loop finishes all iterations without meeting the tolerance condition:
        - Print "Failed to converge within [max_iterations] iterations"
        - Return None
"""


