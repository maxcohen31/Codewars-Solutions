def starts_with(st, prefix): 
    
    if len(prefix) > len(st):
        return False
    
    if prefix == '' and len(st) > 0:
        return True
    elif prefix == '' and st == '':
        return True

    if st[0] == prefix[0] or prefix in st:
        return True
    return False
    
# Solution 2
def starts_with2(st, prefix): 
    return st.startswith(prefix)

# Solution 3
def starts_with3(st, prefix): 
    return st[:len(prefix)] == prefix




print(starts_with(" hello world!", " hello"))
print(starts_with3('hello', 'he'))
print(starts_with("nowai", "nowaisir"))