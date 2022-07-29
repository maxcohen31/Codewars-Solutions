from collections import Counter
def two_by_two(animals):
    if animals == []:
        return False
    couples = Counter(animals)
    for k,v in couples.items():
        if v >= 3:
            couples[k] = 2 
    
    return {k:v for k,v in couples.items() if v == 2}

a = ["dog", "cat", "dog", "cat", "beaver", "cat"]
print(two_by_two(a))