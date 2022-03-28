import datetime

def most_frequent_days(year):
    values_of_days = []
    days = {'Monday': 1, 
            'Tuesday': 2, 
            'Wednesday': 3, 
            'Thursday': 4, 
            'Friday': 5, 
            'Saturday': 6,
            'Sunday': 7
            }
    
    start_of_the_year = datetime.date(year, 1, 1)
    end_of_the_year = datetime.date(year, 12, 31)
    first_year_day = start_of_the_year.isoweekday()
    end_year_day = end_of_the_year.isoweekday()
    
    for k, v in days.items():
        if v == end_year_day and end_year_day == first_year_day:
            values_of_days.append(k)
            return values_of_days
        elif first_year_day == v and first_year_day > end_year_day:
            values_of_days.append(end_year_day)
            values_of_days.append(first_year_day)
        elif first_year_day == v and first_year_day < end_year_day:
            values_of_days.append(first_year_day)
            values_of_days.append(end_year_day)    
    
    result = []
    for k, v in days.items():
        for value in values_of_days:
            if value == v:
                result.append(k)        
        
    return result
    

print(most_frequent_days(2000))