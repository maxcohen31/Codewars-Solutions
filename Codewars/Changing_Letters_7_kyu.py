def swap(st):
    tr = str.maketrans('aeiou', 'AEIOU')
    return st.translate(tr)


# Alternative method
def swap2(st):
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in st:
        if letter in vowels:
            result += letter.upper()
        else:
            result += letter
    return result




s = "Hello, World!"
print(swap2(s))