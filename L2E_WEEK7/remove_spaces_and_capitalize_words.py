'''FUNCTION modify_string(sentence):
    capitalized_str = ""
    no_spaces_str = ""
    
    new_word_flag = True
    
    i = 0
    WHILE i < LENGTH(sentence):
        char = sentence[i]
        
        // Block 1: Capitalization logic
        IF char == " " THEN
            capitalized_str = capitalized_str + " "
            new_word_flag = True
        ELSE
            IF new_word_flag THEN
                ascii_val = ord(char)
                IF ascii_val >= 97 AND ascii_val <= 122 THEN
                    char = chr(ascii_val - 32)
                new_word_flag = False
            capitalized_str = capitalized_str + char
            
        // Block 2: Space removal logic
        IF sentence[i] != " " THEN
            no_spaces_str = no_spaces_str + sentence[i]
            
        i = i + 1
        
    PRINT "Capitalized: " + capitalized_str
    PRINT "No Spaces: " + no_spaces_str
'''

def modify_string(sentence):
    capitlized_str = ''
    no_space_str = ''
    new_word_flag = True

    i = 0

    while i < len(sentence):
        char = sentence[i]

        if char == ' ':
            capitlized_str += ' '
            new_word_flag = True
        else:
            if new_word_flag:
                ascii_val = ord(char)
                if ascii_val >= 97 and ascii_val <= 122:
                    char = chr(ascii_val - 32)
                new_word_flag = False
            capitlized_str += char

        if sentence[i] != ' ':
            no_space_str += sentence[i]
        i += 1
    print(f"Capitalized: '{capitlized_str}'")
    print(f"No Spaces: '{no_space_str}'")

modify_string("hello world from python")