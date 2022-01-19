def add(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    num1 = num1.zfill(len(num2))
    num2 = num2.zfill(len(num1))
    result = ""
    zipping = zip(num1, num2)
    for i, j in zipping:
        result += str(int(i) + int(j))
    return result
    
print(add(16, 18))