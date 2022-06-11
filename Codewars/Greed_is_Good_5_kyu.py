from collections import Counter
def score(dice):
    
    result = 0
    dice = Counter(dice)
    tot_point = {'1':1000, '6':600, '5':500, '4':400, '3':300, '2':200}
    
    for k, v in dice.items():
            if v == 3:
                result += tot_point[str(k)]
            elif v > 3:
                result += tot_point[str(k)]
                
                if k == 1:
                    result += (v-3) * 100
                elif k == 5:
                    result += (v-3) * 50
            else:
                if k == 1:
                    result += v * 100
                if k == 5:
                    result += v * 50
    return result

# print(score([2, 3, 4, 6, 2])) # 0
print(score([1, 1, 1, 3, 1])) # 1100
# print(score([4, 4, 4, 3, 3]))
print(score([2, 4, 4, 5, 4])) # 450