import re
def reverse_letter(string):
    word = re.findall(r"[A-Za-z]", string)
    return ''.join(word)[::-1]



string = "ultr53o?n"
print(reverse_letter(string))