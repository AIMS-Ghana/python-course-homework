#!/usr/bin/python
from math import pi
import sys

circle = lambda a : (a/pi)**0.5
triangle = lambda a : 2*(a/(3**0.5))**0.5
square = lambda a : a**0.5

shapes = {'circle' : circle, 'triangle' : triangle, 'square' : square}

def compute(shape, a):
    assert shape in shapes, shape+" not parseable"
    return  shapes[shape](a)

if __name__ == '__main__':
     s = sys.argv[1]
     a = float(sys.argv[2])
     print compute(s, a)   

