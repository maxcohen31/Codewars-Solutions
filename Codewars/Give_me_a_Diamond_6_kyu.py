def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    make_diamond = ''
    make_diamond2 = ''
    for i in range(1, n, 2):
        make_diamond += " " * ((n - i) // 2) + "*" * i + "\n" 
    for j in range(n, 0, -2):
        make_diamond2 += " " * ((n - j) // 2) + "*" * j + "\n"
    return make_diamond + make_diamond2[:-1] + '\n'

print(diamond(7))