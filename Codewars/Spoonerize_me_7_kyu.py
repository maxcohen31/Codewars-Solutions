def spoonerize(words):
    # ...aaaaand SPOONERIZE!
    words = words.split()
    first_letter = words[0][0]
    second_letter = words[1][0]
    return f"{second_letter + words[0][1:]} {first_letter + words[1][1:]}"



print(spoonerize('wedding bells'))