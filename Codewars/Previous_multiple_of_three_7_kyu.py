def prev_mult_of_three(n: int):
    if n % 3 == 0:
        return n
    else:
        try:
            number = [i for i in str(n)[:-1]]
            return prev_mult_of_three(int(''.join(number)))    
        except ValueError:
            return None


# Solution 2
def prev_mult_of_three2(n: int):
    if n % 3 == 0:
        return n
    elif n == 0:
        return None
    else:
        return prev_mult_of_three2(n // 10)


a = 952406
b = 12
print(prev_mult_of_three2(a))
