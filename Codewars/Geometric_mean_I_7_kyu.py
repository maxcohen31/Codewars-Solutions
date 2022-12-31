def geometric_meanI(arr: list) -> float:
    gm = 1
    filtered = [n for n in arr if isinstance(n, int) and n >= 0]
    n, n_ = len(arr), len(filtered)
    
    if (len(arr) <= 10 and len(arr) - len(filtered) > 1) or (len(arr) > 10 and len(arr) - len(filtered) > len(arr)*0.1):
        return 0
    
    
    for i in filtered:
        gm *= i
    
    return gm ** (1.0 / len(filtered))

print(geometric_meanI([2, 2, 3, 4, 10, 8, 1, 4, 6, 7, 2]))
# print(geometric_meanI([2, 2, 3, 4, 10, -4, 8, 1, 4, 6, 7, 2, '']))
# print(geometric_meanI([2, 3, 4, 6, '5']))