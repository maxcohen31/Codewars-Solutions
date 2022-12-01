import re
def unscramble_eggs(word):
    # Geggoodegg Legguceggkegg!
    return re.sub(r"egg", '', word)


print(unscramble_eggs("Beggegeggineggneggeregg"))