def count_squares(n):
    # since is a sum of squares...
    return (n*(n+1)*(2*n+1)) // 6
    

def count_squares2(n):
    return sum([i*i for i in range(n+1)]) 


print(count_squares(1000000))