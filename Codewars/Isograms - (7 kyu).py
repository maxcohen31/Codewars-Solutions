def is_isogram(string):
    new_string = string.lower()
    if string == '':
        return True
    letters = {letter: new_string.count(letter) for letter in new_string}
    for value in letters.values():
        if value > 1:
            return False
    return True
         
