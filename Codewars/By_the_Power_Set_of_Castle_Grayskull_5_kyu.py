from itertools import combinations
from typing import List

def power(a: List[int]) -> List[List[int]]:
    result = [[]]
    for n in range(1, len(a)+1):
        result += combinations(a, n)
    return result

print(power([1, 2, 3, 4]))