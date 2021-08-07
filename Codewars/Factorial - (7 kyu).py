def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    if n == 0:
        return 1
    elif n > 0:
        molt = 1
        for i in range(1, n+1):
            molt = molt * i 
        return molt
    
print(factorial(5))
