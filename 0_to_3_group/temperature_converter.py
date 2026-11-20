def convert_temperature(temp: float, target_unit: str) -> float:
    target_unit = target_unit.lower()
    units = "cf"

    if target_unit not in units:
        raise ValueError('Target unit must be either "c" or "f"')

    if target_unit == 'f':
        convert_temp = round(((temp * 9/5) + 32), 2)
        return convert_temp
    else:
        convert_temp = round(((temp - 32) * 9/5), 2)
        return convert_temp

print(convert_temperature(32.0, 'c'))
print(convert_temperature(100.0, 'F'))



'''now this is the code to convert from celsius to fahrenhiet and kelvin assuming that our starting temp is always celsius'''

def convert_temperature(temp: float, target_unit: str) -> float:
    target_unit = target_unit.lower()
    valid_units = {'f', 'k'}
    if target_unit not in valid_units:
        raise ValueError('Target unit must be either "f" or "k"(assuming the inputed temperature is always celsius)')

    if target_unit =='f':
        converted_temp = (temp * 1.8) + 32
        return round(converted_temp, 1)
    elif target_unit == 'k':
        converted_temp = temp + 273.15
        return round(converted_temp, 1)

print(convert_temperature(0, 'f'))   
print(convert_temperature(100, 'k'))


'''now what if the starting temp is not always celsius? this is how to solve it'''
def convert_temperature(temp: float, from_unit: str, target_unit: str) -> float:
    # Normalize inputs to lowercase
    start = from_unit.lower()
    target = target_unit.lower()
    
    # 1. Validate units
    valid_units = {'c', 'f', 'k'}
    if start not in valid_units or target not in valid_units:
        raise ValueError("Units must be 'c', 'f', or 'k'")
        
    # If units are the same, no conversion needed
    if start == target:
        return round(temp, 1)

    # 2. Convert everything to Celsius first as a baseline
    if start == 'c':
        celsius = temp
    elif start == 'f':
        celsius = (temp - 32) / 1.8
    elif start == 'k':
        celsius = temp - 273.15

    # 3. Convert Celsius to the target unit
    if target == 'c':
        result = celsius
    elif target == 'f':
        result = (celsius * 1.8) + 32
    elif target == 'k':
        result = celsius + 273.15

    # Return as a float rounded to 1 decimal place to match type hint
    return round(result, 1)

# Examples:
print(convert_temperature(100, 'f', 'c'))  # 37.8 (Fahrenheit to Celsius)
print(convert_temperature(0, 'c', 'k'))    # 273.2 (Celsius to Kelvin)



'''now this is for when you want to keep the parameters to 2 and you still want the starting temperature to be known, you use this creative method'''
def convert_temperature(temp_str: str, target_unit: str) -> float:
    # 1. Split the string (e.g., "100C" becomes temp=100.0 and start="c")
    temp = float(temp_str[:-1]) 
    start = temp_str[-1].lower()
    target = target_unit.lower()
    
    # 2. Base conversion to Celsius
    if start == 'c':
        celsius = temp
    elif start == 'f':
        celsius = (temp - 32) / 1.8
    elif start == 'k':
        celsius = temp - 273.15
    else:
        raise ValueError("Input string must end with 'C', 'F', or 'K'")

    # 3. Target conversion
    if target == 'c':
        return round(celsius, 1)
    elif target == 'f':
        return round((celsius * 1.8) + 32, 1)
    elif target == 'k':
        return round(celsius + 273.15, 1)
    else:
        raise ValueError("Target unit must be 'c', 'f', or 'k'")

# How to use it:
print(convert_temperature("100F", "c"))  # 37.8 (Fahrenheit to Celsius)
print(convert_temperature("0C", "k"))    # 273.2 (Celsius to Kelvin)
print(convert_temperature("300K", "f"))  # 80.3  (Kelvin to Fahrenheit)
