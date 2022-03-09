def least_larger(a, i):
    number = a[i]
    result = []
    for index, n in enumerate(a):
        if n > number:
            result.append(n)
    if result == []: 
        return -1
    return a.index(min(result))


# One-liner
def least_larger(a, i):
    return min(((n, index) for index, n in enumerate(a) if n > a[i]), default=(0,-1))[1]


print(least_larger( [4, 1, 3, 5, 6], 0))
print(least_larger([4, 1, 3, 5, 6], 4))
print(least_larger([1, 3, 5, 2, 4], 0))