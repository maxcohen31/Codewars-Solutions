from string import ascii_lowercase, ascii_uppercase
def consonant_count(s: str) -> int:
    counter = 0
    alpha = ascii_lowercase + ascii_uppercase
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for l in s:
        if l in alpha and l not in vowels:
            counter += 1
    return counter


x = 'helLo world'
print(consonant_count(x))


