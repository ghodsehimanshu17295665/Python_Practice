# Absctraction
# Example 1: Abstract Class for Shapes

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rect = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle Area:", rect.area())
print("Circle Area: ", circle.area())
