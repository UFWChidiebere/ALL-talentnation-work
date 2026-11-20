def sum(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total


# print(sum([2,4,6]))

def matrix(mat):
    for i in range(len(mat)):
        print(f"Row {i+1} total: {sum(mat[i])}")

matrix([[2, 4, 6], [1, 3, 5], [10, 20, 30]]
)

'''another method'''
matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
for i in range(len(matrix)):
    row_total = 0

    for num in matrix[i]:
        row_total += num
    print(f'Row {i + 1} total: {row_total}')


