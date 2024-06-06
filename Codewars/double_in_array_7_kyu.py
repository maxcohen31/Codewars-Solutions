"""
    given an array of n integers, write an algorithm to check if there is one doubled element.
    
    Lower bound: Omega(n)
    Upper bound: O(nlogn)

"""

from typing import List

def check_double(array: List[int]) -> bool:

    d = {}

    for i in array:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    for val in d.values():
        if val == 2:
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 4, 4, 5];
    print(check_double(a))
