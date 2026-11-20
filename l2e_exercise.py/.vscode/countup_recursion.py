"""In this workshop, you will create a countup function that uses recursion to create a list of numbers from 1 to a given number."""

def countup(number):
    if number < 1:
        return []
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list

print(countup(5))


"""the above fumction will output in ascending order cox of the core rule of recursion : a code that happen after the recursive call must stay in line"""


def countdown(num):
    if num < 1:
        return []

    count_list = [num]
    count_list.extend(countdown(num- 1))
    return count_list


print(countdown(8))