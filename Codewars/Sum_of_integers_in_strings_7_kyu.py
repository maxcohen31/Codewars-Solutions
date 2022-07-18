import re
def sum_of_integers_in_string(s):
    start_sum = 0
    s = re.findall('\d+', s)
    for n in s:
        start_sum += int(n)
    return start_sum           


def sum_of_integers_in_string2(s):
    return sum(int(n) for n in re.findall('\d+', s)) 

x = "C4t5 are 4m4z1ng."
q = "The Great Depression lasted from 1929 to 1939."
print(sum_of_integers_in_string2(q))