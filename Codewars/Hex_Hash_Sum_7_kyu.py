import re
def hex_hash(code):

    code = list(code)
    hex_string = ""
    hex_arr = ''.join([hex(ord(i))[2:] for i in code])
    numbers = re.findall(r"[0-9]", hex_arr)
    return sum(int(number) for number in numbers)


x = "Yo"
p = 'dhsajkbfyewquilb4y83q903ybr8q9apf7\9ph79qw0-eq230br[wq87r0=18-[#20r370B 7Q0RFP23B7'
print(hex_hash(p))