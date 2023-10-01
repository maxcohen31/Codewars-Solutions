from re import sub

def debug(s: str) -> str:
    # Finds bug that doesn't have an "s" after it
    return sub("bug(?!s))\b", "" ,s)

