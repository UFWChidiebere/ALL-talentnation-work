'''FUNCTION multiply_matrices(A, B):
    rows_A = LENGTH(A)
    cols_A = LENGTH(A[0])
    rows_B = LENGTH(B)
    cols_B = LENGTH(B[0])
    
    // Validate viability check
    IF cols_A != rows_B THEN
        PRINT "Multiplication not possible"
        RETURN
        
    // Step 1: Initialize empty zero result matrix
    result = []
    i = 0
    WHILE i < rows_A:
        row = []
        j = 0
        WHILE j < cols_B:
            APPEND 0 TO row
            j = j + 1
        APPEND row TO result
        i = i + 1
        
    // Step 2: 3-Level nested calculation loop
    r = 0
    WHILE r < rows_A:
        c = 0
        WHILE c < cols_B:
            k = 0
            WHILE k < cols_A:
                result[r][c] = result[r][c] + (A[r][k] * B[k][c])
                k = k + 1
            c = c + 1
        r = r + 1
        
    RETURN result
    
    
    matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
print("Product Matrix:", multiply_matrices(matrix_A, matrix_B))'''

def multiply_matrix(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # FIX: Must compare columns of A to rows of B
    if cols_A != rows_B:
        print('Multiplication is not possible')
        return None

    result = []
    i = 0
    while i < rows_A:
        row = []
        j = 0
        while j < cols_B:
            row.append(0)
            j = j + 1
        result.append(row)
        i = i + 1

    r = 0
    while r < rows_A:
        c = 0
        while c < cols_B:
            k = 0
            while k < cols_A:
                result[r][c] = result[r][c] + (A[r][k] * B[k][c])
                k = k + 1
            c = c + 1
        r = r + 1
        
    return result

matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]
print("Product Matrix:", multiply_matrix(matrix_A, matrix_B))
