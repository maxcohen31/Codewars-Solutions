def largest(n,xs):
    result = []
    for i in range(n):
        result.append(max(xs))
        xs.remove(max(xs))
    return sorted(result)




s = [1, 2, 3, 6, 7] # [6, 7]
print(largest(2, s))
