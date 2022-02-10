# Technical Interview

def missing_no(nums):
    return [n for n in range(0, 101) if n not in sorted(nums)][0]


def missing_no(nums):
    n = []
    list_of_numbers = [i for i in range(0, 101)]
    for number in list_of_numbers:
        if number not in sorted(nums):
            n.append(number)
    return n        





