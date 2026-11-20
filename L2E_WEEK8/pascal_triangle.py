def pascal_rows(n: int) -> list[list[int]]:
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1] * (i + 1)

        for j in range(1, i):
            new_row[j] = prev_row[j - 1] + prev_row[j]
        triangle.append(new_row)

    return triangle

def pascal_row_bonus(k:int) ->list[int]:
    row = [1]
    for _ in range(k):
        for j in range(len(row) - 1, 0, -1):
            row[j] = row[j] + row[j - 1]

        row.append(1)
    return row

    
if __name__ == "__main__":
    print("--- QUESTION 7: PASCAL'S TRIANGLE ---")
    total_rows = 5
    my_pyramid = pascal_rows(total_rows)
    
    for idx, row in enumerate(my_pyramid):
        # Generate spacing offsets manually without using .center()
        spaces = " " * (total_rows - idx - 1)
        row_str = " ".join(str(val) for val in row)
        print(f"{spaces}{row_str}")
        
    print("\n--- Q7 BONUS: SINGLE ARRAY IN MEMORY ---")
    print(f"Row Index 4 (5th row): {pascal_row_bonus(4)}")
