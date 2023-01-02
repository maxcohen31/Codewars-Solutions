def matrix(array): 
    a = array
    for row in range(len(a)):
        for col in range(len(a[0])):
            if row == col:
                if a[row][col] < 0:
                    a[row][col] = 0
                else:
                    a[row][col] = 1
    return a