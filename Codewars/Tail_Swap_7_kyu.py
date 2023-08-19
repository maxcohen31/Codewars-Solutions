from typing import List

def tail_swap(strings: List[str]) -> List[str]:
    new_str = [s.split(':') for s in strings]
    return [new_str[0][0] + ':' +new_str[1][1]] + [new_str[1][0] + ':' + new_str[0][1]]


