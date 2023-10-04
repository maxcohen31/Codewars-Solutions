from typing import List, Type, Dict

def populate_dict(keys: List[str], default: str|int|None) -> Dict[int,str]:
    result = dict()

    for idx, val in enumerate(keys):
        result[val] = default
    return result

