def expanded_form(num):
    expanded_number = []
    num = [i for i in str(num)]
    for i, n in enumerate(num[::-1]):
        if n != '0':
            expanded_number.append(n + str(i * '0'))
    return ' + '.join(expanded_number[::-1])
    
x = 70304
a = 12
print(expanded_form(x))