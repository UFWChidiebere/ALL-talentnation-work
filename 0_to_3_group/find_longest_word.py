def longest_word(words: list[str]) -> str:
    if isinstance(words, str):
        words = words.split() #this line of code is to check fot the longest word in a sentence

    if not words:
        return ''
    
    l_w = words[0]
    for word in words:
        if len(word) > len(l_w):
            l_w = word

    return f"The longest word in the list is: '{l_w}'"

words = ["cat", "elephant", "dog", "hippopotamus"]
words1 = ["apple", "pear", "peach"]
word3 = 'i love programming'
# word4 = ['i love programming']
print(longest_word(words))
print(longest_word(words1))
print(longest_word(word3))
# print(longest_word(word4))


'''this is the shortest way  to solving the same problem using the max() function. the function takes an iterable, and then an optional key and an optional default parameter to fall back on if the key provided is not found'''
def longest_word_max(words):
    return max(words, key=len) #the len is use for the key coz if it is not used, python will find  the max using the ascii value of the alphabet(be it lower and upper). if there's no match on the first letter it will move to the next one and compare until there's a match and then return it
print(longest_word_max(["cat", "zebra", "elephant"]))
