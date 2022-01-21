def multiplication_table(size):
    result = []
    for i in range(size):
        new_arr = []
        for j in range(size):
            new_arr.append((i+1) * (j+1))
        result.append(new_arr)
    return result        



print(multiplication_table(5))