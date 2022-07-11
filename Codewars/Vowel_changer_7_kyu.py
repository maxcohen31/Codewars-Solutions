def vowel_change(txt, vow):
    vowels = "aeiou"
    for char in txt:
        if char in vowels:
            txt = txt.replace(char, vow)
    return txt

print(vowel_change('ciao', 'a'))