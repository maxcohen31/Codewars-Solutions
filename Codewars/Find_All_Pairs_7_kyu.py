from collections import Counter
def duplicates(arr):
    count = 0
    new = Counter(arr)
    
    for k, v in new.items():
        if v >= 2 and v % 2 == 0:
            count += v // 2
        elif v >= 2 and v % 2 != 0:
            count += v // 2
    return count
    


print(duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]))
print(duplicates([0, 0, 0, 0, 0, 0, 0]))