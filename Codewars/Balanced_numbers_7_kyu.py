def balanced_num(number):
    number = [int(n) for n in str(number)]
    if len(number) <= 2:
        return 'Balanced'
    elif len(number) % 2 == 0:
        if sum(number[:(len(number) // 2) - 1]) == sum(number[(len(number) // 2) + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'
    else:    
        if sum(number[:(len(number) // 2)]) == sum(number[(len(number) // 2) + 1:]):
            return 'Balanced'
        else:
            return 'Not Balanced'       


a = 295591
b = 959
print(balanced_num(b))