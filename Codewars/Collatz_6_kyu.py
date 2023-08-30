def collatz(n: int) -> str:
    col = [n]
    while(n != 1):
        if n % 2 == 0:
            col.append(n//2)
            n //= 2
        elif n % 2 == 1:
            col.append(3*n + 1)
            n = 3 * n + 1
    return "->".join(str(i) for i in col)


print(collatz(3))
    #your code here
