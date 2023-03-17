def hyperfact(num: int) -> int:
    hyperfac = 1 
    
    for i in range(1, num+1):
        hyperfac *= pow(i, i)
    return hyperfac if num <= 5 else hyperfac % 1000000007
n = 6
print(hyperfact(n))
