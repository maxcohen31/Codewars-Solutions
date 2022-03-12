import re
def is_vowel(s): 
    if len(s) > 1:
        return False
    elif len(s) == 1 and s[0] in re.findall(r"^[aeiouAEIOU]", s):
        return True
    else:
        return False

