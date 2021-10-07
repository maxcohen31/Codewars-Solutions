def remove_duplicate_words(s):
    return ' '.join(list(dict.fromkeys(s.split())))
