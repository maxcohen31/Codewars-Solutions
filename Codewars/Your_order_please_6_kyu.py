import re
def order(sentence):
    result = []
    pattern = re.findall(r"\d", sentence)          
    a = sorted(pattern)
    for number in a:
        for word in sentence.split():
            if number in word:
                result.append(word)
    return ' '.join(result)

print(order("W0uld Valentin5e b2 m4 you1"))