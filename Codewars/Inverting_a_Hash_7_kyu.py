def invert_hash(dictionary: dict) -> dict:
    return {v:k for k, v in dictionary.items()}


print(invert_hash({'a':1, 'b':2, 'c':3}))