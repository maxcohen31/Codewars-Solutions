def cycle(n):
    count = 0
    div = 1
    if n % 2 == 0 or n % 5 == 0:
        return -1
    
    while True:
        div = (div * 10) % n
        count += 1 
        if div == 1:
            break
    return count

# Better Sol
def cycle(n) :
    if n % 2 == 0 or n % 5 ==0:
        return -1
    k = 1
    while pow(10,k,n) != 1:
        k += 1
    return k


print(cycle(13))