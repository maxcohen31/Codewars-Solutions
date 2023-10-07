from typing import List

def first_reverse_try(arr: List[int]) -> List[int]:
    first = arr[0]
    last = arr[-1]
    
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    
    return [last] + arr[1:-1] + [first] 
