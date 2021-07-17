import re
def validPhoneNumber(phoneNumber):
    valid = re.match(r'(^\([0-9]{3}\)) ([0-9]{3}[-.][0-9]{4})$', phoneNumber)
    if valid:
        return True
    else:
        return False    
    
