# Not completed

def powers(n):
    tmp = []
    i = 0
    res = []

    while (2 ** i) <= n:
        tmp.append(2 ** i)
        i += 1

    for j in tmp[::-1]:
        if n >= j:
            res.append(j)
            n -= j
    return res[::-1]
