# Recursive Method - O(n^3)
def add(A,B):
    C =[[0 for j in range(len(A[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j]+B[i][j]
    return C

def multiply(A,B):
    result_matrix = [[0 for j in range(len(A[0]))] for i in range(len(A))]
    if len(A)==1 and len(B)==1:
        return [[A[0][0]*B[0][0]]]
    if len(A[0])!=len(B):
        return "Dimensions should be in powers of 2"
    else:
        split_index = len(A)//2
        A11 = [[0 for j in range(split_index)] for i in range(split_index)]
        A12 = [[0 for j in range(split_index)] for i in range(split_index)]
        A21 = [[0 for j in range(split_index)] for i in range(split_index)]
        A22 = [[0 for j in range(split_index)] for i in range(split_index)]
        B11 = [[0 for j in range(split_index)] for i in range(split_index)]
        B12 = [[0 for j in range(split_index)] for i in range(split_index)]
        B21 = [[0 for j in range(split_index)] for i in range(split_index)]
        B22 = [[0 for j in range(split_index)] for i in range(split_index)]
        for i in range(split_index):
            for j in range(split_index):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j+split_index]
                A21[i][j] = A[i+split_index][j]
                A22[i][j] = A[i+split_index][j+split_index]
                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j+split_index]
                B21[i][j] = B[i+split_index][j]
                B22[i][j] = B[i+split_index][j+split_index]
        

        r11 = add(multiply(A11,B11),multiply(A12,B21))
        r12 = add(multiply(A11,B12),multiply(A12,B22))
        r21 = add(multiply(A21,B11),multiply(A22,B21))
        r22 = add(multiply(A21,B12),multiply(A22,B22))
        for i in range(split_index):
            for j in range(split_index):
                result_matrix[i][j] = r11[i][j]
                result_matrix[i][j+split_index] = r12[i][j]
                result_matrix[i+split_index][j] = r21[i][j]
                result_matrix[i+split_index][j+split_index] = r22[i][j]
        
        return result_matrix

        
matrix_A = [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [2, 2, 2, 2] ] 
 

 
matrix_B = [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [2, 2, 2, 2] ] 
 

 
print(multiply(matrix_A, matrix_B))

        


