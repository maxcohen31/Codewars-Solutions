from typing import Tuple, List

def count_vegetables(string: str) -> List[Tuple[int, str]]:
    vegetables = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]
    new_veg = [i for i in string.split() if i in vegetables]
    count_veg = {i:new_veg.count(i) for i in new_veg}
    return sorted([(v, k) for k,v in count_veg.items()], reverse = True)

    
    



s1 = 'potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage' 
print(count_vegetables(s1))


    
