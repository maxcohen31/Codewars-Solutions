def get_last_digit(index: int) -> int:
    a = 1
    b = 1
    c = 0

    for _ in range(2, index):
        c = a + b 
        a = b
        b = c
    return c % 10


