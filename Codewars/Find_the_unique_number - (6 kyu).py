def find_uniq2(arr):
    unique = filter(lambda x: arr.count(x) == 1, set(arr))
    a = list(unique)
    return a[0]



def find_uniq(arr):
    for unique in set(arr):
        if arr.count(unique) == 1:
            return unique
    
    
