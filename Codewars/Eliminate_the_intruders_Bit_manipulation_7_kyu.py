def eliminate_unset_bits(number: str) -> int:
    return int(number.replace('0', ''), 2) if number.count('1') >= 1 else 0



    
