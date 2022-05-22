def min_max(lst):
    min_max = []
    max_ = max(lst)
    min_ = min(lst)
    min_max.append(min_)
    min_max.append(max_)
    return min_max if len(lst) >= 2 else [lst[0], lst[0]]


print(min_max([2342432, 5]))