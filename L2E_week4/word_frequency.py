# --- STEP 1: Word Cleaning Helper ---
def clean_and_lowercase(word: str) -> str:
    """Manually removes basic punctuation and converts characters to lowercase."""
    cleaned = ""
    for ch in word:
        # Manually skip basic punctuation marks
        if ch == ',' or ch == '.' or ch == '!' or ch == '?':
            continue
            
        # Manually convert uppercase characters to lowercase
        if 'A' <= ch <= 'Z':
            cleaned += chr(ord(ch) + 32)
        else:
            cleaned += ch
            
    return cleaned


# --- STEP 2: The Core Counting Function ---
def count_words(words: list[str]) -> dict[str, int]:
    """Pure function that builds a fresh word frequency dictionary map."""
    freq_map = {}
    
    for word in words:
        cleaned_word = clean_and_lowercase(word)
        
        # If the word isn't blank, update our tracking sheet
        if cleaned_word != "":
            if cleaned_word in freq_map:
                freq_map[cleaned_word] += 1
            else:
                freq_map[cleaned_word] = 1
                
    return freq_map


# --- STEP 3: Finding the Most Frequent Word ---
def most_frequent(freq: dict[str, int]) -> str:
    """Finds the single most frequent word without using max() or sorting."""
    top_word = None
    max_count = -1
    
    for word, count in freq.items():
        if count > max_count:
            max_count = count
            top_word = word
            
    return top_word


# --- STEP 4: Main Program Execution (Printing strictly outside) ---
input_paragraph = "Python is fun, and Python is powerful!"

# Break the paragraph into a list of words by spaces
# This changes "Python is fun," into ['Python', 'is', 'fun,', ...]
words_list = input_paragraph.split(" ")

# Generate our frequency dictionary map
word_counts = count_words(words_list)

# Find the highest occurring word record
target_word = most_frequent(word_counts)

# Output the metrics cleanly
print(f"Most frequent word: {target_word} ({word_counts[target_word]})")



'''the psudocde for the code above

STEP 1: Define a helper function to clean a single word.
        - Create an empty string 'cleaned'.
        - Loop through every character in the word:
            - If the character is a comma, period, exclamation mark, or question mark, skip it.
            - If it is a capital letter, manually turn it into a small letter (or use .lower() since we are processing a single character loop, but manual math or .lower() works here).
            - Add the valid character to 'cleaned'.
        - Return the 'cleaned' word.

STEP 2: Define the pure function 'count_words(words_list)'.
        - Create a brand new, empty dictionary called 'freq_map'.
        - Loop through every word in the provided words_list:
            - Clean the word using our helper function from Step 1.
            - If the cleaned word is empty (like if a lone punctuation mark was removed), ignore it.
            - If the cleaned word is ALREADY in our 'freq_map' dictionary:
                - Add 1 to its current count.
            - Otherwise (if it's a brand new word):
                - Set its count to 1.
        - Return the 'freq_map' dictionary.

STEP 3: Define the pure function 'most_frequent(freq_dict)'.
        - Create a variable 'top_word' set to None.
        - Create a variable 'max_count' set to -1.
        - Loop through each word and its count inside the 'freq_dict' dictionary:
            - If the current count is greater than 'max_count':
                - Update 'max_count' to be this new count.
                - Update 'top_word' to be this word.
        - Return 'top_word'.

STEP 4: Run the main program.
        - Take the raw sentence string.
        - Break it into a list of words using string.split(" ").
        - Send that list to 'count_words' and save the returned dictionary.
        - Send that dictionary to 'most_frequent' and save the most popular word.
        - Print the final result completely outside the functions.
'''


'''the bonus question answer'''
from functools import reduce

def most_frequent_reduce(freq: dict[str, int]) -> str:
    """Bonus alternative using reduce instead of a manual for loop."""
    # This checks pairs of words and keeps the one with the higher count value
    return reduce(lambda acc, word: word if freq[word] > freq[acc] else acc, freq.keys())