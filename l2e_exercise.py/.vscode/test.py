def recursive_countdown(number):
    #the if statement is the base case
    if number < 1:
        return
    print(number)
    #the function below is the recursive case
    recursive_countdown(number -1)


recursive_countdown(5)


def recursive_countdown(number):
    print(f'Function call started for number: {number}')
    if number < 1:
        print('Base case reached')
        return
    print(f'Calling recursive_countdown with number: {number - 1}')
    recursive_countdown(number - 1)
    print(f'Function call completed for number: {number}')

recursive_countdown(3)