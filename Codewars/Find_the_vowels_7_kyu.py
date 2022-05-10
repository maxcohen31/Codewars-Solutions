def vowel_indices(word):
    result = []
    new_word = list(word)
    vowels = 'aeyiouAEIYOU'
    for idx, vow in enumerate(new_word, start=1):
        if vow in vowels:
            result.append(idx)
    return result

