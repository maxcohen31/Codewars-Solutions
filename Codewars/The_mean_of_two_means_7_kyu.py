from typing import List

def get_mean(arr: List[int], x: int, y: int) -> int|float:
    first_mean = sum(arr[0:x]) / len(arr[0:x])
    second_mean = sum(arr[-y:]) / len(arr[-y:])
    
    if (x > 1 and y > 1) and (x <= len(arr) and y <= len(arr)):
        return (first_mean + second_mean) / 2
    return -1     


