def calculate_total(cart_items):
    """
    Calculate the total price of items in the shopping cart.

    Args:
        cart_items (list): A list of dictionaries, each representing an item in the cart.
                           Each dictionary should have 'price' and 'quantity' keys.

    Returns:
        float: The total price of all items in the cart.
    """
    total = 0.0
    for item in cart_items:
        total += item['price'] * item['quantity']
    return total

# 1. Define the items as dictionaries containing their details
shopping_cart = [
    {"name": "Notebook", "price": 500, "quantity": 1},
    {"name": "Pen", "price": 100, "quantity": 2},
    {"name": "Water Bottle", "price": 1200, "quantity": 1}
]

# 2. Pass the list of items as an argument into the function
final_bill = calculate_total(shopping_cart)

# 3. Print the output from outside the function
print(f"Total Cart Cost: {final_bill}")  # Output: 1900




'''this is the question that brought up the above code. The question is asking to create a function that calculates the total price of items in a shopping cart. The function should take a list of dictionaries as input, where each dictionary represents an item in the cart and contains 'price' and 'quantity' keys. The function should return the total price of all items in the cart. The code provided defines the function, creates a shopping cart with items, calls the function with the shopping cart, and prints the total cost.''' 

'''saw the stuff while studying and here is the statement or the stuff ''' #Suppose someone adds three items to their cart:

    # A notebook priced at 500
    # A pen priced at 100, with 2 being purchased
    # A water bottle priced at 1,200