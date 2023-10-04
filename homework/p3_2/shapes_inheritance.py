# parent class for shapes
class Shape:
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def area(self):
        area = self.radius * 3.14
        return area

    def perimeter(self):
        return 2 * 3.14 * self.radius
    

class Rectangle(Shape):
    def __init__(self, x, y):
        self.length = x
        self.height = y

    def area(self):
        area = self.length * self.height
        return area

    def perimeter(self):
        return (self.length + self.height) * 2


class Square(Shape):
    def __init__(self, x):
        self.side = x

    def area(self):
        area = self.side**2 
        return area

    def perimeter(self):
        return 4 * self.side


circle = Circle(3)

rectangle = Rectangle(3,3)

square = Square(3)
