from typing import List
def min_min_max(arr: List[int]) -> List[int]:
    new_arr = sorted(arr)
    mid = []

    for i in range(new_arr[0], new_arr[-1]):
        if i not in new_arr:
            mid.append(i)
    
    return [min(new_arr), min(mid), max(new_arr)]
    


x = [-1, 4, 5, -23, 24]
print(min_min_max(x))