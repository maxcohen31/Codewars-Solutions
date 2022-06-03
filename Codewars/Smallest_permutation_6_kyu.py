def min_permutation(n):
    if n == 0:
        return n
    elif n > 0:
        n = str(n)
        numb_of_zeros = n.count('0')
        new_n = n.replace('0', '')
        perm = ''.join(sorted(list(new_n)))
        return int(perm[0] + (numb_of_zeros * '0') + perm[1:])
    elif n < 0 and str(n)[:-1] == '0':
        return n
    elif n < 0:
        n = str(n)
        numb_of_zeros = n.count('0')
        new_n = n.replace('0', '').replace('-', '')
        perm = ''.join(sorted(list(new_n)))
        return -1 * int(perm[0] + (numb_of_zeros * '0') + perm[1:])
    

print(min_permutation(9125660530))

