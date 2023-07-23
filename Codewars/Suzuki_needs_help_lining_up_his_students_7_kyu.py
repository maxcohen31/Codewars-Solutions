from typing import List

def lineup_students(string: str) -> List[str]:
    sorted_list = sorted(sorted(string.split()), key=len, reverse=False)
    return sorted_list[::-1]





s1 = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'
print(lineup_students(s1))
