def capitals(word):
    result = []
    for i in range(len(word)):
        if word[i].isupper():
            result.append(i)
    return result


s = 'CodEWaRs'
print(capitals(s))