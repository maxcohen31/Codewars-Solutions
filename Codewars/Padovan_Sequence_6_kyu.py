def padovan(n):
    if n == 0 or n == 1 or n == 2:
        return 1

    if n >= 3:
        a = 1
        b = 1
        c = 1
        d = 1
        for _ in range(3, n+1):
           d = a + b
           a = b
           b = c
           c = d
        return d

# Alternative Solution
def padovan2(n):
    pad = [1, 1, 1]
    while len(pad) < n+1:
        pad.append(pad[-2] + pad[-3])
    return pad[-1]

# Alternative Solution
from functools import lru_cache

@lru_cache(maxsize=None)
def padovan3(n):
    if n < 3:
        return 1
    return padovan(n-2) + padovan(n-3)

