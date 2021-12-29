def lost_sheep(friday,saturday,total):
    summing_sheep_friday = sum(friday)
    summing_sheep_saturday = sum(saturday)
    return total - (summing_sheep_friday + summing_sheep_saturday)
                   
        