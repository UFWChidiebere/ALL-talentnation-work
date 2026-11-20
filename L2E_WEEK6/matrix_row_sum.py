matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]

for row_index in range(0, len(matrix)):
    current_row = matrix[row_index]
    row_sum = 0
    column_count = len(current_row)

    for item in current_row:
        row_sum += item

    row_average = row_sum / column_count
    print(f'Row {row_index + 1} total: {row_sum} | average: {row_average}')


total_row = len(matrix)
total_column = len(matrix[0])

for col_index in range(0, total_column):  
    col_sum = 0
    for row_index in range(0, total_row):  
        item = matrix[row_index][col_index] 
        col_sum += item                     
    print(f'Column {col_index + 1} total: {col_sum}')
