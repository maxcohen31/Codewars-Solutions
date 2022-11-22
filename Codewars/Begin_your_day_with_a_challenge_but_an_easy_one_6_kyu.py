def one_two_three(n):
    if n == 0:
        return [0, 0]
    else:
        x, y = divmod(n, 9)
        if y != 0:
            result = [('9' * x) + str(y), '1' * n]
        else:
            result = [('9' * x), '1' * n]
        return [int(i) for i in result]

print(one_two_three(157))