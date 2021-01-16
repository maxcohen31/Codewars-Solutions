import string

# Pangram

def is_pangram(s):

    ascii_var = string.ascii_lowercase
    for c in ascii_var:
        if c not in s.lower():
            return False
    return True

print(is_pangram('the quick brown fox jumps over the lazy dog'))

