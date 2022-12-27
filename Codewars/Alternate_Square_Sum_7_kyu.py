def alternate_sq_sum(arr: list) -> int:
    sum_ = 0
    
    for idx in range(len(arr)):
        if idx % 2 != 0:
            sum_ += pow(arr[idx], 2)
        else:
            sum_ += arr[idx]
    return sum_

print(alternate_sq_sum2([11, 12, 13, 14, 15]))