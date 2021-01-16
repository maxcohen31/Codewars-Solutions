# Array Difference

def array_diff(a, b):
    l1 = []

    if len(a) > len(b):
        for c in a:
            if c not in b:
                l1.append(c)
        return l1

    elif len(a) == 0 and len(b) > 0:
        return a

    elif len(a) < len(b):
        for i in a:
            if i not in b:
                l1.append(i)
        return l1

x = [3, 10]
y = [15, 16, -17, -16, 20]
print(array_diff(x, y))
