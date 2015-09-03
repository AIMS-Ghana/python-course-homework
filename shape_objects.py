#!/usr/bin/env python
import math
class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "HUH?"

    def __init__(self, area):
        self.__area = area
        self.__dim = self.invert_area(area)

    strformat = "{}, area: {}, {}: {}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.__area,
          self.dimname(),
          self.__dim
        )

    def draw(turt):
        pass

class Triangle(Shape):
     def kind(self):
        return "Triangle"
     def invert_area(self, area):
        return math.sqrt(area / (math.sqrt(3)))
     def dimname(self):
        return "Side:"
class Square(Shape):
     def kind(self):
        return "Square"
     def invert_area(self, area):
        return math.sqrt(area/pi)
     def dimname(self):
        return "Side"
from math import pi

class Circle(Shape):
     def kind(self):
        return "Circle"

     def invert_area(self, area):
        return math.sqrt(area)

     def dimname(self):
        return "Radius"

if __name__ == "__main__":
    circ = Circle(10)
    Triangle = Triangle(10)
    Square = Square(10)
    print(circ)
    print(Triangle)
    print(Square)
