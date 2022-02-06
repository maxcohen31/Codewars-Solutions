import re         
def remove(s):
    return re.sub('!+$', '', s)
    