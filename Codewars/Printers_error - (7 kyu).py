import string
def printer_error(s):
    letters = 0
    for letter in s:
        if letter not in string.ascii_lowercase[0:13]:
            letters += 1
    return f'{letters}/{len(s)}'              


 