def show_sequence(n: int) -> str:
    sequence = ""
    result = 0
    if n == 0:
        return "0=0"
    elif n < 0:
        return f"{n}<0"
    for i in range(0, n+1):
        result += i
        sequence += f"+{i}"
    return f"{sequence} = {result}"[1:]


print(show_sequence(6))