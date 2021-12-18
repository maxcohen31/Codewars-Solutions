from math import ceil
def wallpaper(l, w, h):
    numbers = {0: "zero", 
               1: "one", 
               2: "two", 
               3: "three", 
               4: "four", 
               5: "five", 
               6: "six", 
               7: "seven", 
               8: "eight",
               9: "nine", 
               10: "ten", 
               11: "eleven", 
               12: "twelve", 
               13: "thirteen", 
               14: "fourteen", 
               15: "fifteen",
               16: "sixteen", 
               17: "seventeen", 
               18: "eighteen", 
               19: "nineteen", 
               20: "twenty"}
    if l == 0 or w == 0 or h == 0:
        return 'zero'
    roll_area = 10 * 0.52
    return numbers[ceil(((2 * (l * h)) + (2 * (w * h))) * 1.15 / roll_area)]
    
print(wallpaper(6.3, 4.5, 3.29))    
