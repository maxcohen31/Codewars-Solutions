def covfefe(s: str) -> str:
    s = s[:]
    result = ""
    
    if "coverage" in s:
        result = s.replace("coverage", "covfefe")
    else:
        result = f"{s} covfefe"
    
    return result


