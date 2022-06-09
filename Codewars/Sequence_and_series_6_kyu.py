def get_score(n):
    if n == 1:
        return 50
    else:
        result = []
        start = 50
        count = 100
        for i in range(0, n-1):
            count += 50
            start = start + count - 50
            result.append(start)
        return result[-1]


    