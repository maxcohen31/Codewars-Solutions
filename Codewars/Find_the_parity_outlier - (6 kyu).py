def find_outlier(integers):
    even = []
    odd = []
    for n in integers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    if len(even) > len(odd):
         return odd[0]
    else:
        return even[0]


x = [2, 4, 0, 100, 4, 11, 2602, 36]
y = [160, 3, 1719, 19, 11, 13, -21]
print(find_outlier(x))