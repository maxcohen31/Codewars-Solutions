def meeting(rooms, need):

    if need == 0:
        return 'Game On'

    n = need
    avaiable_chairs_for_each_room = [chair[1] - len(chair[0]) for chair in rooms]
    result = []
    for chair in avaiable_chairs_for_each_room:
        if chair > 0:
            if chair >= n:
                result.append(n)
                return result
            else:
                result.append(chair)
                n -= chair
        else:
            result.append(0)
    return 'Not enough!'

print(meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4)) # [0, 1, 3]
print(meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5)) # [0, 0, 1, 2, 2]