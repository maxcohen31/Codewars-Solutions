from typing import List

def geo_mean(nums: List[int], arith_mean: int|float) -> int|float:
    nums = nums[:]
    list_lenght = len(nums) + 1
    missing_numb = (arith_mean * list_lenght) - sum(nums)
    nums.append(missing_numb)
    
    # Geometric mean
    mult = 1
    for n in nums:
        mult *= n
    return pow(mult, 1/list_lenght)
    

print(geo_mean([1, 2], 3))