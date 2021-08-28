def grabscrab(word, possible_words):
    words = []
    word_dict = {w:word.count(w) for w in word}
    for word in possible_words:
        poss_word = {k:word.count(k) for k in word}
        if word_dict == poss_word:
            words.append(word)
    return words
    
    
w = ["sport", "parrot", "ports", "matey"]    
s = 'ortsp'
print(grabscrab(s, w))
