from re import sub

def fire_fight(s: str) -> str:
    return sub("Fire", "~~", s)
