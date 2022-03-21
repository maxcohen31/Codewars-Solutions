from collections import Counter
def find_uniq(arr):
    arr_dict = Counter(arr)
    for k, v in arr_dict.items():
        if v == 1:
            return k

    
x = [ 1, 1, 1, 2, 1, 1 ]
print(find_uniq(x))

