def two_sum(numbers, target):
    seen = {}  
    
    for i, num in enumerate(numbers):
        complement = target - num
        
        '''Check if the needed complement has already been traversed'''
        if complement in seen:
            return [seen[complement], i]
            
        '''Store current number and index in hash map'''
        seen[num] = i
        
    return []

'''Test Case Given: Numbers: [2, 7, 11, 15] | Target: 9 → Output: [0, 1]''' 
numbers = [3, 2, 4]
print(two_sum(numbers, 6))






























"""Memory Storage: Initialize a empty dictionary seen = {} to map processed values to their respective indices.

Linear Processing: Loop through the list using enumerate(numbers) to get both index i and value num.

Complement Verification: Compute the target difference complement = target - num.

Lookup: Search the hash map keys for the complement. If it exists, return [seen[complement], i]. If it does not, store the current number's index (seen[num] = i) and continue."""
