from math import pi

class Sphere:
    def __init__(self, radius: int, mass: int) -> None:
        self.radius = radius
        self.mass = mass
    
    def get_radius(self) -> int:
        return self.radius

    def get_mass(self) -> int:
        return self.mass
    
    def get_volume(self) -> float:
        return round((4/3) * pi * self.radius**3, 5)
    
    def get_surface_area(self) -> float:
        return round((4 * pi * self.radius**2), 5)

    def get_density(self) -> float:
        return round(self.mass/self.get_volume(), 5)



if __name__ == "__main__":
    s = Sphere(2, 50)
    print(s.get_density())