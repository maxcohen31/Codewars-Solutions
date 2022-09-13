def max_product(lst, n_largest_elements):
    lst = sorted(lst[:], reverse=True)
    new = lst[0:n_largest_elements]
    mult = 1
    for i in new:
        mult *= i
    return mult
    

print((max_product([-4,-27,-15,-6,-1],2))) # 4 = -1 * -4