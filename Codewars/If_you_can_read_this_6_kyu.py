def to_nato(words):
    alphabet = {
        "A":"Alfa",
        "B":"Bravo",
        "C":"Charlie",
        "D":"Delta",
        "E":"Echo",
        "F":"Foxtrot",
        "G":"Golf",
        "H":"Hotel",
        "I":"India",
        "J":"Juliett",
        "K":"Kilo",
        "L":"Lima",
        "M":"Mike",
        "N":"November",
        "O":"Oscar",
        "P":"Papa",
        "Q":"Quebec",
        "R":"Romeo",
        "S":"Sierra",
        "T":"Tango",
        "U":"Uniform",
        "V":"Victor",
        "W":"Whiskey",
        "X":"Xray",
        "Y":"Yankee",
        "Z":"Zulu",
        ",": ",",
        ".": ".",
        "?": "?",
        "!": "!"
        }
    
    result = ''
    for word in words:
        for k, v in alphabet.items():
            if word.upper() == k:
                result += ''.join(v + ' ')
    return result[:-1]

print(to_nato('If, you can read this'))