
class Shape:
    def area(self):
        pass

# Method Overriding
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

# Method Overloading
class Rectangle(Shape):
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def area(self):
        if self.width is not None:
            return self.length * self.width
        else:
            return self.length**2

# Usage
circle = Circle(radius=5)
rectangle_square = Rectangle(length=4)
rectangle_rectangle = Rectangle(length=4, width=6)

# Overriding
print("Area of Circle:", circle.area())

# Overloading
print("Area of Square:", rectangle_square.area())
print("Area of Rectangle:", rectangle_rectangle.area())
