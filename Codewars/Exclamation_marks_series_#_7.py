# Remove words from the sentence if they contain exactly one exclamation mark. 
# Words are separated by a single space, without leading/trailing spaces.

def remove(s):
    result = []
    new_s = list(s.split())
    for element in new_s:
        if element.count('!') == 0 or element.count('!') > 1:
            result.append(element)
    return ' '.join(result)

s = 'Hi Hi! Hi!'
print(remove(s))