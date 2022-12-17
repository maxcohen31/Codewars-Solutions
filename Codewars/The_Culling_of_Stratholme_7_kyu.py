import re
def purify(s: str) -> str:
    result = ""
    s1 = s.split()

    for w in s1:
        x = re.sub(r".?[iI]+.?", "", w)
        result += " " + x
        
    return ' '.join(result.split())
    



print(purify("Pineapple pizza is delicious")) # "eapple za deus"
print(purify("In heaven all the interesting people are missing")) # heaven all the teresg people are g