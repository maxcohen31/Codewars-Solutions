import re
def valid_number(n: str) -> bool:
    re_match2 = bool(re.fullmatch(r"^[+-]?\d*\.[0-9][0-9]$", n))    
    return re_match2