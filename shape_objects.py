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
    def invert_area(self, area):
        return ((area*4)**0.5)/3
    def dimname(self):
        return "side"

class Square(Shape):
    def kind(self):
        return "Square"
    def invert_area(self, area):
        return area**0.5
    def dimname(self):
        return "side"


from math import pi

class Circle(Shape):
    def kind(self):
        return "Circle"
    def invert_area(self, area):
        return (area/pi)**0.5
    def dimname(self):
        return "side"

if __name__ == "__main__":
    circ = Circle(10)
    tri = Triangle(10)
    squa = Square(8)  
    print(circ)
    print(tri)
    print(squa)
