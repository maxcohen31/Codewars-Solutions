# CodeWars >> Square every digits

def square_digits(num):
    
    dig = []
    for n in str(num):
        dig.append(str(int(n) ** 2))
    return int(''.join(dig))

print(square_digits(9119))
