from math import sqrt
from typing import List

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime(n: int) -> List[int]:
    result = []
    for p in range(2, n+1):
        if is_prime(p):
            result.append(p)
    return result

print(prime(5))
    