#!/usr/bin/env python

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
        return "TRIANGLE"
    def dimname(self):
        return "side"
    def invert_area(self, area):
        return (2*(float( area))**0.5)/3**0.25
    


class Square(Shape):
    def kind(self):
        return "SQUARE"
    def dimname(self):
        return "side"
    def invert_area(self, area):
        return (float (area))**.5

from math import pi

class Circle(Shape):
    def kind(self):
        return "CIRCLE"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
        return (area/pi)**.5

if __name__ == "__main__":
    circ = Circle(10)
    triang = Triangle(10)
    sqr = Square(10)
    print(circ)
    print(triang)
    print(sqr)
