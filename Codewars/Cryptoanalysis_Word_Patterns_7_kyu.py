def word_pattern(word: str) -> str:
    letters = []
    result = ""
    new_word = list(word.lower())
    
    for w in new_word:
        if w not in letters:
            letters.append(w)
        result += str(letters.index(w)) + '.'
    return result[0:-1]

x = "Hippopotomonstrosesquippedaliophobia"
print(word_pattern(x))
