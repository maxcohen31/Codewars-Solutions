def sum_of_n(n):
    if n < 0:
        return sorted([sum(x for x in range(i,1)) for i in range(n, 1)], reverse=True)
    else:
        return [sum([x for x in range(i+1)]) for i in range(n+1)]

# Alternative Solution
def sum_of_n2(n):
    if n > 0:
        sum_n = 0
        new_list = []
        for i in range(0, n+1):
            sum_n += (i + 1) - 1
            new_list.append(sum_n)
        return new_list

    elif n < 0:
        sum_n2 = 0
        new_list2 = []
        for i in range(0, n-1, -1):
            sum_n2 += (i - 1) + 1
            new_list2.append(sum_n2)   
    return new_list2
    
print(sum_of_n2(5))