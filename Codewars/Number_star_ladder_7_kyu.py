def pattern(n):
    # raise NotImplementedError("TODO: pattern")
    ladder = ""
    for i in range(1, n+1):
        ladder +=  '1'+ f"{'*'*(i-1)}{i}\n"
    return ladder[1:-1]
    
print(pattern(3))