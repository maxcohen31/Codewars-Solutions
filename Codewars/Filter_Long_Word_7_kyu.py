def filter_long_words(sentence, n):
    return [word for word in sentence.split() if len(word) > n]

