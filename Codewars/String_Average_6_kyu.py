from math import floor
from statistics import mean 
def average_string(s:str) -> str:
    new_str = s.split()
    numbers = []
    digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    if s == "":
        return "n/a"
    for n in new_str:
        if n not in digits:
            return "n/a"
    for idx, num in enumerate(new_str):
        if num in digits:
            numbers.insert(idx, digits[num])
    return list(digits.keys())[list(digits.values()).index(floor(mean(numbers)))]
    




x = "zero nine five two"
y = "one one eight one"
a = 'fa'
print(average_string(x))
print(average_string(y))