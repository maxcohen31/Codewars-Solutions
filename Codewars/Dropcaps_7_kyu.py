from re import sub

def drop_cap(words: str) -> str:
    matching = sub(r"(\b\w{3,}+)", lambda x: x.group().capitalize(), words)
    return matching
    

