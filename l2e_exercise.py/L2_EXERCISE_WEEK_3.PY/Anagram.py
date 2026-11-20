def is_anagram(word1, word2):
    '''Change the clean inputs to lowercase'''
    w1 = word1.casefold()
    w2 = word2.casefold()
    '''Fast exit if lengths do not match'''
    if len(w1) != len(w2):
        print("Output: Not an anagram")
        return False
    freq1 = {}
    freq2 = {}
    '''Build frequency map for word 1'''
    for char in w1:
        freq1[char] = freq1.get(char, 0) + 1
    '''Build frequency map for word 2'''
    for char in w2:
        freq2[char] = freq2.get(char, 0) + 1

    """Compare dictionaries: to check if it is the same thing that is in dictionary 1 that is in dictionary 2"""
    if freq1 == freq2:
        print("Output: Anagram")
        return True
    else:
        print("Output: Not an anagram")
        return False
    
'''Test Case'''
# Input: Word 1: listen | Word 2: silent → Output: Anagram
# Input: Word 1: triangle | Word 2: integral → Output: Anagram
# Input: Word 1: apple | Word 2: pale → Output: Not an anagram
# Input: Word 1: hello | Word 2: billion → Output: Not an anagram 

(is_anagram('silent', 'listen'))
(is_anagram('triangle', 'integral'))
(is_anagram('apple', 'pale'))
(is_anagram('hello', 'billion'))







































'''Length Pre-check: If lengths differ, they cannot be anagrams (though spaces could throw this off, assuming single-word inputs as per examples).

Frequency Mapping Function: Create a helper workflow to build character map counts. Lowercase everything to enforce case-insensitivity.

Compare Maps: Compare the dictionary footprints of both words. If every key matches identical values, output "Anagram".'''