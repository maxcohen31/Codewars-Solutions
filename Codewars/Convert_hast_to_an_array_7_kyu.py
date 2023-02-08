from typing import List
def convert_hash_to_array(hash: dict) -> List[List[str|int]]|List[List[str|str]]:
    result = []
    for k, v in hash.items():
        result.append([k, v])

    return result

