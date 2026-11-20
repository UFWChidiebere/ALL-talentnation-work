from functools import reduce
def flatten_nested_list(nested_list: list) ->list:
    e_list = []
    for item in nested_list:
        if isinstance(item, list):
            e_list.extend(flatten_nested_list(item))
        else:

            e_list.append(item)
    return e_list
    
def sum_nested_list(nested_list):
    flat = flatten_nested_list(nested_list)
    if not flat:
        return 0 #this is to make the reduce reduce 0 since a default value is not passed in as the third parameter. if i am to remove this, i will have to add 0 into the reduce function(after the flat(flat, 0))

    return reduce(lambda total, num: total + num, flat)
        

'''the above code solve the problem, however, it does not satisfy how it was instructed to solving the problem. '''


#THIS IS THE CODE THAT SOLVE THE PEOBLEM RECURSIVELY
def sum_nested_list_recursively(nested_list:list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += sum_nested_list_recursively(item)
        else:
            total += item
    return total
nested_list = [1, [2, 3], [4, [5]]]
print(sum_nested_list_recursively(nested_list))

