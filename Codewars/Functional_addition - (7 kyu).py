def add(i):
    def add2(j):
        return i + j
    return add2



add_one = add(1)
print(add(3))