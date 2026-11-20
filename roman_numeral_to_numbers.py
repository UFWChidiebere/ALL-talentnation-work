# ROMAN NUMERAL TO NUMBER

# func to convert roman numeral to number
def rom_to_num(roman):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    for i in range(len(roman)):
        # check if not last roman numeral and the value is less than the next one
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
            total -= values[roman[i]]
        else:
            total += values[roman[i]]
    return total

# func to convert number to roman numerals
def num_to_rom(number):
    values = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    result = ""
    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value
    return result

def convert_roman(roman):
    roman = roman.upper()

    # check if input are valid Roman numerals  
    if any(char not in "IVXLCDM" for char in roman):  
        return "Invalid Roman numeral"  
  
    number = rom_to_num(roman)  

    # check if result follows the standard format  
    if num_to_rom(number) != roman:  
        return "Invalid Roman numeral"  
    return number

# Main Program Execution
print("========== CONVERSION MENU ==========")
print("1. Roman numeral to number")
print("2. Number to Roman numeral")

choice = input("Choose an option: ")

if choice == "1":
    roman = input("Enter a Roman numeral: ")
    print("Numeric value:", convert_roman(roman))
elif choice == "2":
    number = int(input("Enter a number: "))
    print("Roman numeral value:", num_to_rom(number))
else:
    print("Invalid choice")


# Quick automated test runner
test_romans = {
    "VIII": 8, 
    "MCMXCIV": 1994, 
    "xiv": 14, 
    "IIII": "Invalid Roman numeral", 
    "VX": "Invalid Roman numeral"
}

print("\n--- Running Automated Tests ---")
for roman_input, expected in test_romans.items():
    result = convert_roman(roman_input)
    status = "✅ PASS" if result == expected else f"❌ FAIL (Got {result}, Expected {expected})"
    print(f"Input: {roman_input:<10} -> {status}")
