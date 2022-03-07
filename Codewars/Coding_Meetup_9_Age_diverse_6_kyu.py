def is_age_diverse(lst): 
    a, b, c, d, e, f, g ,h, i, l = False, False, False, False, False, False, False, False, False, False
    for person in lst:
        if person['age'] < 20:
            a = True
        elif person['age'] >= 20 and person['age'] < 30:
            b = True
        elif person['age'] >= 30 and person['age'] < 40:
            c = True
        elif person['age'] >= 40 and person['age'] < 50:
            d = True
        elif person['age'] >= 50 and person['age'] < 60:
            e = True
        elif person['age'] >= 60 and person['age'] < 70:
            f = True
        elif person['age'] >= 70 and person['age'] < 80:
            g = True
        elif person['age'] >= 80 and person['age'] < 90:
            h = True                
        elif person['age'] > 90 and person['age'] < 100:
            i = True
        elif person['age'] > 100:
            l = True
    if a == b == c == d == e == f == g == h == i == l:
        return True
    return False       