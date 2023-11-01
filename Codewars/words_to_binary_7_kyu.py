from typing import List

"""

    Write a function that takes a string and returns an array containing binary
    numbers equivalent to the ASCII codes of the characters of the string. The
    binary strings should be eight digits long.

"""


def word_to_bin(word: str) -> List[str]:
    result = []
    
    for char in word:
        result.append(bin(ord(char))[2:].zfill(8))
    return result
    

if __name__ == "__main__":
   print(word_to_bin("man"))
   
