def valid_parentheses(s):
    new_par = []
    for par in s:
        if par == '(':
            new_par.append(par)
        elif par not in ['(', ')']:
            continue
        else:
            try:
                new_par.pop()
            except:
                return False
    if len(new_par) == 0:
        return True
    else:
        return False


