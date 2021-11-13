# Solution
def validate_word(word):
    word_low = word.lower()
    d = {a:word_low.count(a) for a in word_low}
    d_check = list(d.values())[0]
    for i in d:
        if d[i] != d_check:
            return False
    return True


# Alternative solution
def validate_word2(word):
    word = word.lower()
    return len(set(word.count(i) for i in word)) == 1

