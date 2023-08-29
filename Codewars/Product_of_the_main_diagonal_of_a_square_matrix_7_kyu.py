from typing import List

def main_diagonal_product(mat: List[List[int]]) -> int:
    result = 1
    row = len(mat)
    col = len(mat[0])

    for i in range(row):
        for j in range(col):
            if i == j:
                result *= mat[i][j]
    return result

