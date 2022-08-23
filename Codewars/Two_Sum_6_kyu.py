def two_sum(numbers: list, target: int) -> list:
    result = {}
    
    for idx, val in enumerate(numbers):
        if target - val in result:
           return [result[target - val], idx]    
        result[val] = idx
    return result


print(two_sum([1, 2, 3], 4))