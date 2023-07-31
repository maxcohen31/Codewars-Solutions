def to_leet_speak(s: str) -> str: 
    new_string = [letter for letter in s]
    alphabet = {
    "A" : '@',
    "B" : '8',
    "C" : '(',
    "D" : 'D',
    "E" : '3',
    "F" : 'F',
    "G" : '6',
    "H" : '#',
    "I" : '!',
    "J" : 'J',
    "K" : 'K',
    "L" : '1',
    "M" : 'M',
    "N" : 'N',
    "O" : '0',
    "P" : 'P',
    "Q" : 'Q',
    "R" : 'R',
    "S" : '$',
    "T" : '7',
    "U" : 'U',
    "V" : 'V',
    "W" : 'W',
    "X" : 'X',
    "Y" : 'Y',
    "Z" : '2'
     }

    result = []
    for i in new_string:
        if i == " ":
            result.append(i)
        for k, v in alphabet.items():
            if i == k:
                result.append(v)
    return "".join(result)


print(to_leet_speak("HELLO WORLD"))

    


