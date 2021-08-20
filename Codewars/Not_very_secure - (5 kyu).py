def alphanumeric(password):
    return password.isalnum()
    
# Alternative Solution using regular expressions
import re
def alphanumeric_2(password):
    return bool(re.match('^[a-zA-Z0-9]+$', password))
    

