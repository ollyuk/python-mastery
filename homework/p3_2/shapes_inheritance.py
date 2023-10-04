# parent class for shapes
class Shape:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        pass


class Circle(Shape):
    def area(self):
        area = self.radius * 3.14
        return area

class Square(Shape):
    def __init__(self, x, y):
        self.length = x
        self.height = y

    def area(self):
        area = self.length * self.height
        return area

circle = Circle(3)

square = Square(3,3)
