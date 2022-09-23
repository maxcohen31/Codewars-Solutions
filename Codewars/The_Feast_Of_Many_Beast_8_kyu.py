def feast(beast, dish):
    first_b = beast[0]
    last_b = beast[-1]
    first_d = dish[0]
    last_d = dish[-1]
    
    return first_b == first_d and last_b == last_d


# Alternative Solution
def feast2(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

print(feast("great blue heron", "garlic naan"))
 