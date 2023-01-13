def cyclops(n: int) -> bool:
    binary = bin(n)[2:]
    binary_to_string = str(binary)

    if '0' not in binary_to_string:
        return False

    index_zero = str(binary).index('0')


    first_part = binary_to_string[:index_zero]
    second_part = binary_to_string[index_zero+1:]

    return first_part == second_part




    
    



print(cyclops(3))