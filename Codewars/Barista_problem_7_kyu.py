def barista(coffees):
    coffees = sorted(coffees)
    result = 0
    wait = coffees[0]
    
    for c in coffees[1:]:
        result += wait
        wait = wait + c + 2
    return result + wait

# Alternative Solution
def barista2(coffees):
    return [n*(i+1)+2*i for i,n in enumerate(sorted(coffees, reverse=True))]
