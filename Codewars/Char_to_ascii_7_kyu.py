from typing import Dict
from re import findall

def char_to_ascii(s: str) -> Dict[str, int]:
    if s == "":
        return None
    characters = findall(r"[a-zA-Z]", s)
    return {c:ord(c) for c in "".join(char for char in characters)}
    
