#!/usr/bin/env python3

import math 

class Shape:
    def kind(self):
        return "shape"

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

class Square(Shape):
 def kind(self):
        return "shape"
 

from math import pi

class Circle(Shape):
 def kind(self):
        return "Circle"   


if __name__ == "__main__":
    circ = Circle(10)
    tri= Triangle(5)
    sq=Square(5)
    print(circ)
    print (tri)
    print (sq)
