def nth_char(words):
    result = ""
    for idx, word in enumerate(words):
        result += word[idx]
    return result








c = ["yoda", "best", "has"] 
print(nth_char(c))