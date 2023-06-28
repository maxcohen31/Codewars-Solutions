from typing import List

def dominator(arr: List[int]) -> int:
    half = len(arr) // 2
    for val in arr:
        if arr.count(val) > half:
            return val
    return -1

a = [3,4,3,2,3,1,3,3]
b = [1,1,1,2,2,2]

print(dominator(b))
