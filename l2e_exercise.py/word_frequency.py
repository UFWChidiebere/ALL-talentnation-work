sentence = input("input: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Move this print out here so it only displays ONCE
print("\nOutput:")

# Fix the spacing here to keep the code clean
for word, count in word_count.items():
    print(f"{word}: {count}")


"""this code above is good however, it does not tackle the optional stretch in the exercise"""


"""the two code below tackle the optional stretch"""

"""code 1"""
sentence = input("input: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    cleaned_word = word.strip(".,!?;:\"()")
    
    if cleaned_word:  # Makes sure the word isn't blank
        # Your awesome .get() logic dynamically updates the dictionary
        word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1

print("\nOutput:")
for word, count in word_count.items():
    print(f"{word}: {count}")


"""code 2"""

sentence = input("input: ")
words = sentence.lower().split()
word_count = {}

for word in words:
    # Clean punctuation from the left and right edges of the word
    cleaned_word = word.strip(".,!?;:\"()")
    
    # Skip if cleaning left us with an empty string (like a stray icon or symbol)
    if not cleaned_word:
        continue
        
    if cleaned_word in word_count:
        word_count[cleaned_word] += 1
    else:
        word_count[cleaned_word] = 1

print("\nOutput:")
for word, count in word_count.items():
    print(f"{word}: {count}")




"""now the codes that have functions defined in it"""

#code 1

def word_frequency(sentence):
    punctuation = ".,!?;:\"()"
    cleaned_sentence = ""
    
    # Normalize inputs manually to clean away punctuation traps
    for char in sentence.lower():
        if char not in punctuation:
            cleaned_sentence += char
        else:
            cleaned_sentence += " "  # Replace symbols with spaces to prevent stuck words
            
    words = cleaned_sentence.split()
    frequency_dict = {}
    
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
            
    return frequency_dict


#code 2
def alternative_word_frequency(sentence):
    raw_words = sentence.lower().split()
    frequency_dict = {}
    
    for word in raw_words:
        # Strip trailing or leading symbols from individual words
        cleaned_word = word.strip(".,!?;:\"()")
        
        if cleaned_word: # Skips empty string records
            frequency_dict[cleaned_word] = frequency_dict.get(cleaned_word, 0) + 1
            
    return frequency_dict


