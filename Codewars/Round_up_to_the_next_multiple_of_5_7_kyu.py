def is_multiple(m: int) -> bool:
    if m % 5 != 0:
        return False
    return True

def round_to_next5(n: int) -> int:
    while not is_multiple(n):
        n += 1
    return n


print(round_to_next5(7))