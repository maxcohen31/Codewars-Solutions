def evaporator(content, evap_per_day, threshold):
    days = 0
    full_content = 100
    while full_content > threshold:
        full_content -= full_content * (evap_per_day / 100)
        days += 1
    return days    
print(evaporator(10, 10, 5))