def fibonacci(n: int) -> int:
    """Given a positive argument n, returns the nth term of the Fibonacci Sequence.
    """
    # low performance
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # else:
    #     return fibonacci(n-2) + fibonacci(n-1)
    
    a = 0
    b = 1
    result = [0, 1]
    
    for i in range(n):
        c = a + b
        a = b
        b = c 
        result.append(c)
    return result[n]
    
print(fibonacci(6))