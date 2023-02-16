def freq_seq(s: str, sep: str) -> str:
    new_s = list(s[:])
    result = []

    for letter in new_s:
        x = new_s.count(letter)
        result.append(str(x))
        
    return sep.join(result)





print(freq_seq("hello world", "-"))
