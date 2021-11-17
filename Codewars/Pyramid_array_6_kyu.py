def pyramid(n):
    result = []
    if n == 0:
        return []
    if n > 0:
        for i in range(1, n+1):
            result.append([1]*i)
        return result
        
# Cleaner Solution
def pyramid2(n):
    return [[1]*i for i in range(1, n+1)]        
        
print(pyramid2(3))