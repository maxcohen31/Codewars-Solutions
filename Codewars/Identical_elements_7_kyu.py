def duplicate_elements(m, n):
    for i in m:
        for j in n:
            if i == j:
                return True
    return False        





a = [0, 2, 3]
b = [1, 5, 7]
print(duplicate_elements(a, b))