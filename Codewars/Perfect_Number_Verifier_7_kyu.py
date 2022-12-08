#Should return whether or not n is a perfect number
def is_perfect(n: int) -> bool:
    perfect_numbs = [6, 28, 496, 8128, 33550336, 8589869056]
    if n in perfect_numbs:
        return True
    return False


print(is_perfect(3))