from typing import List
def consecutive(arr: List[int]) -> int: 
    if len(arr) in [0, 1]: return 0
    sorted_arr = sorted(arr)
    full_arr = list(range(sorted_arr[0], sorted_arr[-1]+1))
    return len(full_arr) - len(sorted_arr)


