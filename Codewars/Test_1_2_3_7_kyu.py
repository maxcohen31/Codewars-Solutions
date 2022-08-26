def number(lines):
    
    s = ''
    result = []
    indexes = [idx for idx, val in enumerate(lines, start=1)]
    zipping = zip(lines, indexes)

    for i, j in zipping:
        s = f"{j}: {i}"
        result.append(s)
    return result

print(number(["a", "b", "c"]))