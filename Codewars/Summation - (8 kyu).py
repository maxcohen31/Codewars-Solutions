# Summation

def summation(n):
    
    start = 0
    for x in range(1, n + 1):
        start = start + x
    return start
        

print(summation(8))