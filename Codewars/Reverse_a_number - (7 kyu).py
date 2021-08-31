def reverse_number(numb):
    if numb > 0:
        return int(str(numb)[::-1])
    else:
        return -1 * int(str(numb * -1)[::-1])
       

n = -456
print(reverse_number(n))