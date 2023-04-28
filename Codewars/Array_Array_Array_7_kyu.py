from typing import List

def explode(arr: List[str|int]|List[int|int]|str) -> List[List[int|int]]|List[List[str|int]]|str:  
    integer = 0
    string = 0
    result = [arr[:]]

    for idx, val in enumerate(arr):
        if isinstance(val, str):
            string += 1
        elif isinstance(val, int):
            integer += 1
    
    if string == 1 and integer == 1:
        if isinstance(arr[1], int):
            result = [arr] * arr[1]
        else:
            result = result * arr[0]
    elif integer == 2:
        result = result * sum(arr)
    elif string == 2:
        return "Void!"
    return result

print(explode(['a', 3]))
print(explode([6, 'c']))
# print(explode([9, 3]))