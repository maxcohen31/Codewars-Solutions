from typing import List

def max_diff(lst: List[int]) -> int:
    if len(lst) in [0, 1]:
        return 0
    
    max_numb = max(lst)
    min_numb = sorted(lst)[0]

    if min_numb <= 0:
        return max_numb - min_numb if min_numb < 0 else max_numb + min_numb
    return max_numb - min_numb


x = [-0, 1, 2, -3, 4, 5, -6]
print(max_diff(x))

