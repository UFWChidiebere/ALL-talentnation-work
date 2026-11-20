def decimal_to_binary(num):
    if num == 0:
        return 0
    binary_str = ""
    temp = num

    while temp > 0:
        remainder = temp % 2
        binary_str = str(remainder) + binary_str
        temp = int(temp/2)
    return binary_str
print(decimal_to_binary(10))
print(decimal_to_binary(25))
print(decimal_to_binary(1))
# print(decimal_to_binary(1010))
