def switcheroo(string: str) -> str:
    return string.replace('a', '*').replace('b', 'a').replace('*', 'b')

# Alternative sol
def switcheroo(string):
    #your code here
    result = ''
    for letter in string:
        if letter == 'a':
            letter = 'b'
        elif letter == 'b':
            letter = 'a'
        result += letter
    return result