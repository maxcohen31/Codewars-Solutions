def mygcd(x, y):
    if x > y:
        div = x // y
        while y != 0:
            x, y = y, x%y
        return x    
    elif x < y:
        div = y // x
        while x != 0:
            y, x = x, y%x
        return y
    return 1
    
print(mygcd(8, 9))