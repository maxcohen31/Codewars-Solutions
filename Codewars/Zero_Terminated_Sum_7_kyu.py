def largest_sum(s: str) -> int:
    new_s = s.split('0')
    sum_of_numb = [sum(int(i) for i in numbs) for numbs in new_s]
    return max(sum_of_numb)
