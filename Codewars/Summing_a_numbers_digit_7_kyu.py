def sum_digits(n):
    return sum([int(x) for x in str(abs(n))])
    


print(sum_digits(10))