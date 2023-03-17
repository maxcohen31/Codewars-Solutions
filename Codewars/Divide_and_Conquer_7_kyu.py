from typing import List
def div_con(x: List[int|str]) -> int:
    str_list = [int(i) for i in x if isinstance(i, str)]
    int_list = [i for i in x if isinstance(i, int)]
    return sum(int_list) - sum(str_list)

x = [9, 3, '7', '3']
print(div_con(x))