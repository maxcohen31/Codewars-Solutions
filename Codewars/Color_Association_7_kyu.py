from typing import List, Dict

def colour_association(arr: List[List[str]]) -> List[Dict[str, str]]:
    return [{color:meaning} for color, meaning in arr]
