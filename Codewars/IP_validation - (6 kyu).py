def is_valid_IP(ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    for number in ip:
        if number.isdigit() == False:
            return False
        if number.find('0') == 0 and int(number) != 0:
            return False
        if int(number) > 255 or int(number) < 0:
            return False
    return True    

# Alternative method
def is_valid_IP2(ip):
    ip = ip.split('.')
    n = 0
    for element in ip:
        if element.isdigit():
            if int(element) > 0 and int(element[0]) == 0:
                return False
            if int(element) >= 0 and int(element) < 256:
                n += 1
    return n == 4        
                     
                    
                         
                         
                         
  