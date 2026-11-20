"""Chika's code for most frequent occuring word"""
word = input("Enter Word Here:")
mostcommon = word[0]
highestcount = word.count(mostcommon)
for i in word:
    if word.count(i) > highestcount:
        mostcommon = i
        highestcount = word.count(i)
print(mostcommon)

"""this code was written by Tosin and it is to check for repetitive word in a sentence"""
# 1. Take input and clean it up
sentence = input('Enter sentence: ').lower().strip().split()

res = {}

# 2. Count occurrences of each word
for word in sentence:
    if word not in res:
        res[word] = 1
    else:
        res[word] += 1

# 3. Print all word counts
for key, value in res.items():
    print(f'{key} : {value}')

# 4. Find and print the highest count
if res:  # Ensures the dictionary isn't empty if the user entered nothing
    highest_word = max(res, key=res.get)
    highest_count = res[highest_word]
    print(f'\nThe highest is "{highest_word}" with a count of {highest_count}')




"""the code without using max"""
# 1. Take input and clean it up
sentence = input('Enter sentence: ').lower().strip().split()

res = {}

# 2. Count occurrences of each word
for word in sentence:
    if word not in res:
        res[word] = 1
    else:
        res[word] += 1

# 3. Print all word counts
for key, value in res.items():
    print(f'{key} : {value}')

# 4. Find the highest count manually
highest_word = ""
highest_count = 0

for key, value in res.items():
    if value > highest_count:
        highest_count = value
        highest_word = key

# 5. Output the result
if highest_count > 0:
    print(f'\nThe highest is "{highest_word}" with a count of {highest_count}')



