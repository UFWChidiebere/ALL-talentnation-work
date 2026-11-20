# def process_weather(location, temperature):
#     if temperature > 25:return 'sunny'
#     else:return 'cloudy'
# print(process_weather('lagos', 10))

'''these are the various ways to get the total of prices in a store'''
cart_items = [5000,3000,7500,2500]
total = 0 
for price in cart_items:total += price
# print(total)

def total_price(prices: list[int]) -> int:
    sum_price = 0
    for price in prices:
        sum_price += price
    return sum_price
# cart_items = [5000,3000,7500,2500]
# print('--' * 10)
# print(total_price(cart_items))

def total_price_sum(prices):
    sum_total = sum(prices)
    return sum_total

# cart_items = [5000,3000,7500,2500]
# print('--' * 10)
# print(total_price_sum(cart_items))


'''now let's say i don't want to add all the price but want to add only the price that is equal or above a specified anount, this is how to go about it'''
def specified_price_sum(prices):
    total = 0
    for price in prices:
        if (0 < price < 3000):
            continue
        total += price
    return total
# cart_items = [5000,3000,7500,2500]
# print(specified_price_sum(cart_items))


#now the above code works using the 'continue' to skip prices that are not up to 3000 without adding them to the sum total. if you don't wnat to use the 'continue', you can do it like this below
def sum_prices_without_skiping(prices):
    total = 0
    for price in prices:
        if price >= 3000: 
            total += price
    return total
# cart_items = [5000,3000,7500,2500]
# print(sum_prices_without_skiping(cart_items))



'''now the two approach is awesome. however, filter can be used to achieve this same result'''
def filter_price_sum(prices):
    return sum(filter(lambda price: price>=3000, prices))
cart_items = [1000, 0, 200, 4000, 4200, 8900, 5900, 7211, 6798, 9099, 570, 1, 45, 67, 688, 10000]
print(f'Thi is the sum total of the prices that are equal or greater than 3000 in the items in the cart: #{filter_price_sum(cart_items)}')


