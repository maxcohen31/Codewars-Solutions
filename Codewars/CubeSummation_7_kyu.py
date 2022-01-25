def cube_sum(n, m):
    n, m = sorted([n, m])
    return sum([i ** 3 for i in range(n + 1, m + 1)])
    
def cube_sum2(n, m):
    return sum([i ** 3 for i in range(m+1, n+1) if n > m]) or sum([i ** 3 for i in range(n+1, m+1) if n < m]) 
    
 