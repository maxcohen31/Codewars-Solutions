def mxdiflg(a1, a2):
    
    if a1 == a2 == []:
        return -1
    
    result = []
    first = [str(len(i)) for i in a1]
    second = [str(len(i)) for i in a2]
    
    if first == [] or second == []:
        return -1
    elif first == [] and second == []:
        return -1
    else:
        for i in first:
            for j in second:
                result.append(abs(int(i) - int(j)))
    return max(result)       
    
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

print(mxdiflg(a1, a2))