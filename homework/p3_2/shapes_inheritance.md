Certainly! Here's a simple exercise that tests your knowledge of writing a class and inheritance in Python:

**Exercise: Creating a Shape Hierarchy**

Create a Python program that models basic geometric shapes using classes and inheritance. Define a base class called `Shape`. Then, create two subclasses: `Rectangle` and `Circle`. Each class should have methods to calculate the area and perimeter (or circumference in the case of a circle) of the shape.

Here are the steps to complete the exercise:

1. Create a `Shape` class with the following methods:
   - `area()`: This method should return the area of the shape (implement it as a placeholder method).
   - `perimeter()`: This method should return the perimeter of the shape (implement it as a placeholder method).

2. Create a `Rectangle` class that inherits from `Shape`. The `Rectangle` class should have:
   - A constructor `__init__(self, width, height)` that initializes the width and height of the rectangle.
   - Overridden `area()` and `perimeter()` methods to calculate the area and perimeter of the rectangle.

3. Create a `Circle` class that inherits from `Shape`. The `Circle` class should have:
   - A constructor `__init__(self, radius)` that initializes the radius of the circle.
   - Overridden `area()` and `perimeter()` methods to calculate the area and circumference of the circle.

4. Instantiate objects of both the `Rectangle` and `Circle` classes and demonstrate the use of the `area()` and `perimeter()` methods to calculate and print the areas and perimeters (circumferences) of these shapes.

Example usage:
```python
# Create a rectangle and calculate its area and perimeter
rectangle = Rectangle(5, 4)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())

# Create a circle and calculate its area and circumference
circle = Circle(3)
print("Circle Area:", circle.area())
print("Circle Circumference:", circle.perimeter())
```

This exercise will test your ability to define classes, use inheritance, and implement methods for calculating properties of different shapes. It's a great way to practice object-oriented programming concepts in Python.
