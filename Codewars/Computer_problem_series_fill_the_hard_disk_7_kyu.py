def save(sizes, hd): 
    result = 0
    for i, a in enumerate(sizes):
        result += sizes[i]
        if result > hd:
            return i
    return len(sizes)
    
# Alternative solution    
def save(sizes, hd): 
    while sum(sizes) > hd:
        sizes.pop()
    return len(sizes)

    
a = [4,4,4,3,3]
b = [4,8,15,16,23,42]
c = [100]
print(save(a, 12))