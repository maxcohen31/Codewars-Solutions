from functools import lru_cache

@lru_cache(100000)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))