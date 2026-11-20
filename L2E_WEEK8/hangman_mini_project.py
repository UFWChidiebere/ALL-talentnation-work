def play_hangman(word, guesses, max_attempts):
    guessed_letters = []
    wrong_guesses = []
    
    # Process guesses one by one simulating the timeline of the game
    for guess in guesses:
        if guess in guessed_letters:
            continue  # Ignore repeated guesses entirely
            
        guessed_letters.append(guess)
        
        if guess not in word:
            wrong_guesses.append(guess)
            
        # Dynamically evaluate the current word reveal state
        display = "".join([char if char in guessed_letters else "_" for char in word])
        
        # Check instant termination criteria
        if "_" not in display:
            return ("won", display, wrong_guesses)
        if len(wrong_guesses) >= max_attempts:
            return ("lost", display, wrong_guesses)
            
    # Fallback state if guesses exhaust before win/loss condition met
    final_display = "".join([char if char in guessed_letters else "_" for char in word])
    return ("playing", final_display, wrong_guesses)


# --- Bonus Implementation ---
def main():
    secret_word = "developer"
    max_lives = 4
    history_of_guesses = []
    
    print("--- Welcome to Hangman! ---")
    
    while True:
        status, display, wrong_guesses = play_hangman(secret_word, history_of_guesses, max_lives)
        
        print(f"\nWord: {display}")
        print(f"Incorrect guesses: {wrong_guesses}")
        print(f"Attempts remaining: {max_lives - len(wrong_guesses)}")
        
        if status == "won":
            print("Congratulations! You won the game! 🎉")
            break
        elif status == "lost":
            print(f"Game Over! You ran out of attempts. The word was '{secret_word}'. 💀")
            break
            
        user_input = input("Guess a letter: ").strip().lower()
        
        if len(user_input) != 1 or not user_input.isalpha():
            print("Please enter exactly one single alphabetic letter.")
            continue
            
        history_of_guesses.append(user_input)

# Test cases verification
print(play_hangman("apple", ["a", "z", "p", "l", "e"], 3))   # ("won", "apple", ["z"])
print(play_hangman("python", ["a", "b", "c", "d"], 3))       # ("lost", "______", ["a", "b", "c"])
print(play_hangman("python", ["p", "p", "y"], 5))            # ("playing", "py____", [])
print(play_hangman("a", [], 3))                              # ("playing", "_", [])
