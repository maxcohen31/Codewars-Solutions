def find_color(x):
    if x > 255:
        x = 255
    if x < 0:
        x = 0
    return '%02x'.upper() % x
    
def rgb(r, g, b):
    return f"{find_color(r)}{find_color(g)}{find_color(b)}"

        
print(rgb(-255, 275, 4))
print(rgb(-255, 34, -4))
print(rgb(24, 33, 666))
