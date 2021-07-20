# Sum of numbers 3

def get_sum(x, y):
    s = 0
    if x > y:
        for index in range(y, x + 1):
            s = s + index
        return s
    elif x < y:
        for index in range(x, y + 1):
            s = s + index
        return s
    else:
        return x

print(get_sum(2, 1))
print(get_sum(0, -1))

