from math import floor
def convert(degrees):
    if degrees == int(degrees):
        return [degrees]
    elif degrees == float(degrees):
        minutes = (degrees - floor(degrees)) * 60
        seconds = round((floor(minutes) - minutes) * -60)
        if floor(seconds) == 0 and floor(minutes) == 0 and floor(degrees) == 0:
            return [0]
        if seconds == int(0.0):
            return [floor(degrees), floor(minutes)] 
        else:
            return [floor(degrees), floor(minutes), floor(seconds)]




