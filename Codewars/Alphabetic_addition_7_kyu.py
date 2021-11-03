def add_letters(*letters):
    position = [(ord(x)+ 1) - ord('a') for x in letters] # Return the position of the letter in the alphabet
    summing = (sum(position) - 1)
    return chr((summing % 26) + ord('a'))

from string import ascii_lowercase
def add_letters2(*letters):
    alphabet = ascii_lowercase
    result = 0
    for c in letters:
        result = result + alphabet.index(c) + 1       
    return alphabet[(result - 1) % 26]
    
    
print(add_letters('g', 'l'))

