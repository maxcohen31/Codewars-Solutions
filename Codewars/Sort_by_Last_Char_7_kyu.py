def last(s):
    s = s.split()
    return sorted(s, key=lambda s: s[-1])


x = "man i need a taxi up to ubud"
c = "take me to semynak"
print(last(c))