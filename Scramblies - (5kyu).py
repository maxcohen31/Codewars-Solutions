def scramble(x, y):
    if len(x) == 0 or len(y) == 0:
        return False
    for letters in set(y):
        if x.count(letters) < y.count(letters):
            return False
    return True

