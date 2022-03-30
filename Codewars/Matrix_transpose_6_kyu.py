def transpose(matrix):
    return [[matrix[col][row] for col in range(len(matrix))] for row in range(len(matrix[0]))]
    
# Nested for loop
def transpose2(matrix):
    transpose_result = []
    for row in range(len(matrix[0])):
        new_matrix = []
        for col in range(len(matrix)):
            new_matrix.append(matrix[col][row])
        transpose_result.append(new_matrix)
    return transpose_result

import numpy as np
def transpose3(matrix):
    return np.transpose(matrix).tolist()
A = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

B = [[1, 2, 3]]

