# Create phone number

def create_phone_number(n):
    
    full_str = ''.join([str(numb) for numb in x])
    return f'({full_str[0:3]})' + ' ' + f'{full_str[3:6]}' + '-' + f'{full_str[6:10]}'
        
        
def create_phone_number_2(x):
    
    phone_number = "({}{}{}) {}{}{}-{}{}{}{}".format(*x)
    return phone_number
        

