def count_odd_pentaFib(n):
    
    if 1 <= n <= 4:
        return 1
    elif n == 0:
        return 0
    
    starting_numbers = [0, 1, 1, 2, 4]
    
    for i in range(n):
        starting_numbers.append(sum(starting_numbers[(len(starting_numbers)-5):len(starting_numbers)]))
    
    output = starting_numbers[0:n+1]
    return len([i for i in output if i % 2 != 0]) - 1

def count_odd_pentaFib2(n):
    
    if n == 0:
        return 0

    seq = [0, 1, 1, 2, 4]
    a, b, c, d, e = 0, 1, 1, 2, 4
    for _ in range(n-4):
        f = a + b + c + d + e
        a = b
        b = c
        c = d
        d = e
        e = f
        seq.append(e)
    
    return len([i for i in seq[0:n-1] if i % 2 != 0]) - 1



print(count_odd_pentaFib(10))
print(count_odd_pentaFib2(10))