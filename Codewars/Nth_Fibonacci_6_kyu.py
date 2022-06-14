def nth_fib(n: int) -> int:
    a, b = 0, 1
    result = [0, 1]
    for i in range(n):
        c = a + b
        a = b
        b = c
        result.append(c)
    return result[n-1]


print(nth_fib(43))