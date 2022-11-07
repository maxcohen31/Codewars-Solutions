import re
def filter_string(string):
    #your code here
    numbers = re.findall(r"[0-9]", string)
    return int(''.join(numbers))


a = "a1b2c3"
print(filter_string(a))