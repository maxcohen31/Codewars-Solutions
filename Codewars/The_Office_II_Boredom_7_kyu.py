def boredom(staff):

    departments = {
        'accounts': 1,
        'finance' : 2,
        'canteen': 10,
        'regulation': 3,
        'trading': 6,
        'change': 6,
        'IS': 8,
        'retail': 5,
        'cleaning': 4,
        'pissing about': 25
    }
    
    tot_boredom = 0

    for k, v in departments.items():
        for v1 in staff.values():
            if v1 == k:
                tot_boredom += v
    # return tot_boredom
    if  tot_boredom <= 80:
        return 'kill me now'
    elif tot_boredom > 80 and tot_boredom < 100:
        return 'i can handle this'
    return 'party time!!'


print(boredom({"tim": "change", "jim": "accounts",
  "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
  "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
  "mr": "finance" }))