from functools import lru_cache

@lru_cache(maxsize=None)
def last_fib_digit(n):
    n = n % 60
    if n <= 1:
        return n
    else:
        return (last_fib_digit2(n-1) + last_fib_digit2(n-2)) % 10 

# Clever Solution
def last_fib_digit(n):
    n = n % 60
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b % 10    

print(last_fib_digit(9000000008))