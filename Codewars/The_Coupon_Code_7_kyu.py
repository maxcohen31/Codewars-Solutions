import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    
    current_date = datetime.datetime.strptime(current_date, '%B %d, %Y')
    expiration_date = datetime.datetime.strptime(expiration_date, '%B %d, %Y')
    
    if entered_code == correct_code and type(entered_code) == type(correct_code):
        if expiration_date < current_date:
            return False
        elif expiration_date == current_date:
            return True
        elif expiration_date >= current_date:
            return True
    else:
        return False
    
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015"))