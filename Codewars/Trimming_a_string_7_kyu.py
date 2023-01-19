def trim(phrase: str, size: int) -> str:
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return f"{phrase[0:size]}..."
    else:
        return f"{phrase[0:size-3]}..."

print(trim("Creating kata is fun", 14))
print(trim("London is freezing", 18))