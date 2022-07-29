def points(games):
    points = 0
    for point in games:
        p = point.split(':')
        if int(p[0]) > int(p[1]):
            points += 3
        elif int(p[0]) < int(p[1]):
            points += 0
        else:
            points += 1
    return points 

match = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
# print(points(match))

