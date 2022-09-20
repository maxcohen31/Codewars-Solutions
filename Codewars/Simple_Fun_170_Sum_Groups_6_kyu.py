from itertools import groupby
def get_even(n):
    return True if n % 2 == 0 else False

def sum_groups(arr):
    # one element array
    if len(arr) == 1:
        return 1
    
    # Groupby function 
    iterator = groupby(arr, get_even)
    result = [sum(elements) for key, elements in iterator]

    return len(result) if len(result) == len(arr) else sum_groups(result)
    
    

print(sum_groups([1,1,2,2]))
print(sum_groups([2, 1, 2, 2, 6, 5, 0, 2, 0, 5, 5, 7, 7, 4, 3, 3, 9]))