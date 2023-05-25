from re import match

def validate_time(time: str) -> bool:
    return bool(match(r"([01]?[0-9]|2[0-3]):[0-5]+[0-9]+", time))
