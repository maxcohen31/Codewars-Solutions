# Bit Counting

def bit_count(n):
    x = bin(n)
    count = 0
    for i in x:
        if i == '1':
            count += 1
    return count

print(bit_count(9))

