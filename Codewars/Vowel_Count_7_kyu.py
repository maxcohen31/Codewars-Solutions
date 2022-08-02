def get_count(input_str):
    vowels = []
    num_vowels = 0
    for v in input_str:
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            num_vowels += 1
            vowels.append(num_vowels)
    return len(vowels)

print(get_count('tre'))
