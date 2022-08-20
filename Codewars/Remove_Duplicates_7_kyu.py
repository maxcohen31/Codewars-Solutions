def unique(integers):
    result = []
    for i in integers:
        if i not in result:
            result.append(i)
    return result



x = [1, 5, 2, 0, 2, -3, 1, 10]
print(unique(x))