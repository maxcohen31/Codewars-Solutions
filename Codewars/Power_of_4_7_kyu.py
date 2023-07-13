def powerof4(n: int) -> bool:
    if not isinstance(n, int) or isinstance(n, bool):
        return False    
    if n <= 0 and isinstance(n, int):
        return False
    while n > 1:
        if n % 4 != 0:
            return False
        n //= 4
    return True

if __name__ == "__main__":
    a = 6 
    print(powerof4(a))
