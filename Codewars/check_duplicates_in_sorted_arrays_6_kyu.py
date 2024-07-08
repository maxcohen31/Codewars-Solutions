"""
    Given an array of sorted integers >= 0, write an divide-et-impera algorithm 
    to check if thare are any duplicates.
    
    Exercise from Algorithm and DS class.

    Yep, not a Codewars kata.
"""

from typing import List
from math import floor

def check_duplicates(arr: List[int]) -> bool:
    def binary_search(l: int, r: int):
        if (l >= r):
            return False
        else:
            mid = floor((l + r) / 2)
            
            # Check if mid is equal to the previous element or the next one
            if (arr[mid] == arr[mid+1] or arr[mid] == arr[mid-1]):
                return True
            else:
                return binary_search(l, mid) or binary_search(mid+1, r)

    return binary_search(0, len(arr) - 1)


if __name__ == "__main__":
    a = [1, 3, 6, 8]
    print(check_duplicates(a))
