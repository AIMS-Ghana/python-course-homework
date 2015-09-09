#!/usr/bin/python
import sys
import math
from draw import t
import draw_shape
import csv
import turtle


def check(name, area, r, col, x, y):
    # assert (a > 0), "you entered a negative number"
    if name == "TRIANGLE":
        s = 2 * (math.sqrt((float(area) / math.sqrt(3))))
        # print 'equilateral TRIANGLE, area', area, 'side: ', s
        draw_shape.draw_triangle(s, r, col, x, y)
        print (name, s, r, col, x, y)
        # return s


    elif name == "SQUARE":
        q = math.sqrt(float(area))
        # print 'square, area', area, 'side: ', q
        draw_shape.draw(q, r, col, x, y)
        print(name, q, r, col, x, y)
        # return q
        #  elif name == "G_rect":
    #    draw_shape.




    elif name == "CIRCLE":
        v = math.sqrt((float(area) / math.pi))
        # print 'CIRCLE, area', area, 'radius: ',
        draw_shape.CIRC(v, r, col, x, y)
        print(name, v, r, col, x, y)
        # return r

    else:


        pass
        # print("Uknown shape")


if __name__ == "__main__":



    filename = 'pjct.csv'
    filename = (sys.argv[1])

    output = (sys.argv[2])
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            check(str(row[0]), float(row[1]), float(row[2]), str(row[3]), float(row[4]), float(row[5]))
            ts = turtle.getscreen()
            ts.getcanvas().postscript(file="output.eps")
