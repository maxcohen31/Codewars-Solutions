def encode(st):
    encoded_str = ''
    vowels = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    for idx, vow in enumerate(st):
        for k,v in vowels.items():
            if st[idx] == k:
                vow = str(v)
        encoded_str += vow
    return encoded_str

    
def decode(st):
    decoded_str = ''
    vowels = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u'}
    for idx, vow in enumerate(st):
        for k,v in vowels.items():
            if st[idx] == str(k):
                vow = v
        decoded_str += vow
    return decoded_str


# print(encode('hello'))
print(decode('h2llo'))