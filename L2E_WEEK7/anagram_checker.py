def is_anagram(str1, str2):
    dict1 = {}
    dict2 = {}

    i = 0
    while i < len(str1):
        char = str1[i]
        ascii_val = ord(char)
        if ascii_val >= 65 and ascii_val <= 90:
            char = chr(ascii_val + 32)

        # dict1[char] = dict1.get(char, 0) + 1 #this can be use instead of the if-else statement that is used below

        if char in dict1:
            dict1[char] = dict1[char] + 1
        else:
            dict1[char] = 1
        i += 1

    j = 0
    while j < len(str2):
        char = str2[j]
        ascii_val = ord(char)
        if ascii_val >= 65 and ascii_val <= 90:
            char = chr(ascii_val + 32)

        # dict2[char] = dict2.get(char, 0) + 1 #this can be use instead of the if-else statement that is used below

        if char in dict2:
            dict2[char] = dict2[char] + 1
        else:
            dict2[char] = 1
        j += 1

    if dict1 == dict2:
        return True
    else:
        return False

print(is_anagram("listen", "silent"))        # True
print(is_anagram("Dormitory", "dirtyroom"))  # True
print(is_anagram("hello", "world"))          # False



'''this is another method that can be used to to check for it without using a  dicionary'''
def is_anagram_using_list(str1, str2):
    # Create fixed slots for 26 lowercase letters [a-z]
    frequency_list1 = [0] * 26
    frequency_list2 = [0] * 26

    # Populate first list
    i = 0
    while i < len(str1):
        char = str1[i]
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:  # Convert to lowercase
            ascii_val += 32
        
        # Only track if it's a valid letter [a-z]
        if 97 <= ascii_val <= 122:
            index = ascii_val - 97  # 'a' becomes 0, 'b' becomes 1...
            frequency_list1[index] += 1
        i += 1

    # Populate second list
    j = 0
    while j < len(str2):
        char = str2[j]
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:
            ascii_val += 32
        
        if 97 <= ascii_val <= 122:
            index = ascii_val - 97
            frequency_list2[index] += 1
        j += 1

    # Direct structural comparison
    return frequency_list1 == frequency_list2



'''this is the shortest method if there were to be no constraint and also, this method is structrally slow coz sorting takes extra calculations'''
def is_anagram_cheat_sorting(str1, str2):
    # Convert both to lowercase and sort them alphabetically
    return sorted(str1.lower()) == sorted(str2.lower())


'''this is the professional method'''
from collections import Counter

def is_anagram_cheat_counter(str1, str2):
    # Counter automatically builds a frequency map under the hood
    return Counter(str1.lower()) == Counter(str2.lower())
