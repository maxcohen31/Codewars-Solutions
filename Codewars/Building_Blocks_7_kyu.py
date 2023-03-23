from typing import List
class Block:
    def __init__(self, lst: List) -> None:
        self.lst = lst
        
    def get_width(self) -> int:
        return self.lst[0]
    
    def get_length(self) -> int:
        return self.lst[1]
    
    def get_height(self) -> int:
        return self.lst[2]
    
    def get_volume(self) -> int:
        return self.lst[0] * self.lst[1] * self.lst[2]
    
    def get_surface_area(self) -> int:
        return 2 * (self.lst[1] * self.lst[2] + self.lst[0] * self.lst[1] + self.lst[0] * self.lst[2])

b = Block([27, 92, 43])
print(b.get_surface_area())