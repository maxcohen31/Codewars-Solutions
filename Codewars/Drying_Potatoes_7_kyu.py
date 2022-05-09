from math import floor
def potatoes(p0, w0, p1):
    return floor(w0 * (100 - p0) / (100 - p1))