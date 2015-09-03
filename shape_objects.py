#!/usr/bin/env python3
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
    def dimname(self):
        return "side"
    def invert_area(self, area):
         return (2*(float(area))**0.5)/3**0.25


class Square(Shape):
    def kind(self):
        return "square"
    def dimname(self):
        return "length"
    def invert_area(self, area):
        return (area**0.5)


from math import pi

class Circle(Shape):
    def kind(self):
        return "circle"
    def dimname(self):
        return "radius"
    def invert_area(self, area):
        return (area/pi)**0.5


if __name__ == "__main__":
    circ = Circle(20)
    tri = Triangle(9)
    squa = Square(12)
    print(squa)
    print(tri)
    print(circ)
