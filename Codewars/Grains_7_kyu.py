def square(number):
    i = 1
    for n in range(1, number):
        number = number * i
        i *= 2
    return i    