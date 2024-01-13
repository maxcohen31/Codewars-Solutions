"""
    You are given a 32-bit integer n. 
    Swap each pair of adjacent bits in its binary representation and return the result as a decimal number.

    The potential leading zeroes of the binary representations have to be taken into account, 
    e.g. 0b100 as a 32-bit integer is 0b00000000000000000000000000000100 and is reversed to 0b1000.
"""

def swap_adjacent_bit(n: int):
    # We nedd to take into account leading zeros
    binary = list(bin(n)[2:].zfill(32))

    for bit in range(0, len(binary) - 1, 2):
        binary[bit], binary[bit+1] = binary[bit+1], binary[bit]
    return int("".join(binary), 2)


