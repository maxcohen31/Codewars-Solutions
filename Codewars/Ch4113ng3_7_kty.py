def nerdify(txt: str) -> str:
    result = ""
    new_txt = list(filter(lambda x: x in txt, txt))
    nerd_dict = {
        'A': '4', 
        'a': '4',
        'E': '3',
        'e': '3',
        'L': '1',
        'l': '1',
        }
    
    for letter in new_txt:
        if letter in nerd_dict:
            result += nerd_dict[letter]
        else:
            result += letter
    return result

# Alternative solution
def nerdify2(txt: str) -> str:
    return txt.translate(txt.maketrans("AaEel", "44331"))


x = "Fundamentals"
print(nerdify2(x))