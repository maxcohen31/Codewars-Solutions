from typing import Dict

def solution(pairs: Dict[str,str]) -> str:
    result = []

    for i in pairs:
        result.append(f"{str(i)} = {str(pairs[i])}")
    return ",".join(sorted(result))

