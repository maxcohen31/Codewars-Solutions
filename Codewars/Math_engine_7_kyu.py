from typing import List

def math_engine(arr: List[int]) -> int:
    if arr is None: return 0 

    pos_product = 1
    neg_sum = 0

    for val in arr:
        if val >= 0:
            pos_product *= val
        else:
            neg_sum += val
    return pos_product + neg_sum
    
