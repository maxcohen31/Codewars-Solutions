# LETTERS is preloaded
  
def nato(word):
    
    word = [w.upper() for w in word]
    result = []
    for w in word:
        for k, v in LETTERS.items():
            if k == w:
                result.append(v)
    return ' '.join(result)


# Alternative Solution
def solution2(word):
    return ' '.join(LETTERS[i] for i in word.upper())

s = "abc"
z = "babble"
print(nato(z))