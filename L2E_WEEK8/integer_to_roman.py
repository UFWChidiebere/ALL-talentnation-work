def int_to_roman(num: int) -> str:
    if not (1 <= num <=3999):
        raise ValueError('Input must be an integer between 1 and 3999 inclusive.')
    roman_mappings = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    result = []
    for value, symbol in roman_mappings:
        while num >= value:
            result.append(symbol)
            num -= value
    return "".join(result)































'''this is the bonus part for this question and it was done with AI'''

def roman_to_integer(s: str) -> int:
    """Week 7 baseline function used to decode Roman numerals back to integers."""
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    # Process from right to left to handle subtractive forms effortlessly
    for char in reversed(s):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
        
    return total


def verify_all_roman_round_trips():
    """
    Bonus Check Loop: Converts every integer from 1 to 3999 to Roman and back.
    Prints 'All round trips passed' or details of the first failure.
    """
    failure_found = False
    
    for i in range(1, 4000):
        # 1. Convert integer to Roman numeral string
        roman_string = int_to_roman(i)
        
        # 2. Convert that string back to an integer
        round_trip_integer = roman_to_integer(roman_string)
        
        # 3. Check if the cycle matches perfectly
        if round_trip_integer != i:
            print(f"❌ Round trip failure found at integer: {i}")
            print(f"   Generated Roman Numeral: {roman_string}")
            print(f"   Decoded back to: {round_trip_integer}")
            failure_found = True
            break  # Stop at the very first failure as requested
            
    if not failure_found:
        print("✅ All round trips passed! (Tested integers 1 through 3999 successfully)")


# Run the validation
if __name__ == "__main__":
    verify_all_roman_round_trips()
