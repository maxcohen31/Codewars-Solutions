def pofi(n):    
    cycle = {0: '1', 1: 'i', 2: '-1', 3: '-i'}
    return cycle.get(n%4)

print(pofi(6))            