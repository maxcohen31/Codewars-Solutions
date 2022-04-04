from math import sqrt    
def predict_age2(*ages):
    return sqrt(sum([i ** 2 for i in ages])) // 2

print(predict_age2(65, 60, 75, 55, 60, 63, 64, 45))