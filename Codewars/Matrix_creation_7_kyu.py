def get_matrix(n):
    array_zero = [[0] * n for i in range(n)]
    for row in range(len(array_zero)):
        for col in range(len(array_zero[0])):
            if row == col:
                array_zero[row][col] = 1
    return array_zero           

import numpy as np
def get_matrix(n):
    return np.identity(n).tolist()

print(get_matrix(4))
        