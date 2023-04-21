def even_and(a: int) -> bool:
    return a & 1 != 1

def even_or(a: int) -> bool:
    return a + 1 == a | 1

def even_xor(a: int) -> bool:
    return a ^ 1 != a - 1

def even_shift(a: int) -> bool:
    return (a >> 1) << 1 == a

def is_even(n: int) -> bool:
    operators = ["AND", "OR", "XOR", "SHIFT"]
    for op in operators:
        if op == "ADD":
            even_and(n)
        elif op == "OR":
            even_or(n)
        elif op == "XOR":
            even_xor(n)
        elif op == "SHIFT":
            even_shift(n)



print(is(4))