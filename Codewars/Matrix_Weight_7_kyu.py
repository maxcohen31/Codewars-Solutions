from typing import List
import numpy as np

def thin_or_fat(matrix: List[int]) -> str:
    sum_rows = np.sum(matrix, axis=0)
    sum_columns = np.sum(matrix, axis=1)
    
    height = np.sum([np.sqrt(i) for i in sum_rows])
    width = np.sum([np.sqrt(j) for j in sum_columns])

    if np.sum(sum_rows) < 0 or np.sum(sum_columns) < 0:
        return None
    elif height > width:
        return "thin"
    elif height < width:
        return "fat"
    elif width == height:
        return "perfect"
    
# Alternative method
def thin_or_fat(matrix: List[int]) -> str:
    rows = []
    columns = []

    # Find sum of elements in rows:
    for i in range(len(matrix)):
        row = 0
        for j in matrix[i]:
            row += j
        rows.append(row)
    
    # Find sum of elements in columns
    for i in range(len(matrix)):
        col = 0
        for j in range(len(matrix)):
            col += matrix[j][i]
        columns.append(col)

    width = np.sum([np.sqrt(r) for r in rows])
    height = np.sum([np.sqrt(c) for c in columns])
    
    if sum(rows) < 0 or sum(columns) < 0:
        return None
    elif width > height:
        return "fat"
    elif width < columns:
        return "thin"
    else:
        return "perfect"
    

m = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]


print(thin_or_fat(m))