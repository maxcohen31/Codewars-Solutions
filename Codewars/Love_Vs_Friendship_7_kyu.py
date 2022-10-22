from string import ascii_lowercase
def words_to_marks(s):
    # Easy one
    result = 0
    s = list(s)
    alphabet = dict(zip(ascii_lowercase, list(range(1, 27))))
    for char in s:
        for k,v in alphabet.items():
            if k == char:
                result += v
    return result


l = 'love'
a = 'attitude'
print(words_to_marks(a))