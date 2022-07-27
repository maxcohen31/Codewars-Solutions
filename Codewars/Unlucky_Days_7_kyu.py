from datetime import date, timedelta
def unlucky_days(year):
    result = []
    day_1 = date(year, 1, 1)
    day_365 = date(year, 12, 31)
    
    while day_1 < day_365:
        if day_1.isoweekday() == 5 and day_1.day == 13:
            result.append(day_1)
        day_1 += timedelta(days=1)
    return len(result)
        
print(unlucky_days(1634))
