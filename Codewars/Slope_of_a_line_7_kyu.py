def getSlope(p1, p2):
    try:
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    except ZeroDivisionError as e:
        return None
    
