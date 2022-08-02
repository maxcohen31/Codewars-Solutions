def direction(facing, turn):
    wind_rose = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    return wind_rose[(wind_rose.index(facing)+turn//45)%len(wind_rose)]
    
