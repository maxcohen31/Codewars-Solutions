from math import ceil
def buses(kids: int, adults: int, places: int) -> int:
    if places == 0:
        return 0

    buses = ceil((kids + adults) / places)
    if adults < 2 * buses and kids > 0:
        return 0
    return buses
    
