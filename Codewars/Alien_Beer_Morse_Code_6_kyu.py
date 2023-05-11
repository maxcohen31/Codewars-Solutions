from itertools import islice

def morse_converter(string: str) -> int:

    alien_dict = {
        ".----": 1,
        "..---": 2,
        "...--": 3,
        "....-": 4,
        ".....": 5,
        "-....": 6, 
        "--...": 7,
        "---..": 8,
        "----.": 9,
        "-----": 0
    }

    split_message = [string[i:i+5] for i in range(0, len(string), 5)]
    return int("".join([str(alien_dict[i]) for i in split_message if i in alien_dict]))

print(morse_converter( "---..-----...--"))