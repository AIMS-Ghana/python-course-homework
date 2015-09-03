class Shape:
    def invert_area(area):
        pass

    def dimname():
        return "HUH?"

    def __init__(self, area):
        self.__area = area
        self.__dim = invert_area(area)
        self.__kind = "WHAT?"

    strformat = "{}, area: {}, {}: {}"

    def __str__():
        return strformat.format(
          self.__kind,
          self.__area,
          dimname(),
          self.__dim
        )

    def draw(turt):
        pass

class Triangle(Shape):
    pass

class Square(Shape):
    pass

class Circle(Shape):
    pass