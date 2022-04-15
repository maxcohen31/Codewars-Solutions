def solve(n):
    r = 0
    notes = [10, 20, 50, 100, 200, 500]
    for idx, note in enumerate(reversed(notes)):
        r += n // note
        n %= note
    if n % note != 0:
        return -1
    return r

print(solve(770))
