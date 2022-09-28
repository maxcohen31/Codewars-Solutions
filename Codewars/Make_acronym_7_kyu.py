def to_acronym(inp):
    return ''.join([i.upper()[0] for i in inp.split()])


s = "Code Wars"
print(to_acronym(s))