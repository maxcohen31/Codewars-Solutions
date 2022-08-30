def stock_list(listOfArt: list, listOfCat: list) -> str:

    if len(listOfCat) == 0 or len(listOfArt) == 0:
        return ''

    letters = [l.split()[0][0] for l in listOfArt]
    values = [l.split()[-1] for l in listOfArt]
    result = {k:0 for k in listOfCat}
    letters_value = zip(letters, values)
    string = ''

    for i, j in letters_value:
        if i in listOfCat and len(listOfCat) > 0:
            result[i] += int(j)

    for k, v in result.items():
        string += f"({k} : {v}) - "
    return string.rstrip('-')[:-3] 


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
d = ["A", "B", "C", "D"]
x = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
y = ['N', 'R']
print(stock_list(b, c))
print(stock_list(x, y))

