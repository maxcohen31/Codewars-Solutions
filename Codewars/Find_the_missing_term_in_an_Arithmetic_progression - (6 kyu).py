def find_missing(arr):
    diff = (arr[-1] - arr[0]) // len(arr)
    for element in range(1, len(arr)):
        if arr[element + 1] - arr[element] != diff:
            return arr[element] + diff
        else:
            arr[0] = arr[element]
        
# Alternative Solution 
def find_missing_2(arr):
    min_arr = arr[0]        
    max_arr = arr[-1]
    return ((min_arr + max_arr) * (len(arr) + 1)) // 2 - sum(arr)    
        
    
    

seq = [1, 3, 5, 9, 11]
print(find_missing_2(seq))
