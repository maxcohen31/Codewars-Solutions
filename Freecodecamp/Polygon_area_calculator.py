# Polygon Area Calculator

from math import sqrt

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, chosen_width):
        self.width = chosen_width

    def set_height(self, chosen_height):
        self.height = chosen_height

    def __str__(self):
         return 'Rectangle(width = {}, height = {})'.format(self.width, self.height)

    def area(self):
        self.area = self.width * self.height
        return self.area

    def get_diagonal(self):
        self.diagonal = sqrt(self.width ** 2 + self.height ** 2)
        return self.diagonal

    def perimeter(self):
        self.perimeter = self.width * 2 + self.height * 2
        return self.perimeter

    def get_picture(self):
        if self.width > 50 or self.height > 50:
             print('Too big for picture')

        else:
            for w in range(self.width):
                for h in range(self.height):
                    print('*', end = '')
                print()


    def get_amount_inside(self, new_shape):
        return self.area() // new_shape.area()


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
            self.width = side
            self.height = side
            return self.width, self.height

    def __str__(self):
        return 'Square(side = {})'.format(self.side)
