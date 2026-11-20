def caesar_cipher():
    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift pattern (it should be integer): "))
    except ValueError:
        print("Shift pattern must be an integer.")
        return
        
    mode = input("Choose processing mode ('encrypt' or 'decrypt'): ").strip().casefold()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected.")
        return
        
    '''Normalize shift size within the boundaries of a 26-letter alphabet'''
    shift = shift % 26
    if mode == "decrypt":
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            '''Determine alphabetical case base anchor point using .islower()'''
            base = ord("a") if char.islower() else ord("A")
            
            '''Calculate cyclic wrap-around position math INSIDE the chr() function'''
            shifted_char = chr(base + (ord(char) - base + shift) % 26)
            result += shifted_char
        else:
            '''preserved special symbols, space, numbers'''
            result += char

    print(f"Output: {result}")
    return result



# Input: Text: hello | Shift: 1 | Mode: encrypt → Output: ifmmp
# Input: Text: xyz | Shift: 2 | Mode: encrypt → Output: zab (Notice the wrap-around)
# Input: Text: hello, world! | Shift: 3 | Mode: encrypt → Output: khoor, zruog! (Notice punctuation and spaces are preserved)
# Input: Text: ifmmp | Shift: 1 | Mode: decrypt → Output: hello 

caesar_cipher()



"""Normalize Shift Key: Keep shifts bounded within our alphabet matrix bounds using modulo (shift = shift % 26).

Determine Direction: If decrypting, reverse the processing direction (shift = -shift).

Character Iteration: Loop through the message text.

Alphabet Check & Math Wraparound: Use char.isalpha() to capture alpha characters. Use ord(char) to calculate its underlying Unicode point. Check uppercase versus lowercase bases ('a' or 'A') to maintain proper formatting, then apply the cyclic offset formula: new_char = base + (old_char - base + shift) % 26.

Preservation: Append non-alphabet characters without modification.
"""


























'''this code is from freecodecamp: a workshop in freecodecamp'''
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

# encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
# decrypted_text = decrypt(encrypted_text, 13)
# print(encrypted_text)
# print(decrypted_text)