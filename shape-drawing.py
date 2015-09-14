#!/usr/bin/env python3


# shape objects calculate sides of figures, given the area
import shape_objects
# draw shape gives a single shape on the canvas
import draw_shape
import turtle

# inspect data for invalid row specifications
def check_input(figures):
    count = 0
    error_format = 'There is a problem with the {0} specified in line {1} of the given input file'
    checks = { 0 : (lambda x: x in ['SQUARE', 'TRIANGLE', 'RECTANGLE', 'CIRCLE'] , 'type'),
               1 : (lambda x: x in ['RED','ORANGE','YELLOW','GREEN','BLUE','PURPLE'] , 'colour'),
               2 : (lambda x: 0 <= float(x) < 360, 'angle'),
               3 : (lambda x: float(x) > 0 ,  'area'),
               4 : (True, 'x-coordinate'),
               5 : (True,'y-coordinate'),
              }
    for row in figures:
        count +=1
        for i in range(4):
            assert (checks[i][0](row[i].split()[0])), error_format.format(checks[i][1], str(count))
    return None


# deal with given row
class paint:
    def __init__(self, row):
        self.__area = float(row[3].split()[0])
        self.__color = row[1].split()[0]
        self.__kind = row[0].split()[0]
        self.__angle, self.__x, self.__y = float(row[2].split()[0]),float(row[4].split()[0]),float(row[5].split()[0])


    def position(self, angle, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(angle)
        turtle.pendown()


    def draw(self):
        self.position(self.__angle, self.__x, self.__y)
        draw_shape.draw(self.__kind, self.__area, self.__color, cont = True)



# Program flow begins here
if __name__ == '__main__':
    import csv
    import sys
    assert (''.join(list(sys.argv[1])[-4:]) == '.csv'), 'The format of the input file is not appropiate. Please specify as \'filename.csv\''
    with open(sys.argv[1]) as input_file:
        figures = csv.reader(input_file, delimiter = ',')
        check_input(figures)
        input_file.seek(0)
        for row in figures:
            #Do diagram justice with data on turtle canvas
            thingy_bobby = paint(row)
            thingy_bobby.draw()
        if len(sys.argv) == 3:
            # Produce out file if asked to do so
            # Should fix this later so that turtle does not animate at all
            assert (''.join(list(sys.argv[2])[-4:]) == '.eps'), 'The format of the output file is not appropiate. Please specify as \'filename.eps\''
            ts = turtle.getscreen()
            ts.getcanvas().postscript( file = sys.argv[2])
