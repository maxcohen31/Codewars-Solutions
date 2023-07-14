def is_divisible(*args) -> bool:
    numbs = [arg for arg in args]
    result = []
    for n in numbs:
        if numbs[0] % n == 0:
            result.append(1)
        else:
            result.append(0)
    return all(result)
