import re
def decipher(cipher):
    result = []
    m = re.findall(r'9\d{1}|1\d{2}', cipher)
    for element in m:
        result.append(chr(int(element)))
    return ''.join(result)    

