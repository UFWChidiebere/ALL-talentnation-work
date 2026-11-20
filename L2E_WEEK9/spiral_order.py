def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    left = 0
    result = []

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right-=1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top -1, -1):
                result.append(matrix[row][left])
            left += 1

    return result

x1 =([[1,2,3], [4,5,6], [7,8,9]])
x2 = ([[1,2,3,4], [5,6,7,8]])
x3 = ([[1],[2],[3]])
x4 = ([])




# Bonus
def spiral_fill(n: int) -> list:
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        grid.append(row)

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            grid[top][col] = num
            num += 1
        top += 1

        for row in range(top, bottom + 1):
            grid[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                grid[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                grid[row][left] = num
                num += 1
            left += 1

    return grid




print(spiral_order(x1))
print(spiral_order(x2))
print(spiral_order(x3))
print(spiral_order(x4))

