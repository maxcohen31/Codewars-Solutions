from textwrap import wrap
def solution(s):
    s = [','.join(i) for i in s]
    if len(s) % 2 != 0:
        s.append('_')
        return wrap(''.join(s), 2) 
    else:
        return wrap(''.join(s), 2)
    
    
# Alternative Solution
def solution2(s):
    return [(s + '_')[i:i+2] for i in range(0, len(s), 2)]

x = 'Ciao Ema'
print(solution(x))