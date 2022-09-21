import datetime

days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def day_of_week(date):
    s = datetime.datetime.strptime(date, '%d/%m/%Y').weekday()
    return days[s]

d = "29/02/2016"
print(day_of_week(d))