def copy_dict(stock):
    new_stock = {}
    for key, value in stock.items():
        new_stock[key] = value
    return new_stock

def restock(stock, item, qty):
    new_stock = copy_dict(stock)
    if isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
        return new_stock
    if item in new_stock:
        new_stock[item] = new_stock[item] + qty
    else:
        new_stock[item] = qty
    return new_stock

def sell(stock, item, qty):
    new_stock = copy_dict(stock)
    if isinstance(qty, bool) or not isinstance(qty, int) or qty <= 0:
        return (new_stock, False)
    if item not in new_stock or new_stock[item] < qty:
        return (new_stock, False)
    new_stock[item] = new_stock[item] - qty
    return (new_stock, True)

def low_stock(stock, limit):
    result = []
    for item, qty in stock.items():
        if qty < limit:
            result.append(item)
    return result

def total_items(stock):
    total = 0
    for qty in stock.values():
        total = total+qty
    return total


# Bonus
def inventory_value(stock: dict, prices: dict) -> int | float:
    total_val = 0
    for item in stock:
        if item in prices:
            total_val += stock[item] * prices[item]
    return total_val


# # --- Test Suite for C5: Shop Inventory ---

# stock = {"rice": 10, "beans": 5}
# print("1. INITIAL STOCK:", stock)
# print("-" * 40)

# # 1. Prompt Examples & Proof of Immutability
# print("Restock new item ('gari', 8):", restock(stock, "gari", 8))
# print("Restock existing ('rice', 5):", restock(stock, "rice", 5))
# print("Stock after restocks (MUST BE UNCHANGED):", stock)
# print("-" * 40)

# # 2. Successful Sale & Immutability Proof
# updated_stock, ok = sell(stock, "rice", 4)
# print("Sell ('rice', 4):", updated_stock, "| Success:", ok)
# print("Original stock after successful sell (MUST BE UNCHANGED):", stock)
# print("-" * 40)

# # 3. Failed Sales (Not enough stock & Missing item)
# failed_1, ok_f1 = sell(stock, "beans", 9)
# print("Sell too much ('beans', 9):", failed_1, "| Success:", ok_f1)

# failed_2, ok_f2 = sell(stock, "yam", 1)
# print("Sell missing ('yam', 1):", failed_2, "| Success:", ok_f2)
# print("Original stock after failed sells (MUST BE UNCHANGED):", stock)
# print("-" * 40)

# # 4. Required Custom Scenario: Selling Exact Quantity Down to 0
# exact_sale, ok_exact = sell(stock, "beans", 5)
# print("Sell exact stock ('beans', 5):", exact_sale, "| Success:", ok_exact)
# print("Is 'beans' still in dictionary at 0?:", "beans" in exact_sale and exact_sale["beans"] == 0)
# print("-" * 40)

# # 5. Edge Cases: Invalid Quantities (0, negative, float, boolean)
# print("Restock 0:", restock(stock, "rice", 0))
# print("Restock negative (-5):", restock(stock, "rice", -5))
# print("Restock float (2.5):", restock(stock, "rice", 2.5))
# print("Sell boolean (True):", sell(stock, "rice", True))
# print("-" * 40)

# # 6. Helper Queries: low_stock & total_items
# print("Low stock (< 6) on original:", low_stock(stock, 6))          # ['beans']
# print("Low stock (< 6) after exact sale:", low_stock(exact_sale, 6)) # ['beans'] (since 0 < 6)
# print("Total items in original:", total_items(stock))                # 15
# print("Total items in empty shop:", total_items({}))                 # 0

stock = {"rice": 10, "beans": 5}

print("Before calls:", stock)

print(restock(stock, "gari", 8))    # {'rice': 10, 'beans': 5, 'gari': 8}
print(restock(stock, "rice", 5))    # {'rice': 15, 'beans': 5}
print(sell(stock, "rice", 4))       # ({'rice': 6, 'beans': 5}, True)
print(sell(stock, "beans", 9))      # ({'rice': 10, 'beans': 5}, False)
print(sell(stock, "yam", 1))        # ({'rice': 10, 'beans': 5}, False)
print(low_stock(stock, 6))          # ['beans']
print(total_items(stock))           # 15

print("After calls:", stock)        # {'rice': 10, 'beans': 5}



print('==' * 20)
assert restock(stock, "gari", 8) == {"rice": 10, "beans": 5, "gari": 8}
assert restock(stock, "rice", 5) == {"rice": 15, "beans": 5}
assert sell(stock, "rice", 4) == ({"rice": 6, "beans": 5}, True)
assert sell(stock, "beans", 9) == ({"rice": 10, "beans": 5}, False)
assert sell(stock, "yam", 1) == ({"rice": 10, "beans": 5}, False)
assert low_stock(stock, 6) == ["beans"]
assert total_items(stock) == 15
assert stock == {"rice": 10, "beans": 5}
print("All example checks passed!")
