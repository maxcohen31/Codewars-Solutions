import re
def case_id(c_str: str) -> str:
    if c_str != c_str.islower() and c_str != c_str.upper() and "-" not in c_str and "_" not in c_str:
        return "camel"

    snake = bool(re.match(r"^([a-z]{1,})(_[a-z0-9]{1,})*$", c_str))
    kebab = bool(re.match(r"^([a-z]{1,})(-[a-z0-9]{1,})*$", c_str))
    if snake:
        return "snake"
    elif kebab:
        return "kebab"
    else:
        return "none"

