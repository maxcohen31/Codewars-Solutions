# IQ test

def iq_test(numbers):
    even = []
    odd = []
    # Main loop
    for i, c in enumerate(numbers.split(), start = 1):
        if int(c) % 2 == 0:
            even.append(i)
        elif int(c) % 2 != 0:
            odd.append(i)
    return even, odd

print(iq_test('2 4 7 8 10 11'))

