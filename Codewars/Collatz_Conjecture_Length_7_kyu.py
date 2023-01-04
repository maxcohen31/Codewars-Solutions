def collatz(n: int) -> int:
    collatz_len = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        collatz_len += 1

    return collatz_len 

# Recursion
def collatz(n):
    return 1 if n == 1 else 1 + collatz(3 * n + 1 if n % 2 else n // 2)
