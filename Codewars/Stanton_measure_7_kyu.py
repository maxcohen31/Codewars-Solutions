def stanton_measure(arr):
    count_one = 0
    stanton = 0
    for a in arr:
        if a == 1:
            count_one += 1
    for i in arr:
        if i == count_one:
            stanton += 1
    return stanton      
            
s = [1, 4, 3, 2, 1, 2, 3, 2]        
print(stanton_measure(s))             


