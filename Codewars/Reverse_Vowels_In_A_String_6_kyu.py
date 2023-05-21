def reverse_vowels(s: str) -> str:
    chars = list(s)
    start = 0
    end = len(s) - 1
    
    while start < end:
        if chars[start].lower() not in "aeiou":
            start += 1
            continue
        elif chars[end].lower() not in "aeiou":
            end -= 1
            continue
        chars[start], chars[end] = chars[end], chars[start]
        start += 1
        end -= 1
    return "".join(chars)
