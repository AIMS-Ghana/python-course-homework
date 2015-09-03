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

    def invert_area(self,area):
	return math.sqrt (  float(area*4) / float(math.sqrt(3))    )

    def dimname(self):
        return "Side"


class Square(Shape):
      def kind(self):
        return "Square"

      def invert_area(self,area):
	return (float(area)**(0.5))

      def dimname(self):
        return "Side"

from math import pi

class Circle(Shape):
      def kind(self):
        return "Circle"

      def invert_area(self,area):
	return math.sqrt(float(area)/math.pi)

      def dimname(self):
        return "Radius"

if __name__ == "__main__":
    circ = Circle(10)
    square = Square(4)
    triangle = Triangle(34)
    print(circ)
    print(square)
    print(triangle)
