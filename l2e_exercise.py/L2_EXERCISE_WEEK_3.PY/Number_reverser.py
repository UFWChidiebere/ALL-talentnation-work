def reverse_integer(num):
    '''Establish base flag constraints for negative numbers'''
    is_negative = False
    if num < 0:
        is_negative = True
        num = -num

    reversed_num = 0
    
    while num > 0:
        '''Isolate the last digit'''
        digit = num % 10    
        '''Shift left and add'''            
        reversed_num = (reversed_num * 10) + digit  
        '''cur off the processed digit'''
        num = num // 10                 
    '''Re-apply structural sign inversion if verified negative'''
    if is_negative:
        reversed_num = -reversed_num
    return reversed_num

'''Test Case for the exercise'''
# Input: 12345 → Output: 54321
# Input: -987 → Output: -789
# Input: 1200 → Output: 21 (Mathematically, leading zeros are dropped)
# Input: 0 → Output: 0 

print(reverse_integer(12345))
print(reverse_integer(-789))
print(reverse_integer(21))
print(reverse_integer(0))
















































































'''Sign Extraction: Track if the input is negative. Store this in a flag variable and convert the value to its absolute magnitude (abs(num)) to run math cleanly.

Initialize Reversed Buffer: Set reversed_num = 0.

Algorithmic Extraction Loop: Run a loop while num > 0.

Isolate Digit: Extract the trailing digit using modulo (digit = num % 10).

Shift and Build: Left-shift the existing reversed layout buffer by multiplying by 10, then add the new digit (reversed_num = (reversed_num * 10) + digit).

Truncate Original: Truncate the evaluated trailing digit off the original value via floor integer division (num = num // 10).

Reapply Sign: Multiply by -1 at completion if the sign flag was active.'''