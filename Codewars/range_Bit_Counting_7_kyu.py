def range_bit_counting(a, b):
    result = 0
    range_bit = [i for i in range(a, b+1)]
    to_binary = [bin(i)[2:] for i in range_bit]
    
    for binary in to_binary:
        result += binary.count('1')
    return result


# Quicker sol
def range_bit_count(a, b):
    return sum(bin(i).count('1') for i in range(a, b+1))


if __name__ == "__main__":
    print(range_bit_counting(2, 7))
