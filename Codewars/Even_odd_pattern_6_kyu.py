def even_odd(arr):
    tot = 0
    for i, element in enumerate(arr):
        if i % 2 != 0:
            tot *= element  
        else:
            tot += element    
    return tot        
            
lst = [2, 2, 2, 4]
print(even_odd(lst))

# [1,2,2,1,6,1,3,9,6,1] => 0*1+2 = 2+2 =4*1 = 4+6 =10*1=10+3 =13*9=117+6=123*1=123   