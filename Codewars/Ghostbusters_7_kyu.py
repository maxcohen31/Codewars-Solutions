def ghostbuster(building):
    if ' ' in building:
        return ''.join(building.split())
    else:
       return "You just wanted my autograph didn't you?"
    

x = "O  f fi ce"
y = 'Factor y'
d = 'adsasfa'
print(ghostbuster(y))
print(ghostbuster(d))
