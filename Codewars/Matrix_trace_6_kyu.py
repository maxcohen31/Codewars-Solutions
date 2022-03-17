def trace(matrix):
    if matrix == []:
        return None
    elif len(matrix) != len(matrix[0]):
        return None
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == len(matrix[0]):
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    result += matrix[i][j] 
    return result




