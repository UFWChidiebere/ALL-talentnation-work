'''STEP 1: Define the decorator function 'memoize(func)'.
        - Create a fresh, empty dictionary called 'cache' inside memoize.
          (Because of closures, this dictionary stays secretly alive in memory).
        - Define an inner wrapper function called 'wrapper(*args)'.
            - Check if the input arguments '*args' are already keys inside our 'cache' notebook.
            - If YES: Quietly return the pre-calculated value from the 'cache' instantly.
            - If NO: Let the original function run using 'func(*args)' and save its calculation answer.
            - Write that new answer down in the 'cache' dictionary: cache[args] = answer.
            - Return the fresh answer.
        - Return the 'wrapper' function itself.

STEP 2: Build the recursive Fibonacci function and tag it with '@memoize'.
        - Base Case: If n is less than 2, return n.
        - Recursive Case: Return fib(n - 1) + fib(n - 2).

STEP 3: Run the main program.
        - Call fib(35) and print the output. Watch how it prints almost instantly instead of taking minutes!
'''

# --- STEP 1: The Custom Memoization Decorator ---
def memoize(func):
    """A decorator that caches a function's results in a closure notebook."""
    # This dictionary lives inside the decorator's closure space (not global)
    cache = {}
    
    def wrapper(*args):
        # args is a tuple of the inputs. Since tuples are hashable, they can be dictionary keys!
        if args in cache:
            # If the guard already knows the answer, skip the function and return it instantly
            return cache[args]
            
        # If it's a new question, let the function run and calculate the result
        result = func(*args)
        
        # Save the result in our memory notebook before handing it back
        cache[args] = result
        return result
        
    return wrapper


# --- STEP 2: Applying the Decorator to Fibonacci ---
@memoize
def fib(n: int) -> int:
    """Calculates the nth Fibonacci number recursively."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# --- STEP 3: Main Program Execution (Testing Speed) ---
if __name__ == "__main__":
    print("--- Testing Memoized Fibonacci Speed ---")
    
    # Without @memoize, calculating fib(35) would make your computer lag for seconds.
    # With @memoize, it calculates over 9 million combinations instantly!
    target = 35
    output = fib(target)
    
    print(f"fib({target}) = {output} (Calculated instantly!)")



'''this is the answer to the bonus question'''

# --- Applying memoize to a Second Problem (Climbing Stairs) ---
@memoize
def count_ways(n: int) -> int:
    """Calculates how many unique ways you can climb n stairs taking 1 or 2 steps at a time."""
    # Base Cases
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
        
    # Recursive Case: The ways to reach step n is the sum of ways to reach (n-1) and (n-2)
    return count_ways(n - 1) + count_ways(n - 2)


# Let's run a heavy test for climbing 40 steps
stairs = 40
ways = count_ways(stairs)
print(f"\nDistinct ways to climb {stairs} stairs: {ways} (Calculated instantly using the same notebook guard!)")
