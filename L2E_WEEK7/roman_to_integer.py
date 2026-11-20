def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0

    while i < len(s):
        current_val = roman_map[s[i]]

        if i + 1 < len(s): #this checks if there's a next value
            next_val = roman_map[s[i+1]]
            if current_val < next_val: #this is where the subtraction happens
                total += (next_val - current_val)
                i += 2 #this is to make sure the previous 2 letters we processed during the subtraction is not repeated.... so we skip it and then  move to the next letter
                continue
        total += current_val
        i += 1
    return total

print("III ->", roman_to_int("III"))
print("LVIII ->", roman_to_int("LVIII"))
print("MCMXCIV ->", roman_to_int("MCMXCIV"))




result1 = roman_to_int("MCMXCIV")
print(f"Test Case 1 - Input: 'MCMXCIV' | Expected: 1994 | Got: {result1}")


result2 = roman_to_int("MMMCMXCIX")
print(f"Test Case 2 - Input: 'MMMCMXCIX' | Expected: 3999 | Got: {result2}")

