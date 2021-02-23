def add_time(time1, time2):
    
    # Splitting time1 and time2
    
    time1 = time1.split()
    time1_for = time1[1]
    time1_hour_spl = time1[0].split(':')
    time1_hour_splt = time1_hour_spl[0]
    time1_min = time1_hour_spl[1]
    time2 = time2.split(':')
    time2_hour = time2[0]
    time2_minutes = time2[1]
    minutes_sum = int(time1_min) + int(time2_minutes)
    hours_sum = int(time1_hour_splt) + int(time2_hour) % 12

    # Checking for minutes more than 60, if so add 1 hour
   
    if minutes_sum >= 60:
        minutes_sum = minutes_sum - 60
        hours_sum += 1
    
    if minutes_sum < 10:
        minutes_sum = '0' + str(minutes_sum)

    if time1_for == 'AM' and hours_sum >= 12:
        time1_for = 'PM'
    elif time1_for == 'PM' and hours_sum >= 12:
        time1_for = 'AM'
    elif time1_for == 'AM' and hours_sum < 12:
        time1_for == 'AM'
    elif time1_for == 'PM' and hours_sum < 12:
        time1_for == 'PM'     
    
    
    clock = str(hours_sum) + ':' + str(minutes_sum) + ' ' + time1_for
    return clock

