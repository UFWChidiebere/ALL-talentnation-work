def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]
    else:
        start_num < end_num
        range_list = range_of_numbers(start_num, end_num - 1)
        range_list.append(end_num)
        return range_list


"""the above method is by shrinking the end_num"""

'''below is another method to doing same task by increasing the start_num'''

# def range_of_numbers(start_num, end_num):
#     if start_num == end_num:
#         return[start_num]
#     else:
#         start_num < end_num
#         range_list = range_of_numbers(start_num + 1, end_num)
#         return [start_num] + range_list



print(range_of_numbers(3, 9))   # Output: [3, 4, 5, 6, 7, 8, 9]
print(range_of_numbers(5, 5))   # Output: [5]
print(range_of_numbers(10, 15)) # Output: [10, 11, 12, 13, 14, 15]
