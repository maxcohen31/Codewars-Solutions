def parts_sums(ls):
    ls = ls[:]
    result = [0]   
    s = 0
    for i in ls[::-1]:
        s += i
        result.append(s)
    return result[::-1]

ls = [0, 1, 3, 6, 10]
l =[1, 2, 3, 4, 5, 6]
print(parts_sums(l)) # [20, 20, 19, 16, 10, 0]

n = sum(ls)
for i in ls:
    n = n - i
    print(i, n-i, n)

# ls = [0, 1, 3, 6, 10]
# ls = [1, 3, 6, 10]
# ls = [3, 6, 10]
# ls = [6, 10]
# ls = [10]
# ls = []