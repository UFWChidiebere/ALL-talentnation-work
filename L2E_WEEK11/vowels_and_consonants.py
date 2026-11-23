def count_letters(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
            
    return vowel_count, consonant_count
print(count_letters("Hello, World 123"))  # Output: (3, 7)

#the above code is correct but it does not handle the case where the input string is empty and also the conversion part

def count_letters(text):
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        lower_char = char.lower()
        

        if "a" <= lower_char <= "z":
            if lower_char in "aeiou":
                vowel_count += 1
            else:
                consonant_count += 1
                
    return (vowel_count, consonant_count)

print(count_letters("Hello, World 123"))  
print(count_letters("AEIOU"))             
print(count_letters("rhythm"))            
print(count_letters(""))                 
