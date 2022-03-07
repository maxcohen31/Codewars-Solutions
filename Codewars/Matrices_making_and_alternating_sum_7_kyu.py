def score_matrix(matrix):
    a = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[-1])):
            a += pow(-1, col+row) * (matrix[row][col])
    return a

m1 = [[1, 2, 3], [-3, -2, 1], [3, -1, 2]]
m2 = [[1, 2, 3, 4], [-3, -2, 1, 1], [3, 8, -1, 2], [20, 5, 10, -4], 
        [10, -8, -8, 4]]
print(score_matrix(m2))

