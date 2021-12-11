def sum_fibs(n):
    fibo = []
    a, b = 0, 1
    even_sum = 0
    for i in range(2, n+1):
        a, b = b, a+b
        fibo.append(b)    
    for x in fibo:
        if x % 2 == 0:
            even_sum = even_sum + x
    return even_sum        
print(sum_fibs(9))