from re import sub

def wdm(talk: str) -> str:
    new = talk.replace("puke", "").replace("hiccup", "")
    return " ".join(sub(r"\s+", " ", new).split())


print(wdm("puke All's well hiccup     that ends hiccup well puke"))
print(wdm('puke Love hiccup hiccup most, puke puke puke Trust hiccup hiccup     puke none!'))