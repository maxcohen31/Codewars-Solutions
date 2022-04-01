"""
To introduce the problem think to my neighbor who drives a tanker truck. 
The level indicator is down and he is worried because he does not know if he will be able to make deliveries. 
We put the truck on a horizontal ground and measured the height of the liquid in the tank.
Fortunately the tank is a perfect cylinder and the vertical walls on each end are flat. 
The height of the remaining liquid is h, the diameter of the cylinder base is d, the total volume is vt (h, d, vt are positive or null integers). 
You can assume that h <= d.

Could you calculate the remaining volume of the liquid? 
Your function tankvol(h, d, vt) returns an integer which is the truncated result (e.g floor) of your float calculation
"""

from math import cos, sin, acos, pi, floor
def tankvol(h, d, vt):
    r = d / 2   # radius
    theta = acos((r - h) / r) # theta angle 
    cylinder_height = vt / (pi * pow(r, 2)) # cylider height
    oa = r * sin(theta) # triangle base
    ab = r * cos(theta) # triangle height
    triangle_area = (ab * oa) / 2 # triangle area
    sector_area = (pow(r, 2) * theta) / 2 # sector area
    return floor(cylinder_height * (2 * (sector_area - triangle_area))) # result

    
print(tankvol(5, 7, 3848))