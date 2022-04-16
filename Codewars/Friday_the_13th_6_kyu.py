from datetime import date, timedelta
def friday_the_thirteenths(start, end = None):
    if end == None:
        result = []
        day_1 = date(start, 1, 1)
        day_365 = date(start, 12, 31)
    
        while day_1 < day_365:
            if day_1.isoweekday() == 5 and day_1.day == 13:
                result.append(day_1)
            day_1 += timedelta(days=1)
        return ' '.join(i.strftime('%-m/%-d/%Y') for i in result)

    elif end != None:
        result = []
        day_1 = date(start, 1, 1)
        day_365 = date(end, 12, 31)
    
        while day_1 < day_365:
            if day_1.isoweekday() == 5 and day_1.day == 13:
                result.append(day_1)
            day_1 += timedelta(days=1)
        return ' '.join(i.strftime('%-m/%-d/%Y') for i in result)
        
        
print(friday_the_thirteenths(1999, 2000))
print(friday_the_thirteenths(2000))