from re import findall

def solution(full_text: str, search_text: str) -> int:
    return len(findall(search_text, full_text))


