def fib_rabbits(n, b):
    s, t = 0, 1
    if n == 0:
        return 0
    if b == 0:
        return 1
    for _ in range(2, n+1):
        rabbits = s + t
        s = t * b
        t = rabbits 
    return t
    
print(fib_rabbits(5, 3))