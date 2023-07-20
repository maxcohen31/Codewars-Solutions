from typing import Dict, List

def killer(suspect_info: Dict[str, List[str]], dead:List[str]) -> str:
    sus = {k: v for k, v in suspect_info.items() if all(n in v for n in dead)}
    return list(sus.keys())[0]

    
    

s = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}
d = ['Lucas', 'Bill']
print(killer(s, d))
