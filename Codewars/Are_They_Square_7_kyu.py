def is_square(arr: list) -> bool:
    a = arr
    
    squared = [i**2 for i in range(1000)]
    for i in a:
        if i not in squared:
            return False
    return True

# Alternative Sol.
from math import isqrt

def is_square2(a):
    if a:
        return all(isqrt(x)**2 == x for x in a)

print(is_square([1, 2, 3]))
        