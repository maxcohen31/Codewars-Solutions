def sc(apple):
    result = []
    for row in range(len(apple)):
        for col in range(len(apple[row])):
            if apple[row][col] == 'B':
                result.append(row)
                result.append(col)
    return result