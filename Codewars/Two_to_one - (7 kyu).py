def longest(a1, a2):
    set_a = set(a1)
    set_b = set(a2)
    long = sorted(set_a.union(set_b))
    return ''.join(long)
    
    
    