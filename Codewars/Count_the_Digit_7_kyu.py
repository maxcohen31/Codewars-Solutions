def nb_dig(n, d):
    squared = ''.join([str(i ** 2) for i in range(0, n+1)])
    return squared.count(str(d))

print(nb_dig(25, 1))