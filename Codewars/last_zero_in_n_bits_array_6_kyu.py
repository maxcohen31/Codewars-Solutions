"""
    Given a sorted array of zeros and ones, write an algorithm that return the index of the last zero.

    Example: [0, 0, 0, 1, 1, 1, 1] - result = 2

    Complexity: O(logn)
    
"""

from math import floor
from typing import List

def find_last_zero(a: List[int], l: int, r: int) -> int:
    if (l < r):
        mid: int = floor((l + r) / 2)

        if a[mid] == 0:
            if a[mid+1] == 1 or mid == r:
                return mid

        if a[mid] > 0:
            return find_last_zero(a, l, mid)

        else:
            return find_last_zero(a, mid+1, r)

    return -1

if __name__ == "__main__":
    x = [0, 0, 0, 1, 1, 1, 1] 
    x1 = [0, 1, 1, 1, 1] 
    x2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    print(find_last_zero(x, 0, len(x) - 1))
    print(find_last_zero(x1, 0, len(x1) - 1))
    print(find_last_zero(x2, 0, len(x2) - 1))
