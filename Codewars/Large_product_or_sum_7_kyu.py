def sum_or_product(array, n):
    array = sorted(array)
    s = 0
    p = 1
    for i in range(n):
        p *= array[i]    
        s += array[len(array) - 1 - i]
    if p == s:
        return 'same'
    elif p > s:
        return 'product'        
    else:
        return 'sum'   
    
    
a = [10, 41, 8, 16, 20, 36, 9, 13, 20]
b = [-10, 42, 5, -7, 3, 18]
c = [-4, -1, 5, -7, -2, 6, 20, 23, 7]
print(sum_or_product(c, 3))

