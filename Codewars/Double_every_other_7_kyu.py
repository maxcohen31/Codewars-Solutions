def double_every_other(lst):
    new_lst = []
    for i, n in enumerate(lst):
        if i % 2 == 0:
            new_lst.append(n) 
        elif i % 2 != 0:
            new_lst.append(2*n)                
    return new_lst    
        
# List comprehension
def double_every_other2(lst):
    return [n * 2 if i % 2 != 0 else n for i, n in enumerate(lst)] 
        
arr = [1,2,3,4]
print(double_every_other2(arr))