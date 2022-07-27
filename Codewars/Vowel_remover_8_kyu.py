def shortcut(s: str):
    vowels = 'aeiouy'
    for v in vowels:
        s = s.replace(v, "")
    return s
