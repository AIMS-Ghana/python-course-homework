#!/usr/bin/python

from math import pi

def circle(a:float) -> float:
    return (a/pi)**0.5

def square(a:float) -> float:
    return a**0.5

def triangle(a:float) -> float:
    return 2*(a/(3**0.5))**0.5

shaper = {
  'CIRCLE': circle,
  'TRIANGLE': triangle,
  'SQUARE': square
}

mod = {
    'TRIANGLE':'equilateral '
}

name_shape = {
    'CIRCLE':'radius'
}

def calc_shape(shape:str, a:float) -> float:
    assert shape in shaper, "Shape "+shape+" revise your shape"
    return shaper[shape](a)

import sys

if __name__ == "__main__":
    assert len(sys.argv) == 3, "input SHAPE, area as arguments"
    shape = sys.argv[1]
    area = float(sys.argv[2])
    out = "{}{}, area {}, {}: {}"
    print(out.format(
      mod .get(shape,''),
      shape,
      area,
      name_shape.get(shape,'side'),
      calc_shape(shape, area)
    ))
