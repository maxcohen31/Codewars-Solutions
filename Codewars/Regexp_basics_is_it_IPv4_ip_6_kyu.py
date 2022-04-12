import re
def ipv4_address(address):
    new_address = address.split('.')
    if len(new_address) < 4 or len(new_address) > 4:
        return False

    pattern = r"(([1-9]?\d|25[0-5]|2[0-4]\d|1\d\d)\.){3}([1-9]?\d|25[0-5]|2[0-4]\d|1\d\d)"
    return bool(re.fullmatch(pattern, address))      


# Alternative Solution 
import socket
def ipv4_address_2(address):
    try:
        socket.inet_pton(socket.AF_INET,address)
        return True
    except socket.error: 
        return False

