input_string ="aaabbc"
if len(input_string) == 0:
    print('')

compressed_result = ''
current_char = input_string[0]
current_count = 1

for index in range(1, len(input_string)):
    char = input_string[index]
    if char == current_char:
        current_count += 1
    else:
        compressed_result += current_char + str(current_count)
        current_char = char
        current_count = 1

compressed_result += current_char + str(current_count)
print(f"Encoded: {compressed_result}")


encoded_string = "a12b2"
decoded_result = ''
index = 0

while index < len(encoded_string):
    char = encoded_string[index]
    index += 1

    count_str = ''
    while index < len(encoded_string) and encoded_string[index].isdigit():
        count_str += encoded_string[index]
        index += 1

    if count_str == '':
        count_int = 1
    else:
        count_int = int(count_str)

    decoded_result += char * count_int
print(f'Decoded: {decoded_result}')

'''now this is the code to ask users to input whatever they want to perform in the terminal'''

# --- PART 1: ENCODER ---
# Updated: Now asks the user for a string to compress
input_string = input("Enter a string to encode (e.g., aaabbc): ")

if len(input_string) == 0:
    print('Empty string entered.')
else:
    compressed_result = ''
    current_char = input_string[0]
    current_count = 1

    for index in range(1, len(input_string)):
        char = input_string[index]
        if char == current_char:
            current_count += 1
        else:
            compressed_result += current_char + str(current_count)
            current_char = char
            current_count = 1

    compressed_result += current_char + str(current_count)
    print(f"Encoded: {compressed_result}")


print("-" * 30) # A visual divider in the terminal


# --- PART 2: STRETCH DECODER ---
# Updated: Now asks the user for an encoded string to expand
encoded_string = input("Enter an encoded string to decode (e.g., a12b2): ")
decoded_result = ''
index = 0

while index < len(encoded_string):
    char = encoded_string[index]
    index += 1

    count_str = ''
    while index < len(encoded_string) and encoded_string[index].isdigit():
        count_str += encoded_string[index]
        index += 1

    if count_str == '':
        count_int = 1
    else:
        count_int = int(count_str)

    decoded_result += char * count_int

print(f'Decoded: {decoded_result}')


        