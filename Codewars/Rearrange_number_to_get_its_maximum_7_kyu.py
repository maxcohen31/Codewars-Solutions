def max_redigit(num): 
    num = str(num)
    maximum = ''.join(sorted(num))
    if len(num) == 3 and int(num) > 0:
        return int(maximum[::-1])


# Solution 2
def max_redigit2(num):
    if 99 < num < 1000 and isinstance(num, int):
        return int(''.join(sorted(str(num))))
