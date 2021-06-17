def solution(n):
    result = ''
    list_rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

    list_int = [1000, 900 ,500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom = dict(zip(list_int, list_rom))
    for i in rom.keys():
        while i <= n:
            n -= i
            result += rom[i]
    return result        
        
       