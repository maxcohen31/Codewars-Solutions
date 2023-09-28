from re import findall, search

def area_code(text: str) -> str:
    return findall("\(([^\)]+)\)", text)[0]

# Alternative Solution
def area_code(text):
    return search("\((\d{3})\)", text).group(1)

