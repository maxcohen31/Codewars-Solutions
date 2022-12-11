def der_die_das(wort):
    vowels = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
    result = ""
    count_vow = 0

    for i in wort.lower():
        if i in vowels:
            count_vow += 1
    
    if count_vow < 2:
        result = "das " + wort
    elif count_vow < 4:
        result = "die " + wort
    else:
        result = "der " + wort
    
    return result

print(der_die_das("OOOpa"))
print(der_die_das("Knödel"))
