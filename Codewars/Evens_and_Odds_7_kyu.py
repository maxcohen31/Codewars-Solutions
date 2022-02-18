def evens_and_odds(n):
    return bin(n)[2:] if n % 2 == 0 else hex(n)[2:]