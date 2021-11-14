def generate_shape(n):
    row = [n * '+' for i in range(n)][-1]
    return row + ('\n' + row) * (n-1) 

