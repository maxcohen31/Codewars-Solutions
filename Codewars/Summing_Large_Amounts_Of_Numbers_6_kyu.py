def sum_them(n):
    """This function works for small n.
    But small n isn't enough!"""
    #total = 0
    # for x in range(2 ** n):
    #    total += (x ^ (x // 2))
    #return total

    return ((2**n - 1)) * ((2**n - 1 + 1)) // 2 

print(sum_them(12))