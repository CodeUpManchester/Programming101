from abc import ABCMeta, abstractmethod
from math import pi, sqrt

# Make Shape, an abstract class which can't be instantiated.
# Force subclasses to define ways of working out the area and
# and perimeter by forcing subclasses to have functions with
# those names.
class Shape:
    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# First-level subclasses descended from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * pow(self.radius, 2) # pi r-squared

    def perimeter(self):
        return 2 * pi * self.radius     # 2 pi r

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Heron's formula
        p = perimeter() / 2.0
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# *We* know that squares must be the same width and height, but the
# program needs to enforce that too, so we need to restrict setting
# of width and height. We do it by defining private (underscored)
# class variables and controlling how they are used.
class Square(Shape):
    def __init__(self, edge):
        self._width = edge
        self._height = edge

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._setEdges(value)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._setEdges(value)

    def _setEdges(self, value):
        self._width = value
        self._height = value

    # The Rectangle class will work out area and perimeter in the
    # same way, so we define the functions here using width and height.
    def area(self):
        return self.width * self.height

    def perimeter(self):
        total = self.width * 2
        total += self.height * 2
        return total

# Finally, we define a second-level subclass descended from Square.
# Notice we don't have to redefine area() and perimeter().
class Rectangle(Square):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Adding this line means it also conforms to the Liskov
    # substitution principle (Google it ;)
    def __init__(self, edge):
        self._setEdges(edge)

    # Width and height can now be set
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
