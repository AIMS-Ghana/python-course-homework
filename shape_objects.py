#!/usr/bin/env python3
import math
import turtle
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
        return "triangle"
   def invert_area(self, area):
       return math.sqrt(float((area)*4)/math.sqrt(3))
   def dimname(self):
        return "side"


class Square(Shape):
    def kind(self):
        return "square"
    def dimname(self):
        return "side"
    def invert_area(self, area):
       return area**0.5

from math import pi

class Circle(Shape):
    def kind(self):
        return "circle"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
       return float(math.sqrt(area/math.pi)) 

if __name__ == "__main__":
    circ = Circle(10)
    sq=Square(5)
    tri=Triangle(5)
    print(circ)
    print(sq)
    print(tri)
