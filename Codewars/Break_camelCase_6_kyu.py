import re
def solution(s):
    return re.sub(r"([A-Z][a-z]+)", r' \1', s)



print(solution('breakCamelCase'))