from typing import List, Dict

def user_contacts(data: List[List[str|int]]) -> Dict[str,int]:
    result = dict()
    for contact in data:
        if len(contact) == 2:
            result[contact[0]] = contact[1]
        else:
            result[contact[0]] = None
    return result


data = [["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
print(user_contacts(data))
