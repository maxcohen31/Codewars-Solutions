def bouncing_ball(h, bounce, window):
    rebounds = -1
    while h > 0 & 0 < bounce < 1 and window < h:
        h = bounce * h 
        rebounds += 2
    return rebounds   
    
print(bouncing_ball(3, 0.66, 1.5))    
print(bouncing_ball(2, 0.5, 1))    
