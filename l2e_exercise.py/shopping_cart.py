class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        # if product not in self.cart: #this is removed so as to add duplicate product in the cart
        self.cart.append(product)


    def remove_product(self, product):
        if product in self.cart:
            del self.cart[product]  # This deletes the key from the dictionary
            print(f"{product} removed from cart.")
        else:
            print("This product is not in your cart.")



    # def remove_product(self, product):
    #     if product in self.cart:
    #         print("This product is not available")
    #     else:
    #         del product

    # def remove_product(self, product):
    # if product in self.cart:
    #     self.cart.remove(product)
    #     print(f"{product} removed from cart.")
    # else:
    #     print("This product is not in your cart.")



    def show_cart(self):

        print("Shopping Cart")
        print("---------------")
        for product in self.cart:
            print(f"{product.name} -- $ {product.price}")

    def calculate_total(self):
        total = 0
        print("shopping Cart")
        print("-------------")
        for product in self.cart:
            total += product.price

    def empty_cart(self):
        self.cart.clear()
        print("Cart is now empty")
        
