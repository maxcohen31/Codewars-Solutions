from typing import Dict, List

def ranking(people: List[Dict[str,int]]) -> List[Dict[str,int]]:
    new_dict = sorted(sorted(people, key=lambda x: x["name"]), key=lambda x: x["points"], reverse=True)

    position = 1
    for plp in new_dict:
        plp["position"] = position
    
    for idx in range(1, len(new_dict)):
        if new_dict[idx]["points"] == new_dict[idx-1]["points"]:
            new_dict[idx]["position"] = new_dict[idx-1]["position"]
            position += 1
        else:
            position += 1
            new_dict[idx]["position"] = position
    return new_dict



p = [
    {'name': 'Bob', 'points': 100},
    {'name': 'John', 'points': 100}, 
    {'name': 'Mary', 'points': 100} # should be 1 
    ]
    



people1 = [
        {
            "name": "John",
            "points": 100,
        },
        {
            "name": "Bob",
            "points": 130,
        },
        {
            "name": "Mary",
            "points": 120,
        },
        {
            "name": "Kate",
            "points": 120,
        }
    ]

print(ranking(p))
print(ranking(people1))
