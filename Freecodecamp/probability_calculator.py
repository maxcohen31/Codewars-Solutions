import copy
import random

class Hat:
    
    def __init__(self, **kwargs):
        
        self.contents = []
        for key, value in kwargs.items():
            for x in range(value):
                return self.contents.append(key)
            
    def draw(self, balls):
        
        draw = []
        contents_copy = copy.copy(self.contents)
                
        if balls >= len(contents_copy):
            return self.contents
        for x in range(balls):
            draw_ball = contents_copy.pop(int(random.randint(0, len(contents_copy) -1)))
            draw.append(draw_ball)   
        return draw 
             

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    n = 0
    m = num_experiments
    
    for x in range(num_balls_drawn):
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)
        for color, number in expected_balls.items():
            ball_color = drawn.count(color)
            if ball_color < balls:
                break
         
            n += 1
        return n / m        
    
    
    
          
          
hat = Hat(blue = 5, red = 4, green = 2)
e = experiment(hat, expected_balls = {'red': 2, 'green': 1}, num_balls_drawn = 5, num_experiments = 2000)
print(e)          
            
            
          



        