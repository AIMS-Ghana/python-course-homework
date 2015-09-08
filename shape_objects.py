#!/usr/bin/env python3

class Shape:
    def kind(self):
        return "Shape"

    def invert_area(self, area):
        return area

    def dimname(self):
        return "Side"

    def __init__(self, area):
        self.__area = area
        self.__dim = self.invert_area(area)

    strformat = "{0}, area: {1}, {2}: {3}"

    def __str__(self):
        return Shape.strformat.format(
          self.kind(),
          self.__area,
          self.dimname(),
          self.__dim
        )

    def check(self, area):
        assert (area >=0 ), "Area cannot be negative"


    def draw(turt):
        pass

class Triangle(Shape):
    def kind(self):
        return "TRIANGLE"

    def invert_area(self, area):
        self.check(area)
        return ((16*area**2)/3)**(0.25)


class Square(Shape):
    def kind(self):
        return "SQUARE"

    def invert_area(self,area):
        self.check(area)
        return area**(0.5)

from math import pi


class Circle(Shape):
    def kind(self):
        return "CIRCLE"

    def invert_area(self, area):
        self.check(area)
        return (area/pi)**(0.5)

    def dimname(self):
        return "Radius"


if __name__ == "__main__":
    import sys
    shapes = {
               "CIRCLE":Circle,
               "SQUARE":Square,
               "TRIANGLE":Triangle
             }
    assert (len(sys.argv) == 3), "Input format not appropriate. Specify type, and then area of shape."
    assert (sys.argv[1] in shapes ), "Shape type not understood"
    given = shapes[sys.argv[1]](10)
    print(given)