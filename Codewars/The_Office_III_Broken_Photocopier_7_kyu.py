def broken(inp):
    
    inp = list(inp)
    result = []
    for b in inp:
        if b == '0':
            b = '1'
        elif b == '1':
            b = '0'
        result.append(b)
    return ''.join(result)

print(broken('001111110011001110101111101001'))