prices_in_usd = [10, 20, 30]

# Double every price in the list
doubled_prices = map(lambda price: price * 2, prices_in_usd)

print(doubled_prices)  # Output: [20, 40, 60]


'''just like filter() uses lambda to drop items, map() uses lambda to change items in a list'''

'''they both drop the memory address of the item they are working with. so to get the original/raw/final input, you will need to wrap them inside a list/set/tuple this is as a result of what is called lazy evaluation'''


'''THE GOLDEN RULE OF LAMBDAS

Only use lambdas for simple, one-line operations. If your logic requires multiple steps, if/elif/else blocks, or loops, stop using lambda and write a standard def function_name(): block instead to keep your code clean and readable.'''


'''these are more examples on how to use the lambda function'''
# A function that adds two numbers together
add_together = lambda a, b: a + b

print(add_together(10, 5))  # Output: 15


square_number = lambda x: x * x

print(square_number(5))  # Output: 25



#this is literally combining both the filter() and the map() inside the same lambda function
numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter the evens -> yields (2, 4, 6)
# Step 2: Map over those evens to triple them -> yields (6, 12, 18)
# Step 3: Wrap it all in a list to see the final raw output
final_output = list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, numbers)))

print(final_output)  # Output: [6, 12, 18]


