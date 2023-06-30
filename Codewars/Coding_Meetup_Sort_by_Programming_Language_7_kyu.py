from Typing import List
def sort_by_language(arr: List[dict]) -> List[dict]:
    return sorted(arr, key=lambda x: (x["language"], x["first_name"]), reverse=False)