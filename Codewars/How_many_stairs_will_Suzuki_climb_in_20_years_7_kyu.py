from typing import List

def stairs_in_20(stairs: List[List[int]]) -> int:
    result = 0
    for i in stairs:
        for j in i:
            result += j
    return result * 20


# One-liner
def stairs_in_20(stairs: List[List[int]]) -> int:
    return sum([i for day in stairs for i in day]) * 20
