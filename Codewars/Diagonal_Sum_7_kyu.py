from typing import List

def sum_diagonals(matrix: List[List[int]]) -> int:
    result = 0
    rev_result = 0
    reversed_matrix = matrix[::-1]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                result += matrix[i][j]
    
    for i in range(len(reversed_matrix)):
        for j in range(len(reversed_matrix[0])):
            if i == j:
                rev_result += reversed_matrix[i][j]

    return result + rev_result


