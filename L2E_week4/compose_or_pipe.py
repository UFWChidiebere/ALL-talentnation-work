'''STEP 1: Define the four pure string helper functions.
        - clean_strip(text): Returns text with outer spaces removed.
        - clean_lower(text): Returns text converted to lowercase.
        - remove_vowels(text): Creates a new string skipping any a,e,i,o,u letters, then returns it.
        - manual_reverse(text): Loops backward from the last index to 0, builds a flipped string, and returns it.

STEP 2: Define 'compose(f, g)'.
        - Return a new inner function that takes x, runs g(x) first, then passes that result into f().

STEP 3: Define 'pipe(*funcs)'.
        - Return a new inner function 'piped_mach(x)' that takes a starting value:
            - Loop through each function in the 'funcs' tuple from left to right:
                - Overwrite x with the output of the current function applied to x (x = func(x)).
            - Return the final value of x.

STEP 4: Assemble the pipeline.
        - Create 'text_pipeline = pipe(clean_strip, clean_lower, remove_vowels, manual_reverse)'.
        - Feed the string "  Hello World  " into 'text_pipeline' and print the output.
'''

# --- STEP 1: The Four Pure Text Cleaners ---

def clean_strip(text: str) -> str:
    """Removes leading and trailing whitespace."""
    # Using Python's built-in .strip() is allowed as it is a pure operation
    return text.strip()

def clean_lower(text: str) -> str:
    """Converts the string to lowercase."""
    return text.lower()

def remove_vowels(text: str) -> str:
    """Loops through text and filters out all vowels."""
    result = ""
    vowels = "aeiouAEIOU"
    for char in text:
        if char not in vowels:
            result += char
    return result

def manual_reverse(text: str) -> str:
    """Flips a string backward manually using a loop (No [::-1] or .reverse())."""
    reversed_str = ""
    # Loop backwards from the last index down to 0
    for i in range(len(text) - 1, -1, -1):
        reversed_str += text[i]
    return reversed_str


# --- STEP 2: The Compose Function (Right-to-Left) ---
def compose(f, g):
    """Combines two functions so that f(g(x)) is evaluated."""
    def composed_fn(x):
        return f(g(x))
    return composed_fn


# --- STEP 3: The Pipe Function (Left-to-Right Assembly Line) ---
def pipe(*funcs):
    """Accepts any number of functions and runs them sequentially on an input."""
    def piped_machine(x):
        # Pass the input x down the line, modifying it function by function
        current_value = x
        for func in funcs:
            current_value = func(current_value)
        return current_value
        
    return piped_machine


# --- STEP 4: Main Program Execution ---
if __name__ == "__main__":
    # Test the basic example from the prompt
    add_one = lambda x: x + 1
    double  = lambda x: x * 2
    
    print(f"Compose Example (Expected 11): {compose(add_one, double)(5)}")
    print(f"Pipe Example (Expected 12): {pipe(add_one, double)(5)}")
    
    # Build our custom text assembly line pipeline
    text_pipeline = pipe(clean_strip, clean_lower, remove_vowels, manual_reverse)
    
    # Process the sample string
    input_string = "  Hello World  "
    output_string = text_pipeline(input_string)
    
    print(f"\nOriginal Input: '{input_string}'")
    print(f"Pipeline Output: '{output_string}'") 
    # Logic trace: "  Hello World  " -> "Hello World" -> "hello world" -> "hll wrld" -> "dlrw llh"


'''answer to the bonus question'''
def manual_reverse_recursive(text: str) -> str:
    """Bonus recursive reverse function with zero loops."""
    # Base Case: If the string is empty or a single letter, it's already reversed!
    if len(text) <= 1:
        return text
        
    # Recursive Case: Take the last character and glue it to the front of 
    # whatever comes back from reversing the rest of the string.
    return text[-1] + manual_reverse_recursive(text[:-1])
