def find_nb(m):
    cubes = 0
    tot = 0
    while tot < m:
        cubes += 1
        tot += cubes ** 3
        if tot == m:
            return cubes
    return -1

print(find_nb(1071225))    