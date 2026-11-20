def word_frequency(paragraph):
    '''Manual stripping of basic punctuation'''
    cleaned_text = ""
    for char in paragraph:
        if char.isalnum() or char == " ":
            cleaned_text += char.lower()
            
    words = cleaned_text.split()
    frequency = {}
    
    '''Building frequency map manually'''
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    '''Find the most frequent word manually'''
    max_word = None
    max_count = 0
    for word, count in frequency.items():
        if count > max_count:
            max_count = count
            max_word = word
            
    print(f"Most frequent word: {max_word} ({max_count})")
    return max_word, max_count

























"""nitialize Maps: Create an empty dictionary frequency = {}.

Sanitize Text Manually: Loop through each character of the raw paragraph string. If it is an alphanumeric character or a space, keep it; if it is a punctuation mark, omit it. Convert the sanitized text to lowercase and split it by spaces.

Build Frequencies: Loop over the cleaned words list. Add counts manually into your custom frequency dictionary.

Identify Max Frequency: Initialize max_word = None and max_count = 0. Iterate through the dictionary keys and values manually to extract the highest frequency pair."""