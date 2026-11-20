'''STEP 1: Define the higher-order function 'make_shifter(shift)'.
        - Create an inner function 'shifter(ch)'.
            - Check if 'ch' is a small letter ('a' to 'z'):
                - Find its position relative to 'a', add the shift amount, wrap it around using % 26, and turn it back into a character.
            - Check if 'ch' is a capital letter ('A' to 'Z'):
                - Find its position relative to 'A', add the shift amount, wrap it around using % 26, and turn it back into a character.
            - If it is not a letter (space, digit, punctuation), return 'ch' exactly as it is.
        - Return the 'shifter' inner function itself (do not call it, just return the tool!).

STEP 2: Set up the main runtime block to interact with the user safely outside the functions.
        - Ask the user for their message string.
        - Ask the user to input the mode: 'encrypt' or 'decrypt'.
        - Ask the user for the shift integer value.
        - If the mode is 'decrypt', multiply the shift value by -1 to reverse the alphabet direction.

STEP 3: Fire up the pipeline.
        - Call 'make_shifter(calculated_shift)' to build your custom conversion tool.
        - Use 'map(custom_tool, message)' to transform the text sequentially.
        - Combine the resulting character array back into a unified string using "".join().
        - Print the output.
'''

# --- STEP 1: The Higher-Order Function Factory ---
def make_shifter(shift: int):
    """Returns a tailored function that shifts a single character by a set amount."""
    
    # This inner function remembers the 'shift' variable from outside (this is called a Closure)
    def shifter(ch: str) -> str:
        # Check for lowercase letters
        if 'a' <= ch <= 'z':
            # 1. ord(ch) - ord('a') finds the 0-25 index of the letter
            # 2. adding the shift applies the secret code movement
            # 3. % 26 ensures wrap-around logic (e.g., index 26 drops back to 0)
            return chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            
        # Check for uppercase letters
        elif 'A' <= ch <= 'Z':
            return chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            
        # Leave numbers, spaces, and symbols completely alone
        return ch

    # Return the inner function code block itself as a reusable tool
    return shifter


# --- STEPS 2 & 3: Main Interface & Processing Assembly Line ---
if __name__ == "__main__":
    print("--- Functional Caesar Cipher System ---")
    
    # 1. Gather all inputs outside our pure functions
    user_message = input("Enter your message: ")
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    shift_amount = int(input("Enter shift value (number): "))

    # 2. Adjust shift direction if decrypting
    if mode == "decrypt":
        shift_amount = -shift_amount

    # 3. Call the factory to get our custom character manipulator tool
    my_custom_shifter = make_shifter(shift_amount)

    # 4. Use map to pass every single letter through our custom shifter function
    # map() yields characters one by one, so we join them back together into a single string
    processed_message = "".join(map(my_custom_shifter, user_message))

    # 5. Output the result cleanly
    print(f"\nResulting Message: {processed_message}")


'''NOTE:
the bonus requirements is embedded/included inside the code above'''