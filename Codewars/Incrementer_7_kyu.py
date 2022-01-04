def incrementer(nums):
    if len(nums) > 0:
        result = []
        for i, n in enumerate(nums, start=1):
            result.append(i + n)
        for i, n in enumerate(result):
            if n >= 10:
                result[i] = n % 10
        return result
    else:
        return []
                 
# Solution 2
def incrementer2(nums):
    return [((i+n) % 10) for i, n in enumerate(nums, start=1)]
