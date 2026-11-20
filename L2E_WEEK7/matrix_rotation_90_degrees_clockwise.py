def rotate_matrix_clockwise(matrix):
    N = len(matrix)

    r = 0
    while r < N:
        c = r + 1
        while c < N:
            temp = matrix[r][c]
            matrix[r][c] = matrix[c][r]
            matrix[c][r] = temp
            c += 1
        r += 1


    row_idx = 0
    while row_idx < N:
        left = 0
        right = N - 1
        while left < right:
            temp_val = matrix[row_idx][left]
            matrix[row_idx][left] = matrix[row_idx][right]
            matrix[row_idx][right] = temp_val
            left += 1
            right -= 1
        row_idx += 1



my_matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

rotate_matrix_clockwise(my_matrix)
print("Rotated Matrix:")
for row in my_matrix:
    print(row)