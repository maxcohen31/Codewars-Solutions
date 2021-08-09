def divisors(n):
    divs = []
    for i in range(1, n+1):
        if n % int(i) == 0:
            divs.append(i)
    return len(divs)
            
# print(divisors(12))

def divisors_2(n):
    return len([i for i in range(1, n+1) if n % int(i) == 0])



print(divisors_2(12))