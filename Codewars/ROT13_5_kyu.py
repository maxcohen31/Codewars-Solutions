def rot13(message: str) -> str:
    rot_cipher = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 
    't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm':'z', 'n': 'a', 'o':
    'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w':
    'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E':
    'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 
    'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 
    'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
    
    decrypt = ''
    for letter in message:
        if letter == ' ':
            decrypt += ' '  
        elif letter in rot_cipher:
                decrypt += rot_cipher[letter]  
        else:
            decrypt += letter                     

    return decrypt

                             
# Clever Solution
def rot13_2(message: str) -> str:
    letters_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_2 = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    alphabet =  {k:v for k, v in zip(letters_1, letters_2)}
    
    decrypt = ''
    for letter in message:
        if letter not in alphabet:
            decrypt += letter  
            continue                
        decrypt += alphabet[letter]
    return decrypt    
        









